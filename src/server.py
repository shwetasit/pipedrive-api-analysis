from flask import Flask
import config

server = Flask(__name__)
server.debug= config.DEBUG

from route.user import deal_blueprint
server.register_blueprint(deal_blueprint)

server.run(host= config.HOST, port=config.PORT)
