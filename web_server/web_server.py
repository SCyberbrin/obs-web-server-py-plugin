
from os import path
from rocket3 import Rocket3
from threading import Thread
from bottle import Bottle, static_file


class serverClass(Thread):

    def __init__(self, publicPath: str, port: int=8080) -> None:
        Thread.__init__(self)
        self.app = Bottle()
        self.port = port
        self.publicPath = publicPath

        self._rocket = Rocket3(('127.0.0.1', port), 
                                'wsgi', {'wsgi_app': self.app})

    def run(self):
        
        @self.app.route('/')
        def index():
            return static_file("index.html", root=self.publicPath)

        @self.app.route('/<path:path>')
        def files(path):
            return static_file(path, root=self.publicPath)

        self._rocket.start()
    
    def stop_server(self):
        self._rocket.stop()



if __name__=='__main__':
    global test
    curent_path = path.dirname(path.abspath(__file__))
    test = serverClass(path.join(curent_path, "..", "templates"))
    test.start()