#!/usr/local/bin/python3
# coding=utf-8
import requests
import json
import hashlib
import datetime
import time
import random
# login
#url = "https://interface5.spicit.com.cn/appInterface/user/login"

login_data = [
    {
        #'name':许功胜
        'phone':"18663187137",
        'password':"1234qwer"
    },
    {
        #'name':潘航
        'phone':"18663187145",
        'password':"13484574119ph"
    },
    {
	#'name':曹总
	'phone':"18663187702",
	'password':"rc131030"
    },
    {
	#'name':白哥
	'phone':"18663187367",
	'password':"bxp800515"
    }
]
# M-eM-!M-+M-fM-^JM-%
def submit(phone, password):
    # M-eM-/M-9M-eM-/M-^FM-gM- M-^AM-hM-?M-^[M-hM-!M-^Lmd5M-eM-^JM- M-eM-/M-^F
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    password = md5.hexdigest()
    #M-hM-^NM-7M-eM-^OM-^VM-eM-=M-^SM-fM-^WM-%M-fM-^WM-%M-fM-^\M-^_
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    #print(date)

    url = "https://interface5.spicit.com.cn/api/v1.0/sysUser/login?mobile=" + phone + "&password=" + password
    response = requests.get(url)
    data = json.loads(response.text)["data"]
    #print(data)
    token = data["token"]
    fillUserid = data["id"]
    fillUsername = data["name"]
    organCode = data["companyId"]
    # M-fM-^KM-<M-fM-^NM-%M-hM-.M-$M-hM-/M-^AM-eM--M-^WM-gM-,M-&M-dM-8M-2M-oM-<M-^LM-eM--M-^XM-eM-^\M-(headerM-dM-8M--
    auth_str = phone + ' ' + token
    header={
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Authorization': auth_str
    }
    num = random.randint(0,8)
    temp = str(36 + num / 10)

    data_save = {
        'backTime' : "",
        'backTraffic' : "",
        'backWay' : "",
        'contactDetail' : "",
        'currentHealthState' : "正常",
        'currentLocation' : "凤凰湖生活区",
        'destination' : "",
        'fillAccount' : phone,
        'fillDate' : date,
        'fillUserid' : fillUserid,
        'fillUsername' : fillUsername,
        'isContact' : "否",
        'isLeaveCompany' : "否",
        'isOverseas' : "否",
        'isStay' : "否",
        'isWorking' : "是",
        'leaveTime' : "",
        'leaveTraffic' : "",
        'leaveWay' : "",
        'morningTemp' : temp,
        'nowPlace' : "中国大陆",
        'orgCode' : organCode,
        'otherBackTime' : "",
        'otherOverseas' : "否",
        'takeTogetherDate' : "",
        'workingWay' : "自驾"
    }

    url = "https://interface5.spicit.com.cn/api/v1.0/healthFill/save"
    data_json = json.dumps(data_save)
    response = requests.post(url, data_json, headers=header)
    print(response.text)

date = datetime.datetime.now().strftime('%Y-%m-%d')
print(date)

for p in login_data:
    r = random.randint(0,30)
    time.sleep(r)
    print(r)
    submit(p['phone'], p['password'])

'''
url = 'https://interface5.spicit.com.cn/api/v1.0/healthFill/findDataByOrgCodeOrUserName'
data_json = json.dumps({'fillDate': "2020-04-27", 'fillUserid': fillUserid})

response = requests.post(url, data_json, headers=header)
#print(response.text)
data_json_obj = json.loads(response.text)['data'][0]
temp = data_json_obj['morningTemp']
isStay = data_json_obj['isStay']
isContact =  data_json_obj['isContact']
isOverseas =  data_json_obj['isOverseas']
otherOverseas = data_json_obj['otherOverseas']

data_json_obj['morningTemp'] = '36.5'
data_json_obj['isStay'] = 'M-eM-^PM-&'
data_json_obj['isContact'] = 'M-eM-^PM-&'
data_json_obj['isOverseas'] = 'M-eM-^PM-&'
data_json_obj['otherOverseas'] = 'M-eM-^PM-&'

print(temp, isStay, isContact, isOverseas, otherOverseas)
'''
