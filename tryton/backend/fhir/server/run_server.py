# Script to run server; pass port option to change listening port
# Place one level outside of directory server/
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from server import create_app
from server.config import ProductionConfig

define("port", default=5000, help="Port to listen on", type=int)
#app = create_app(config=ProductionConfig)
app = create_app() #DebugConfig
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(options.port)
IOLoop.instance().start()
