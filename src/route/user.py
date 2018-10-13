from flask import Blueprint
from flask_restful import Api

deal_blueprint = Blueprint('user', __name__)
deal_blueprint_api = Api(deal_blueprint)

from resource.deal import DealListAPI, WonApi
from resource.deal import DealApi
deal_blueprint_api.add_resource(DealListAPI, '/deals')
deal_blueprint_api.add_resource(DealApi, '/dealsbyid/<string:my_id>')
# deal_blueprint_api.add_resource(WonApi, '/deals/<string:status>')

