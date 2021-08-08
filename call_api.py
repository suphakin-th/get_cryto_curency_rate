import json
import requests

api_key = 'Your api key'
url = 'https://api.livecoinwatch.com/coins/single'

code = ['ETH', 'SLP', 'AXS']
data_lean = ['name', 'rate']
data_dict = {}

headers = {
    'x-api-key': api_key,
    'Content-Type': 'application/json'
}
for _c in code:
    payload = json.dumps({
        "currency": "THB",
        "code": _c,
        "meta": True
    })
    data = (requests.request('POST', url, headers=headers, data=payload)).json()
    data_dict.update({
        _c: {
            'name': data.get('name', _c),
            'rate': data.get('rate', 0)
        }
    })

print(data_dict)
