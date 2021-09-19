# Third-Party modules
from werkzeug.serving import make_server
import flask

import time
import threading

import obspython as obs

last_thread = False


class ServerThread(threading.Thread):
    def __init__(self, app, PORT):
        threading.Thread.__init__(self)
        self.srv = make_server('127.0.0.1', PORT, app)
        self.ctx = app.app_context()
        self.ctx.push()
        self.port = PORT
    def run(self):
        print('starting server at PORT ' + str(self.port))
        self.srv.serve_forever()
    def shutdown(self):
        self.srv.shutdown()


def start_server(PORT: int, index_path: str):
    global last_thread, server
    if last_thread:
        stop_server()

    app = flask.Flask(__name__, static_folder='templates', template_folder='templates')
    server = ServerThread(app, PORT)
    server.start()
    last_thread = True

    @app.route('/')
    def index():
        return flask.render_template(index_path) #html file needs to be inside a templates folder


def stop_server():
    global server
    server.shutdown()
    last_thread = False
    time.sleep(1) # Wait for the server to shutdown


def script_description():
    return "A python script for obs to create multiple HTTP server for localhost.\nAlso, to know is that the script could make your obs slow at start up and at closing."



def script_load(settings):
    index_path = obs.obs_data_get_string(settings, "_html_index")
    port = obs.obs_data_get_int(settings, "_port")
    start_server(port, index_path)


def script_unload():
    stop_server()


def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_int(props, "_port", "port:", 1000, 100000, 1) # Setting the ports
    obs.obs_properties_add_text(props, "_html_index", "HTML file path:", obs.OBS_TEXT_DEFAULT) # Setting the path of the HTML file


    return props