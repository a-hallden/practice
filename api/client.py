import requests
from django.conf import settings


class APIResponse(object):
    def __init__(self, data, success, status_code):
        super(APIResponse, self).__init__()
        self.data = data
        self.success = success
        self.status_code = status_code

    def __repr__(self):
        return "success: {}, status code: {}, data: {}".format(
            self.success, self.status_code, self.data
        )


class Client(object):
    def __init__(self):
        self.HOSTNAME = settings.OMDB_HOST_NAME
        self.API_KEY = settings.OMDB_API_KEY

    def do_get(self, params):
        url = self.HOSTNAME
        params["apikey"] = self.API_KEY
        response = requests.get(url, params=params)
        return response.json()

    def search(self, params):
        return self.do_get(params)
