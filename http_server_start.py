import http.server
import socketserver


import threading
import time

import obspython as obs
from pathlib import Path


def http_server_instance(PORT, PATH):
    Handler = http.server.SimpleHTTPRequestHandler

    class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.path = PATH
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

    # Create an object of the above class
    handler_object = MyHttpRequestHandler

    my_server = socketserver.TCPServer(("", PORT), handler_object)

    # Star the server
    print("Serving At Localhost PORT", PORT)
    my_server.serve_forever()


# http_server_instance(9000, "/html/index.html")
def script_description():
    return "A python plugin for obs to create multibel http server for localhost."


def script_update(settings):
    for thread in threading.enumerate(): 
        print(thread)
        if thread.name == "Thread-1":
            pass
    # t = threading.currentThread()
    # if t:
    #     t.do_run = False
    # print(t, "already existing")
    t = threading.Thread(target=http_server_instance, args=(9000, "/html/index.html",))
    print(t, "prepeard")
    t.start()
    print(t, "start")

    # if all_processes == []:
    #     for process in all_processes:
    #         process.terminate()
    # process = multiprocessing.Process(target=http_server_instance, args=(9000, "/html/index.html",))
    # process.start()
    # all_processes.append(process)
    # time.sleep(10)
    # print(all_processes, "now")
    # for process in all_processes:
    #     process.terminate()
    # print(all_processes)




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