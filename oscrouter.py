from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

import argparse

import yaml

parser = argparse.ArgumentParser()
parser.add_argument("--config", default="config.yaml", help="Config file")
args = parser.parse_args()

config = yaml.load(open(args.config, "r"))

# print(config)
clients = {}
for client in config["clients"]:
    print(f"- add client <{client['name']}> on {client['host']}:{client['port']}")
    clients[client['name']] = udp_client.SimpleUDPClient(client['host'], client['port'])
print()

def create_handler(route_clients):
    def handler(addr, args):
        for client in route_clients:
            client.send_message(addr, args)
    return handler

dispatcher = dispatcher.Dispatcher()
# dispatcher.set_default_handler(print)

for route in config["routes"].keys():
    route_clients = config["routes"][route]
    print(f"+ add {route_clients} to route {route}")
    dispatcher.map(route, create_handler(route_clients))
print()

server = osc_server.ThreadingOSCUDPServer(
    (config["server"]["host"], config["server"]["port"]),
    dispatcher
)
print(f"Serving on {server.server_address}")
server.serve_forever()
