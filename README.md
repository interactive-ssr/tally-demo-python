# ISSR - Python Tally Demo 

Interactive SSR (ISSR) is a WebSocket-based framework that allows you to write a declarative HTTP server in any language and have the client sync state automatically. See the [main readme](https://github.com/interactive-ssr/issr-server/blob/master/main.org) for more information.

This is the example project for how to use ISSR with the [Flask](https://flask.palletsprojects.com/en/2.1.x/) web develpment framework.

## Quickstart

```sh
# Clone the repository
$ git clone git@github.com:interactive-ssr/tally-demo-python.git

# Change into tally-demo-python directory
$ cd tally-demo-python
# Create a Python VENV
$ python3 -m venv .venv
# Activate the environment
$ source .venv/bin/activate
# Install Pip requirements(Flask)
$ pip install -r requirements.txt

# Start the Flask server. This server will only be accessed internally by the ISSR server.
$ flask run

# In another terminal, start the ISSR server. This is the public-facing server that uses WebSockets to synchronize state.
$ docker pull charje/issr-server
$ cd tally-demo-python
$ docker-compose up 

# You should now be able to access the public-facing server at 127.0.0.1:3000 
```
