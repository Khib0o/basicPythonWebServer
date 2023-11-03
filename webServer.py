from http.server import HTTPServer, BaseHTTPRequestHandler
from ssl import wrap_socket

host = "127.0.0.1"
port = 8084

def sendFile(fileName, server):
    with open(fileName, "r") as file:
        for line in file:
            server.wfile.write(bytes(line, "utf-8"))


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        sendFile("index.html", self)

if __name__ == "__main__":
    webServer = HTTPServer((host, port), MyServer)

    webServer.socket = wrap_socket(webServer.socket,
                                   keyfile = "/home/ubuntu/private.key",
                                   certfile = "/home/ubuntu/cert.pem",
                                   server_side = True)

    try:
        print("Web server starting")
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")