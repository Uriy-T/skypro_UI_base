from http.server import BaseHTTPRequestHandler, HTTPServer
from config import CONTACTS_PAGE

host_name = 'localhost'
server_port = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Простой учебный сервер для локального запуска.
    """

    def do_GET(self):
        self.send_response(200, "Success")
        self.send_header("Content-type","text/html")
        self.end_headers()
        with open(CONTACTS_PAGE, 'r', encoding='utf-8') as file:
            contact_page = file.read()

        self.wfile.write(contact_page.encode('utf-8'))


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body.decode('utf-8'))
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), MyServer)
    print("Server started on: //%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()

    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped")