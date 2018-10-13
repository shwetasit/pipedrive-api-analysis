import requests
from urllib.parse import urlencode, urlparse, quote_plus
from base64 import b64encode


class Client:
    flow_base_url = "https://oauth.pipedrive.com/oauth/"
    oauth_end = "authorize?"
    token_end = "token"
    api_version = "v1/"
    header = {"Accept": "application/json, */*", "content-type": "application/json"}
    def __init__(self, api_base_url, client_id=None, client_secret=None, oauth=False):
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth = oauth
        self.api_base_url = api_base_url
        self.token = None
    def make_request(self, method, endpoint, data=None, json=None, **kwargs):
        # make the request based on the api allowed methods.
        if self.token:
            if self.oauth:
                self.header["Authorization"] = "Bearer " + self.token
                url = '{0}{1}{2}'.format(self.api_base_url, self.api_version, endpoint)
            else:
                url = '{0}{1}{2}?api_token={3}'.format(self.api_base_url, self.api_version, endpoint, self.token)
            if method == "get":
                response = requests.request(method, url, headers=self.header, params=kwargs)
            else:
                response = requests.request(method, url, headers=self.header, data=data, json=json)
            return self.parse_response(response)
        else:
            raise Exception("To make petitions the token is necessary")

    def _get(self, endpoint, data=None, **kwargs):
        return self.make_request('get', endpoint, data=data, **kwargs)

    def _post(self, endpoint, data=None, json=None, **kwargs):
        return self.make_request('post', endpoint, data=data, json=json, **kwargs)

    def _put(self, endpoint, json=None, **kwargs):
        return self.make_request('put', endpoint, json=json, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self.make_request('delete', endpoint, **kwargs)

    def parse_response(self, response):
        if response.status_code == 204 or response.status_code == 201:
            return True
        elif response.status_code == 400:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check your request body and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 401:
            raise Exception(
                "The URL {0} retrieved and {1} error. Please check your credentials, make sure you have permission to perform this action and try again.".format(
                    response.url, response.status_code))
        elif response.status_code == 403:
            raise Exception(
                "The URL {0} retrieved and {1} error. Please check your credentials, make sure you have permission to perform this action and try again.".format(
                    response.url, response.status_code))
        elif response.status_code == 404:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 410:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 422:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 429:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 500:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 501:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        return response.json()


    def set_token(self, token):
        if token:
            self.token = token
    
    def get_data(self, endpoint, **kwargs):
        if endpoint != "" :
            return self._get(endpoint, **kwargs)
    
    def get_specific_data(self, endpoint, data_id, **kwargs):
        if endpoint != "":
            url = "{0}/{1}".format(endpoint, data_id)
            return self._get(url, **kwargs)
    
    def create_data(self, endpoint, **kwargs):
        if endpoint != "" and kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post(endpoint, json=params)
         
    

    #Deals api

    def get_deals(self, deal_id=None, **kwargs):
        print("outside if!")
        if deal_id is not None:
            print("inside if!")
            url = "deals/{0}".format(deal_id)
        else:
            url = "deals"
        
        return self._get(url, **kwargs)
    
    def create_deal(self, **kwargs):
        url="deals"
        if kwargs is not None:
            params={}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_deal(self, deal_id, **kwargs):
        if deal_id is not None and kwargs is not None:
            url = "deals/{0}".format(deal_id)
            params={}
            params.update(kwargs)
            return self._put(url, json = params)
    
    def delete_deal(self, deal_id):
        if deal_id is not None:
            url = "deals/{0}".format(deal_id)
            return self._delete(url)

    def get_deals_by_name(self, **kwargs):
        if kwargs is not None:
            url = "deals/find"
            return self._get(url, **kwargs)

    def get_deals_by_status(self, **kwargs):
        if kwargs is not None:
            url = "deals/find/status"
            return self._get(url, **kwargs)
    
    def get_deal_participants(self, deal_id, **kwargs):
        if deal_id is not None:
            url = "deals/{0}/participants".format(deal_id)
            return self._get(url, **kwargs)


    

