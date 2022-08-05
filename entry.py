
import json

person = {
    1:{
    'surname': 'Lindt',
    'name': 'Till', 
    'tel': '12345', 
    'comment': 'work'
    },
    2:{
    'surname': 'Hory',
    'name': 'Loky', 
    'tel': '98745', 
    'comment': 'club'
    }
}

def enter_person():
    with open('person.json') as file:
        l_data = json.load(file)
    key = []
    for k in l_data:
        key.append(k[0])
        key_id = int(max(key)) + 1
    print(key_id)

    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    tel = input('Введите телефон: ')
    comment = input('Добавьте комментарий: ')
    new_person = \
        {
            key_id:{
                'surname': name,
                'name': surname, 
                'tel': tel, 
                'comment': comment
            }
        }
    result = {**l_data,**new_person}
    with open('person.json', 'w') as f:
        json.dump(result, f, indent =3)
    return
