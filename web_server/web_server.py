
from concurrent.futures import thread
from threading import Thread
from bottle import Bottle, static_file

class serverClass(Thread):

    def __init__(self, publicPath: str, port: int=8080) -> None:
        Thread.__init__(self)
        self.app = Bottle()
        self.port = port
        self.publicPath = publicPath

    def run(self):
        
        @self.app.route('/')
        def index():
            return static_file("index.html", root=self.publicPath)

        @self.app.route('/<path:path>')
        def files(path):
            return static_file(path, root=self.publicPath)
        
        self.app.run(locals="localhost", port=self.port, quiet=False)


    def stop_server(self):
        self.app.close()
        thread._shutdown = True
