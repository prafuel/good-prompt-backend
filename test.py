import requests
import json

url = "http://127.0.0.1:8000/refine"

prompt1 = ""
prompt2 = ""

data = {
		"data" : {
			"input" : "what is machine learning",
			"type" : "point",
			"format" : "``` 1. <point no 1> 2. <point no 2> 3. <point no 3>...```",
			"from_this" : prompt1,
			"to_this" : prompt2,
		}
	}

res = requests.post(url, json=data)

print(res.json())
