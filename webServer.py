from http.server import HTTPServer, BaseHTTPRequestHandler
from ssl import wrap_socket

host = "127.0.0.1"
port = 8080
html_loc = "/home/ubuntu/basicPythonWebServer/src/"


def sendFile(fileName, server):
    with open(fileName, "r") as file:
        for line in file:
            server.wfile.write(bytes(line, "utf-8"))


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
                
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        path = self.path
        path = path.split("/")

        """match path[1] :
            case "test1":
                sendFile(html_loc+"test1.html", self)
                pass

            case "test2":
                sendFile(html_loc+"test2.html", self)
                pass

            case "kill":
                print("Kill request received, shutting dowm")
                self.server.shutdown()
                pass

            case _:
                sendFile(html_loc+"index.html", self)"""

        if path[1] == "kill":
            print("Kill request received, shutting dowm")
            self.server.shutdown()
        elif path[1] == "test1":
            sendFile(html_loc+"test1.html", self)
        elif path[1] == "test2":
            sendFile(html_loc+"test2.html", self)
        else:
            sendFile(html_loc+"index.html", self)


if __name__ == "__main__":
    webServer = HTTPServer((host, port), MyServer)

    """webServer.socket = wrap_socket(webServer.socket,
                                   keyfile = "/home/ubuntu/private.key",
                                   certfile = "/home/ubuntu/cert.pem",
                                   server_side = True)"""

    try:
        print("Web server starting")
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
        

    webServer.server_close()
    print("Server stopped.")