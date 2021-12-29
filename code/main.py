import json
from urllib import request
from pprint import pprint
from pprint import pp

response = request.urlopen("https://jsonplaceholder.typicode.com/users")

json_response = response.read()
users = json.loads(json_response)

pprint(users)

pp(users)
