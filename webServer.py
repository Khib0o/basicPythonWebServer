from http.server import HTTPServer, BaseHTTPRequestHandler

host = "172.31.53.237"
port = 8080

def sendFile(fileName, server):
    with open(fileName, "r") as file:
        for line in file:
            server.wfile.write(bytes(line, "utf-8"))


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        sendFile("index.html", self)

if __name__ == "__main__":
    webServer = HTTPServer((host, port), MyServer)

    try:
        print("Web server starting")
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")