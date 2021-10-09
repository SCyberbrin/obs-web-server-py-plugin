# Third-Party modules
from bottle import Bottle, ServerAdapter, static_file


import os
import time
import threading

import obspython as obs

server = None

class MyWSGIRefServer(ServerAdapter):
    server = None

    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        server = make_server(self.host, self.port, handler, **self.options)
        print("server running")
        server.serve_forever()

    def stop(self):
        self.server.server_close()

class ServerThread(threading.Thread):
    def __init__(self, PORT, PATH):
        threading.Thread.__init__(self)
        self.server = MyWSGIRefServer(port=PORT)
        self.path = PATH
    def run(self):
        app = Bottle()
        
        @app.route('/')
        def index():
            return static_file("index.html", root=self.path)

        @app.route('/<path:path>')
        def files(path):
            return static_file(path, root=self.path)


        app.run(server=self.server)
    
    def shutdown(self):
        self.server.stop()
        print("server stoping")



def start_server(PORT: int, index_path: str):
    global server
    if server != None:
        server.shutdown()

    server = ServerThread(PORT, index_path)
    print("server is getting starded!!")
    server.start()
    print("server is starded!!")


def stop_server():
    global server
    print("server is getting closed!!")
    server.shutdown()
    server = None
    print("server is closed!!")
    # time.sleep(1) # Wait for the server to shutdown


def script_description():
    return "A python script for obs to create multiple HTTP server for localhost.\nAlso, to know is that the script could make your obs slow at start up and at closing."



def script_load(settings):
    print("script load!!")
    index_path = obs.obs_data_get_string(settings, "_html_index")
    port = obs.obs_data_get_int(settings, "_port")
    start_server(port, index_path)


def script_unload():
    print("script unload!!")
    stop_server()



def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_int(props, "_port", "port:", 1000, 100000, 1) # Setting the ports
    obs.obs_properties_add_text(props, "_html_index", "HTML folder path:", obs.OBS_TEXT_DEFAULT) # Setting the path of the HTML file


    return props