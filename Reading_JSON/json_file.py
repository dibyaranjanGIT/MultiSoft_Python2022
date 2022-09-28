import json
import requests

# data = json.load(open("data.json"))
request = requests.get("https://data.nasdaq.com/api/v3/datasets/FRED/NROUST.json?api_key=WN2sWS9jZNXxb_wjfxFx")
request_text = request.text

data = json.loads(request_text)
print(data)

json.dump(data, open("new_data.json", "w"), indent=4)