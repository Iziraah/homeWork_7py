import json


def delete():
    del_item = 0
    search = input("Что искать будем? ")
    with open('person.json') as file:
        data = json.load(file)
        # print(data)
    for key, val in data.items():
        for k, v in val.items():
            if v == search:
                del_item = key
            
    data.pop(del_item)
    with open('person.json', 'w') as f:
        json.dump(data, f, indent =3)
    return