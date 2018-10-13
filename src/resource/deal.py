from flask import jsonify, request
import requests
import json
from .client import Client
from flask_restful import Resource
from .testApi import Analysis


api_token="137f09ef7c288dedc165c51bce0a0cffe571e1d5"
domain_url="https://api.pipedrive.com/"
client = Client(api_base_url=domain_url)
client.set_token(api_token)

class DealListAPI(Resource):
    def get(self):
        get_deals=client.get_deals()
        deals= Analysis.wonDeal(get_deals)
        return deals

class DealApiQuery(Resource):
    #query param
    def get(self):
        print("rest")
        args = request.args
        print (args) # For debugging
        id = args['id']
        get_specific_deal = client.get_deals(deal_id=id)
        return get_specific_deal

    def post(self):
        args=request.args
        id=args['id']
        status=args['status'] 
        update_deal = client.update_deal(deal_id=id, dealstatus = status)
  

    
    # def post

    # def put
    # def delete
    
  
    #pathparam
class DealApiParam(Resource):
    def get(self, my_id):
        print("inside!")
        get_spe_deal=client.get_deals(deal_id=my_id)
        return get_spe_deal


# class WonApi(Resource):
#     def get(self):
#         get_specific_deal = client.get_deals_by_status(status="won")
#         return get_specific_deal

    

    
    

    
