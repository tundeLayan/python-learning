book = {}
book['tom'] = {
  'name': 'tom',
  'address': '1 red street, NY',
  'phone': 989898
}

import json
import os

s = json.dumps(book)

with open(os.path.expanduser("~/Desktop/testing_python.txt"), "w") as f:
  f.write(s) 