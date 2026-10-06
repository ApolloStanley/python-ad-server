import http.client
import tempfile
import threading
import unittest
import xml.etree.ElementTree as ET
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlparse

import server


class ServerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.media_path = Path(self.temp_dir.name, "sample.mp4")
        self.media_path.write_bytes(b"abcdefghij")
        self.routes = patch.dict(
            server.MEDIA_FILES,
            {
                "/media.mp4": str(self.media_path),
                "/test-media.mp4": str(self.media_path),
            },
        )
        self.routes.start()
        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), server.My_Server)
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self):
        self.httpd.shutdown()
        self.httpd.server_close()
        self.thread.join()
        self.routes.stop()
        self.temp_dir.cleanup()

    def request(self, path, headers=None):
        connection = http.client.HTTPConnection(*self.httpd.server_address)
        connection.request("GET", path, headers=headers or {})
        response = connection.getresponse()
        result = (
            response.status,
            {key.lower(): value for key, value in response.getheaders()},
            response.read(),
        )
        connection.close()
        return result

    def test_media_route_serves_configured_file(self):
        status, headers, body = self.request("/media.mp4")
        self.assertEqual(status, 200)
        self.assertEqual(headers["content-type"], "video/mp4")
        self.assertEqual(body, b"abcdefghij")

    def test_byte_ranges(self):
        cases = (
            ("bytes=2-4", 206, b"cde", "bytes 2-4/10"),
            ("bytes=8-", 206, b"ij", "bytes 8-9/10"),
            ("bytes=-4", 206, b"ghij", "bytes 6-9/10"),
            ("bytes=8-99", 206, b"ij", "bytes 8-9/10"),
            ("bytes=-99", 206, b"abcdefghij", "bytes 0-9/10"),
        )
        for range_header, expected_status, expected_body, expected_range in cases:
            with self.subTest(range_header=range_header):
                status, headers, body = self.request(
                    "/test-media.mp4", {"Range": range_header}
                )
                self.assertEqual(status, expected_status)
                self.assertEqual(body, expected_body)
                self.assertEqual(headers["content-range"], expected_range)

    def test_unsatisfiable_range_and_ignored_multi_range(self):
        status, headers, _ = self.request("/test-media.mp4", {"Range": "bytes=10-"})
        self.assertEqual(status, 416)
        self.assertEqual(headers["content-range"], "bytes */10")

        status, _, body = self.request("/test-media.mp4", {"Range": "bytes=0-1,3-4"})
        self.assertEqual(status, 200)
        self.assertEqual(body, b"abcdefghij")

    def test_ad_beacon_and_unknown_routes(self):
        status, headers, body = self.request("/custom")
        self.assertEqual(status, 200)
        self.assertEqual(headers["content-type"], "application/xml")
        self.assertEqual(ET.fromstring(body).tag, "VAST")

        self.assertEqual(self.request("/?start")[0], 200)
        self.assertEqual(self.request("/unknown")[0], 404)

    def test_vast_templates_are_valid_and_media_paths_are_served(self):
        for name, template in server.VASTS.items():
            with self.subTest(template=name):
                document = ET.fromstring(template("127.0.0.1", server.PORT))
                for media_file in document.findall(".//MediaFile"):
                    media_path = urlparse(media_file.text.strip()).path
                    self.assertIn(media_path, server.MEDIA_FILES)


if __name__ == "__main__":
    unittest.main()
