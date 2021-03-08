import requests
from pprint import pprint

GET_ENDPOINT = "https://api.sheety.co/ca700cff5747162c513bf4821d202b1a/sheetyStudy/sheet1"
POST_ENDPOINT = "https://api.sheety.co/ca700cff5747162c513bf4821d202b1a/sheetyStudy/sheet1"
PUT_ENDPOINT = "https://api.sheety.co/ca700cff5747162c513bf4821d202b1a/sheetyStudy/sheet1" # /[object ID]
DELETE_ENDPOINT = "https://api.sheety.co/ca700cff5747162c513bf4821d202b1a/sheetyStudy/sheet1" #/[Object ID]

put_object_id = 0
delete_object_id = 0

post_json = {
    "sheet1":{
        "hello":"1",
        "test":"2",
        "sheet":"3",
    }
}

put_json = {
    "sheet1":{
        "hello":"88",
        "test":"88",
        "sheet":"88",
    }
}

def get():
    get_response = requests.get(url=GET_ENDPOINT)
    print(get_response)
    print(get_response.json())

def post():
    post_response = requests.post(url=POST_ENDPOINT, json=post_json)
    print(post_response)
    print(post_response.json())

def put(id):
    put_response = requests.put(url=f"{PUT_ENDPOINT}/{id}", json=put_json)
    print(put_response)
    print(put_response.json())

def delete(id):
    delete_response = requests.delete(url=f"{DELETE_ENDPOINT}/{id}")
    print(delete_response)
    print(delete_response.json())
