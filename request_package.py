import requests
import json
ingredients=""
responce=requests.get("https://api.sampleapis.com/coffee/hot")
responce=responce.json()
# responce=json.dumps(responce,indent=2)
# print(responce)


a = "dryed tea"
for i in responce:
    ingredients = i["ingredients"]
    # print(ingredients)
    
    if ingredients!=None:
        # print(ingredients)
        for j in ingredients:
            if a in j:
                print(json.dumps(i,indent=3))
    
