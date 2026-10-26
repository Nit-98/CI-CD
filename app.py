from http.server import HTTPServer, BaseHTTPRequestHandler

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")

HTTPServer(("0.0.0.0", 8000), App).serve_forever()

