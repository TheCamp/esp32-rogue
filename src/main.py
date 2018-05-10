import network
import time

from ws_connection import ClientClosedError
from ws_server import WebSocketServer, WebSocketClient

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('THECAMP', '')

class TestClient(WebSocketClient):
    def __init__(self, conn, clients, usernames):
        self.clients = clients
        self.usernames = usernames
        super().__init__(conn)

    def process(self):
        try:
            msg = self.connection.read()
            if not msg:
                return
            msg = msg.decode("utf-8")
            #authenticate with AUTH:USERNAME:<username> still missing password auth and handling of reconnections
            if msg.startswith('AUTH:'):
                auth_commands = msg.split(":")
                if auth_commands[1] == "USERNAME":
                    if auth_commands[2] in self.usernames:
                        self.connection.write("AUTH:USERNAME:ERROR:TAKEN")
                    else:
                        self.connection.write("AUTH:USERNAME:OK:" + auth_commands[2])
                        self.usernames.append(auth_commands[2])
                else:
                    self.connection.write("AUTH:INCORRECT")
            else:
                for client in self.clients:
                    client.connection.write(msg)
        except ClientClosedError:
            self.connection.close()


class TestServer(WebSocketServer):
    def __init__(self):
        super().__init__("test.html", 10)

    def _make_client(self, conn):
        return TestClient(conn,self._clients,self._usernames)

while not sta_if.isconnected():
    time.sleep(5)

server = TestServer()
server.start()
try:
    while True:
        server.process_all()
except KeyboardInterrupt:
    pass
server.stop()
