import json
from api.src.basecontroller import Controller

PERSONAL_DATA =  [
    {"id":1, "name":"John"},
    {"id":2, "name":"Ronald"},
    {"id":3, "name":"Francis"},
    {"id":4, "name":"Alfredo"}
]

class BICollection(Controller):
    def on_get(self, req, resp, **kwargs):
        results = PERSONAL_DATA
        resp.body = json.dumps(results)


class BIResource(Controller):
    def on_get(self, req, resp, **kwargs):
        result = { "id": kwargs['id']}
        resp.body = json.dumps(result)