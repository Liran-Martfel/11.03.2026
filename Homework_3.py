def new_dict():
    dict1 = {
        "name": "Dan",
        "city": "Tel Aviv",
        "job": "Dev"
    }

    dict2 = {
        "name": "Daniel",
        "city": "TA",
        "country": "Israel"
    }
    dict3 = {}
    if dict1.get("name") in dict2.get("name"):
        dict3["name"] = dict2["name"]
    if dict2.get("city")[0] == dict1.get("city")[0] and dict2.get("city")[1] == dict1.get("city")[4]:
        dict3["city"] = dict1["city"]
    if dict1.get("job") in dict1.get("job"):
        dict3["job"] = dict1["job"]
    dict3["country"] = dict2["country"]

    return dict3

print(new_dict())