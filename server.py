import argparse
import subprocess
import os
import urllib.request
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from media.VAST.rsg_options import iZACgmeQ, ewmPj998
from media.VAST.multiview_options import vast_multiple_mv
from media.VAST.vast_options import vast_simple, vast_custom, vast_multiple, vast_stream2_custom, vast_stream1_custom, vast_stream3_custom, vast_error, AA_OK_SMS_FIRST_V1

PORT = 8082
MEDIA_FILE = "./media/ad_one.mp4"
MEDIA_FILES = {
    "/media.mp4": MEDIA_FILE,
    "/ad_one.mp4": "./media/ad_one.mp4",
    "/ad_two.mp4": "./media/ad_two.mp4",
    "/640x360_1.mp4":"./media/640x360_1.mp4",
    "/640x360_2.mp4":"./media/640x360_2.mp4",
    "/640x360_3.mp4":"./media/640x360_3.mp4"
}


def my_ip(iface="en0"):
    try:
        ip = subprocess.check_output(
            ["ipconfig", "getifaddr", iface], text=True
        ).strip()
        if ip:
            return ip
    except subprocess.CalledProcessError, FileNotFoundError:
        pass
    # Cross-platform fallback: ask the OS which local address it would use to
    # reach the internet (no packets are actually sent).
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def ensure_media_file(url=None):
    if os.path.exists(MEDIA_FILE):
        print(
            f"Using existing media: {MEDIA_FILE} ({os.path.getsize(MEDIA_FILE)} bytes)"
        )
        return
    if not url:
        print(f"WARNING: '{MEDIA_FILE}' not found and no --media-url given.")
        print("Drop an .mp4 there, or pass --media-url <direct-mp4-url>.")
        return
    print(f"Downloading media from {url} ...")
    try:
        os.makedirs(os.path.dirname(MEDIA_FILE) or ".", exist_ok=True)
        urllib.request.urlretrieve(url, MEDIA_FILE)
        print(f"Saved {MEDIA_FILE} ({os.path.getsize(MEDIA_FILE)} bytes)")
    except Exception as e:
        print(f"Download failed: {e}")


IP = my_ip()


VASTS = {"simple": vast_simple, "custom": vast_custom, "multiple": vast_multiple, "multiview": vast_multiple_mv, "stream2": vast_stream2_custom, "stream1": vast_stream1_custom, "stream3": vast_stream3_custom, "error": vast_error, "aa_ok_sms_first_v1": AA_OK_SMS_FIRST_V1, "rsg_options": iZACgmeQ, "ewmPj998": ewmPj998}


