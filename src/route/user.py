from flask import Blueprint
from flask_restful import Api

deal_blueprint = Blueprint('user', __name__)
deal_blueprint_api = Api(deal_blueprint)

from resource.deal import DealListAPI, DealApiParam, DealApiQuery

deal_blueprint_api.add_resource(DealListAPI, '/deals')
deal_blueprint_api.add_resource(DealApiParam, '/dealsbyid/<string:my_id>') #http://127.0.0.1:5000/dealsbyid/19
deal_blueprint_api.add_resource(DealApiQuery, '/dealsbyid')#http://127.0.0.1:5000/dealsbyid?id=19
deal_blueprint_api.add_resource(DealApiQuery, '/deals/update')

# deal_blueprint_api.add_resource(WonApi, '/deals/<string:status>')

