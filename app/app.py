from http.server import HTTPServer, BaseHTTPRequestHandler

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self): 
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write((str(self.headers.get('X-Forwarded-For')) + ', ' + self.client_address[0] + '\n').encode("utf-8"))

server_hostname = ""
server_port = 8080


httpd = HTTPServer((server_hostname, server_port), AppHandler)
httpd.serve_forever()