import random

def simple_list():
    list = []
    for i in range(10):
        list.append({'id': i , 'age' : random.randint(1,100)})
    return list

def sort_list(dicts):
    return sorted(dicts, key=lambda n: n['age'], reverse=False)
