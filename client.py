from taxii2client.v21 import Server
from taxii2client.v21 import Collection
import json
server = Server('http://localhost:5000/taxii2', user='admin', password='Password0')
print(server.api_roots[0].title)
	
print("------------- \n")

api_root = server.api_roots[0]
collection = api_root.collections[0]
print(collection.id)
print(json.dumps(collection.get_objects()))
