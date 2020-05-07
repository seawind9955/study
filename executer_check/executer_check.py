#!/usr/local/bin/python3
# coding=utf-8
import requests
import json

def login(username, password):
    url = "http://www.hotent.xyz:8088/auth"
    params = {
        'username': username,
        'password': password
    }
    params_json = json.dumps(params)

    header={
        'Content-Type': 'application/json;charset=utf-8',
    }
    response = requests.post(url, params_json,headers=header)
    #print(response.text)
    return(json.loads(response.text))

def getInstDetailList(account, token):
    url = "http://www.hotent.xyz:8088/runtime/instance/v1/getInstDetailList"
    params = {
         "pageBean": {
            "page": 0,
            "pageSize": 0,
            "showTotal": True
        }
    }
    params_json = json.dumps(params)
    auth = "Bearer " + token 
    header={
        'Content-Type': 'application/json;charset=utf-8',
        'authorization': auth
    }
    response = requests.post(url, params_json, headers=header)
    #with open('proc_data.txt','w',encoding='utf-8') as f:
        f.write(response.text)
    print(response.text)

login_info = login("admin", "123456")
getInstDetailList("admin", login_info["token"])

   # print(login("admin", "123456")["token"])