book = {}
book['tom'] = {
  'name': 'tom',
  'address': '1 red street, NY',
  'phone': 989898,
}

book['bob'] = {
  'name': 'bob',
   'address': '1 blue street, NY',
  'phone': 121212,
}

import json
s = json.dumps(book)

print(s)

# with open("")