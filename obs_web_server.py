from web_server.web_server import serverClass

from os import path

import obspython as obs

def script_description():
    return """A python script for obs to create multiple HTTP server for localhost.
    Also, to know is that the script could make your obs slow at start up and at closing."""


def script_load(settings):
    print("script load!!")
    index_path = obs.obs_data_get_string(settings, "_html_index")
    port = obs.obs_data_get_int(settings, "_port")

    global test
    curent_path = path.dirname(path.abspath(__file__))
    test = serverClass(path.join(curent_path, "templates"))
    test.setDaemon(True)
    test.start()


def script_unload():
    print("script unload!!")
    test.stop_server()
    


def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_int(props, "_port", "port:", 1000, 100000, 1) # Setting the ports
    obs.obs_properties_add_text(props, "_html_index", "HTML folder path:", obs.OBS_TEXT_DEFAULT) # Setting the path of the HTML file


    return props

if __name__=='__main__':
    global test
    curent_path = path.dirname(path.abspath(__file__))
    test = serverClass(path.join(curent_path, "templates"))
    test.start()
