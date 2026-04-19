#!/usr/bin/env python3
"""
Freedom Fighters Dev Server
- Serves index.html on LAN (all devices on your network)
- Auto-reloads connected browsers when index.html changes
- No installs needed, Python 3 only

Usage:  python3 dev.py [port]
Default port: 8080
"""

import http.server
import ipaddress
import os
import socket
import subprocess
import sys
import time
from urllib.parse import urlparse

# ─── Config ──────────────────────────────────────────────────────────
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
GAME_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(GAME_DIR, "index.html")

_last_hash = None

def get_file_hash():
    """Get hash of index.html for change detection."""
    try:
        with open(INDEX, "rb") as f:
            import hashlib
            return hashlib.md5(f.read()).hexdigest()
    except FileNotFoundError:
        return None

# Script injected into index.html for live-reload polling
RELOAD_SCRIPT = b'''
<script>
(function(){
  var lastHash = null;
  setInterval(function() {
    fetch('/__dev/hash?t=' + Date.now())
      .then(function(r) { return r.text(); })
      .then(function(hash) {
        if (lastHash && hash !== lastHash) {
          console.log('[dev] index.html changed, reloading...');
          location.reload();
        }
        lastHash = hash;
      })
      .catch(function() {});
  }, 500);
})();
</script>
</body>
'''

class DevHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/__dev/hash":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            h = get_file_hash()
            self.wfile.write((h or "none").encode())
            return

        if path in ("/", "/index.html"):
            try:
                with open(INDEX, "rb") as f:
                    content = f.read()
                if b"</body>" in content:
                    content = content.replace(b"</body>", RELOAD_SCRIPT)
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            except FileNotFoundError:
                self.send_error(404)
            return

        super().do_GET()

    def log_message(self, format, *args):
        pass  # suppress noisy logs

def get_lan_ip():
    vpn_prefixes = (
        "proton",
        "pvpn",
        "tun",
        "tap",
        "wg",
        "tailscale",
        "zt",
        "docker",
        "br-",
        "veth",
        "virbr",
    )

    try:
        result = subprocess.run(
            ["ip", "-o", "-4", "addr", "show", "scope", "global"],
            capture_output=True,
            text=True,
            check=False,
        )
        candidates = []
        for line in result.stdout.splitlines():
            parts = line.split()
            if len(parts) < 4:
                continue
            iface = parts[1]
            addr = parts[3].split("/", 1)[0]
            try:
                parsed = ipaddress.ip_address(addr)
            except ValueError:
                continue
            candidates.append((iface, parsed))

        for iface, parsed in candidates:
            if parsed.is_private and not iface.startswith(vpn_prefixes):
                return str(parsed)
        for iface, parsed in candidates:
            if not iface.startswith(vpn_prefixes):
                return str(parsed)
    except FileNotFoundError:
        pass

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def get_listener_pids(port):
    """Return listening PIDs for a TCP port using lsof when available."""
    try:
        result = subprocess.run(
            ["lsof", "-tiTCP:%d" % port, "-sTCP:LISTEN"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return []

    pids = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.isdigit():
            pids.append(int(line))
    return pids

def reclaim_port_if_possible(port):
    """Stop same-user listeners on the requested port so the dev server can reuse it."""
    my_uid = os.getuid()
    reclaimed = []
    for pid in get_listener_pids(port):
        if pid == os.getpid():
            continue
        try:
            if os.stat(f"/proc/{pid}").st_uid != my_uid:
                continue
        except FileNotFoundError:
            continue

        try:
            os.kill(pid, 15)
            reclaimed.append(pid)
        except ProcessLookupError:
            continue
        except PermissionError:
            continue

    if not reclaimed:
        return []

    deadline = time.time() + 2.0
    while time.time() < deadline:
        remaining = [pid for pid in reclaimed if os.path.exists(f"/proc/{pid}")]
        if not remaining:
            break
        time.sleep(0.05)

    for pid in reclaimed:
        if os.path.exists(f"/proc/{pid}"):
            try:
                os.kill(pid, 9)
            except ProcessLookupError:
                pass
            except PermissionError:
                pass

    return reclaimed

def create_server(start_port, attempts=20):
    """Bind the requested port, reclaiming it if possible; otherwise fall forward."""
    reclaimed = []
    for offset, port in enumerate(range(start_port, start_port + attempts)):
        try:
            server = http.server.HTTPServer(("0.0.0.0", port), DevHandler)
            return server, port, reclaimed
        except OSError as exc:
            if getattr(exc, "errno", None) != 98:
                raise
            if offset == 0:
                reclaimed = reclaim_port_if_possible(port)
                if reclaimed:
                    server = http.server.HTTPServer(("0.0.0.0", port), DevHandler)
                    return server, port, reclaimed
    raise OSError(f"No free port found in range {start_port}-{start_port + attempts - 1}")

def main():
    global _last_hash
    _last_hash = get_file_hash()
    lan_ip = get_lan_ip()

    server, actual_port, reclaimed_pids = create_server(PORT)

    print()
    print("=" * 56)
    print("  ⚔️  Freedom Fighters Dev Server")
    print("=" * 56)
    print()
    print(f"  File:  index.html ({os.path.getsize(INDEX):,} bytes)")
    if reclaimed_pids:
        print()
        print(f"  Reclaimed port {PORT} by stopping PID(s): {', '.join(str(pid) for pid in reclaimed_pids)}")
    elif actual_port != PORT:
        print()
        print(f"  Port {PORT} was busy, using {actual_port} instead.")
    print()
    print("  📱 Open in browser (any device on your network):")
    print(f"    Local:  http://localhost:{actual_port}")
    print(f"    LAN:    http://{lan_ip}:{actual_port}")
    print()
    print("  🔄 Live-reload: Edit + save index.html → browsers auto-refresh")
    print("  Press Ctrl+C to stop")
    print("=" * 56)
    print()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Stopped.")
        server.server_close()

if __name__ == "__main__":
    main()
