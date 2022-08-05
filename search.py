import json

def search():
    search = input("Что искать будем? ")
    with open('person.json') as file:
        data = json.load(file)
    #print(data)
    for key, val in data.items():
        for k, v in val.items():
            if v == search:
                print(data[key])
    return
