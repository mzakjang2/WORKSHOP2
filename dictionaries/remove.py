thisdict = {"brand": "ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)

thisdict = {"brand": "ford", "model": "Mustang", "year": 1964}
thisdict.popitem("model")
print(thisdict)

thisdict = {"brand": "ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)

thisdict = {"brand": "ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)