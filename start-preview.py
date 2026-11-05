#!/usr/bin/env python3
"""Serve the travel planner on this computer only, with the correct HTML MIME type."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

if __name__ == '__main__':
    root = str(Path(__file__).resolve().parent)
    with ThreadingHTTPServer(('127.0.0.1', 8765), partial(PreviewHandler, directory=root)) as server:
        print('拾途预览：http://127.0.0.1:8765/ — 关闭终端或按 Ctrl+C 停止', flush=True)
        server.serve_forever()
