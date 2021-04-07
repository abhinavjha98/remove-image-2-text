import json
f = open("env.json")
data = json.load(f)
for i in data["data"]:
    print(i['file_to_scan'])
f.close