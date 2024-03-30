import http.server
import subprocess

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()
        output = "<xmp>"
        if self.path == "/":
            output += subprocess.run('sensors', stdout=subprocess.PIPE).stdout.decode('utf-8') + "</xmp>"
        self.wfile.write(bytes(output,encoding="utf-8"))



if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 8080
    server = http.server.HTTPServer((ip, port), MyHandler)
    server.serve_forever()