class My_Server(BaseHTTPRequestHandler):
    default_vast = "simple"  # set from CLI in __main__

    def _server_media(self, filepath):
        try:
            size = os.path.getsize(filepath)
        except OSError:
            self.send_response(404, "Media file not found")
            self.end_headers()
            return

        start, end, status = 0, size - 1, 200
        range_header = self.headers.get("Range")
        if range_header and range_header.startswith("bytes="):
            try:
                range_spec = range_header.split("=", 1)[1]
                if "," not in range_spec:
                    range_start, range_end = range_spec.split("-", 1)
                    if not range_start:
                        suffix_length = int(range_end)
                        if suffix_length <= 0 or size == 0:
                            start = size
                        else:
                            start = max(size - suffix_length, 0)
                        end = size - 1
                    else:
                        start = int(range_start)
                        end = int(range_end) if range_end else size - 1
                    if start >= size or end < start:
                        self.send_response(416, "Requested Range Not Satisfiable")
                        self.send_header("Content-Range", f"bytes */{size}")
                        self.end_headers()
                        return
                    end = min(end, size - 1)
                    status = 206
            except ValueError:
                start, end, status = 0, size - 1, 200

        length = end - start + 1
        self.send_response(status)
        self.send_header("Content-Type", "video/mp4")
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(length))
        if status == 206:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.end_headers()

        if self.command == "HEAD":
            return

        with open(filepath, "rb") as f:
            f.seek(start)
            remaining, chunk = length, 64 * 1024
            while remaining > 0:
                data = f.read(min(chunk, remaining))
                if not data:
                    break
                try:
                    self.wfile.write(data)
                except BrokenPipeError, ConnectionResetError:
                    break  # player closed the connection (normal on seek/skip)
                remaining -= len(data)

    def _handle(self):
        parsed = urlparse(self.path)
        path, qs = parsed.path, parse_qs(parsed.query)
        # Watermark check (works for any request)
        wm = self.headers.get("X-Roku-Ad-Watermark")

        # 1) Media file request: serve the video (with Range support) and return.
        filepath = MEDIA_FILES.get(path)
        if filepath:
            print(f"\n=== MEDIA {self.command} {self.path} ===")
            print(f"Range: {self.headers.get('Range', '(none)')}")
            print(f"X-Roku-Ad-Watermark: {'PRESENT' if wm else 'ABSENT'}")
            if wm:
                print(f"jwt: {wm}\n(decode at jwt.io)")
            self._server_media(filepath)
            return

        # 2) Ad request vs beacon/impression pixel.
        # A beacon is identified by its query string (e.g. /?start), so a
        # request only counts as an ad request when it has NO query.
        route = path.lstrip("/")
        kind = None
        if not parsed.query:
            if route in VASTS:  # e.g. GET /custom
                kind = route
            elif path in ("/", "/vast", "/ad"):  # default ad
                kind = self.default_vast
            else:
                self.send_error(404, "Not Found")
                return
        is_ad_request = kind is not None

        label = parsed.query or route or "(none)"
        tag = "AD-REQUEST" if is_ad_request else "BEACON"
        print(f"\n=== {tag} {self.command} {self.path} ===")
        print(f"label: {label}")
        print(f"X-Roku-Ad-Watermark: {'PRESENT' if wm else 'ABSENT'}")
        if wm:
            print(f"jwt: {wm}\n(decode at jwt.io)")

        if kind is not None:
            body = VASTS[kind](IP, PORT).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/xml")
        else:
            body = b""  # beacons/impressions: empty 200 pixel
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    do_GET = _handle
    do_POST = _handle
    do_HEAD = _handle

    def log_message(self, *a):  # silence default noisy logging
        pass


if __name__ == "__main__":
    try:
        ap = argparse.ArgumentParser()
        ap.add_argument(
            "--vast",
            choices=VASTS,
            default="simple",
            help=f"default VAST served at '/'. Options: {list(VASTS.keys())}",
        )
        ap.add_argument(
            "--host",
            default="0.0.0.0",
            help="interface to bind (default: all interfaces)",
        )
        ap.add_argument(
            "--media-file",
            default=MEDIA_FILE,
            help="path to the local .mp4 served at /media.mp4",
        )
        ap.add_argument(
            "--media-url",
            default=None,
            help="direct .mp4 URL to download once if --media-file is missing",
        )
        args = ap.parse_args()

        My_Server.default_vast = args.vast
        MEDIA_FILE = args.media_file
        MEDIA_FILES["/media.mp4"] = MEDIA_FILE
        ensure_media_file(args.media_url)
        if args.host != "0.0.0.0":
            IP = args.host

        print(f"Serving on http://{IP}:{PORT}/ (bound to {args.host}; default VAST: {args.vast}) (ctrl-C to stop)")
        print(f"  ad-request URL for raf.force.ad_url:  http://{IP}:{PORT}/")
        print(f"  force a specific VAST:                http://{IP}:{PORT}/custom")
        print(f"  force multiple VAST:                  http://{IP}:{PORT}/multiple")
        print(f"  force stream3 VAST:                   http://{IP}:{PORT}/stream3")
        print(f"  force stream2 VAST:                   http://{IP}:{PORT}/stream2")
        print(f"  force stream1 VAST:                   http://{IP}:{PORT}/stream1")
        print(f"  force error VAST:                     http://{IP}:{PORT}/error")
        print(f"  force AA_OK_SMS_FIRST_V1 VAST:        http://{IP}:{PORT}/aa_ok_sms_first_v1")
        print(f"  force rsg_options VAST:               http://{IP}:{PORT}/rsg_options")
        print(f"  force ewmPj998 VAST:                  http://{IP}:{PORT}/ewmPj998")
        print(f"  force multiview VAST:                 http://{IP}:{PORT}/multiview")
        # print(f"  media file served at:                 http://{IP}:{PORT}/media.mp4")
        ThreadingHTTPServer((args.host, PORT), My_Server).serve_forever()
    except KeyboardInterrupt:
        print("\nShutting server down.")
        exit(0)
