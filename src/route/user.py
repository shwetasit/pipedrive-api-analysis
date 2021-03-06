from flask import Blueprint
from flask_restful import Api

deal_blueprint = Blueprint('user', __name__)
deal_blueprint_api = Api(deal_blueprint)

from resource.deal import DealListAPI, DealApiParam, DealApiQuery, TopDeals

deal_blueprint_api.add_resource(DealListAPI, '/deals')
deal_blueprint_api.add_resource(TopDeals, '/deals/top')
deal_blueprint_api.add_resource(DealApiParam, '/dealsbysid/<string:my_id>') #http://127.0.0.1:5000/dealsbyid/19
deal_blueprint_api.add_resource(DealApiQuery, '/dealsbyid')#http://127.0.0.1:5000/dealsbyid?id=19
#deal_blueprint_api.add_resource(DealApiQuery, '/deals/find/status')

# deal_blueprint_api.add_resource(WonApi, '/deals/<string:status>')

