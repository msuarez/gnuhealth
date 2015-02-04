# Script to run server; pass port option to change
# listening port
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from server import create_app
from server.config import ProductionConfig

define("port", default=5000, help="Port to listen on", type=int)
app = create_app(config=ProductionConfig)
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(options.port)
IOLoop.instance().start()
