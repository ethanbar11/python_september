import json


def write_json():
    d = {'Hello': 'To you', 'Woho': 5, 'Bli bla': [1, 2, 3], 'True': True}
    with open('json_file.json', 'w') as f:
        json.dump(d,f)


def read_json():
    with open('json_file.json', 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    write_json()
    returned_dictioanry=read_json()
    print(returned_dictioanry)
    print(type(returned_dictioanry))
