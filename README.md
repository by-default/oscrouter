# OSC router is simple daemon routnig OSC messages.

usage:

`python3 oscrouter.py --config <config path>`

## Config format:

* `server` section: specify port and host on which router listen to incoming messages
* `clients` section: list of OSC clinets to which messages need to be sent (name, port and host)
* `routes`: list of routes. Specify OSC message path and list of clients (refer to names from `clients` section). You can use wildcards (`*` and `?`) in route path.

See config example.
