# Third-Party modules
from werkzeug.serving import make_server
import flask

import time
import threading

last_thread = False

class ServerThread(threading.Thread):
    def __init__(self, app, PORT):
        threading.Thread.__init__(self)
        self.srv = make_server('127.0.0.1', PORT, app)
        self.ctx = app.app_context()
        self.ctx.push()
    def run(self):
        print('starting server')
        self.srv.serve_forever()
    def shutdown(self):
        self.srv.shutdown()


def start_server(PORT):
    global server
    app = flask.Flask(__name__)
    server = ServerThread(app, PORT)
    server.start()

    @app.route('/')
    def index():
        return flask.render_template('index.html') #html file needs to be inside a templates folder


def stop_server():
    global server
    server.shutdown()


# http_server_instance(9000, "/html/index.html")
def script_description():
    return "A python plugin for obs to create multibel http server for localhost."


def script_update(settings):
    global last_thread
    if last_thread:
        stop_server()
        time.sleep(3)
        
    start_server(9000)
    last_thread = True




# class Data:
#     _text_ = None
#     _int_ = None
#     _settings_ = None


# def save(prop, props):
#     if not Data._settings_:
#         return
#     p = Path(__file__).absolute()  # current script path
#     file = p.parent / "saved_settings.json"
#     try:
#         content = obs.obs_data_get_json(Data._settings_)
#         with open(file, "w") as f:
#             f.write(content)
#     except Exception as e:
#         print(e, "cannot write to file")


# def script_properties():
#     props = obs.obs_properties_create()

#     return props


# def script_update(settings):
#     print("loading shit")
#     Data._text_ = obs.obs_data_get_string(settings, "_text")
#     Data._int_ = obs.obs_data_get_int(settings, "_int")
#     Data._settings_ = settings


if __name__ == "__main__":
    script_update(0)