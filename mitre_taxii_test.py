from taxii2client.v20 import Server
from taxii2client.v20 import Collection
import json
server = Server("https://cti-taxii.mitre.org/taxii/")
api_root = server.api_roots[0]
collection = api_root.collections[0]
print(json.dumps(collection.get_objects()))