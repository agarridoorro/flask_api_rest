import json
from json import JSONEncoder

class GenericEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__

    def toJson(self, o):
        return json.dumps(o, indent=4, cls=GenericEncoder)