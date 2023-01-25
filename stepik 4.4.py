# https://stepik.org/lesson/623073/step/7?auth=login&unit=618703

import json

with open('data.json', encoding='utf-8') as file:
    x = json.load(file)
    x2 = []
    for i in x:
        if type(i)==int:
            x2.append(i+1)
        elif type(i)==str:
            x2.append(i+'!')
        elif type(i)==list:
            i.extend(i)
            x2.append(i)
        elif type(i)==dict:
            i.update({"newkey": None})
            x2.append(i)
        elif type(i)==bool:
            x2.append(not i)
        else:
            continue

with open('updated_data.json', 'w', encoding='utf-8') as file2:
    json.dump(x2, file2)
