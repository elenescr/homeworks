def dict(d):
    a = d.items()
    if len(a) == 0:
        return "dictionary is empty"
    else:
        return "dictionary is not empty"

car = {"brand": "Ford",
       "model": "Mustang",
       "year": 1964
       }
plane = {}

print(dict(car))
print(dict(plane))