import json
from urllib import request
from pprint import pprint
from pprint import pp
from pprint import PrettyPrinter
from pprint import pformat


response = request.urlopen("https://jsonplaceholder.typicode.com/users")

json_response = response.read()
users = json.loads(json_response)

pprint(users)

pp(users)

pprint(users, depth=1)

pprint(users, depth=2)

pprint(users[0], depth=1)

pprint(users[0], depth=1, indent=4)

pprint(users[0], depth=2, indent=4)

pprint(users[0])

pprint(users[0], width=160)

pprint(users[0], width=500)

pprint(users, depth=1)

pprint(users, depth=1, width=40)

pprint(users, depth=1, width=40, compact=True)

# OBS.: Para funcionar, você precisa de 1 arquivo formato .txt
with open("output.txt", mode="w") as file_object:
    pprint(users, stream=file_object)

pprint(users[0], depth=1)

pprint(users[0], depth=1, sort_dicts=False)

number_list = [123456789, 10000000000000]

pprint(number_list, underscore_numbers=True)

custom_printer = PrettyPrinter(
    indent=4,
    width=100,
    depth=2,
    compact=True,
    sort_dicts=False,
    underscore_numbers=True
)

custom_printer.pprint(users[0])

number_list = [123456789, 10000000000000]

custom_printer.pprint(number_list)

address = pformat(users[0]["address"])
chars_to_remove = ["{", "}", "'"]

for char in chars_to_remove:
    address = address.replace(char, "")

print(address)

A = {}
B = {"link": A}
A["link"] = B

print(A)
pprint(A)
