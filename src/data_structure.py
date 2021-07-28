'''
(doc/cookies.json doc/data.json setting.json) setting先暫緩
資料轉json
json導出資料
'''
import json
import time

'''     JSON資料結構設定        '''

data_template = {
    "website": "",
    "items_keywords": [None,None,None,None,None],
    "items_values": 0,
    "payment_method": [],
    "delivery_method": [],
    "times": {
        "month": 0,
        "day": 0,
        "hour": 0,
        "min": 0
    }
}


def CookiesToJSON(cookies):
    jsonCookies = json.dumps(cookies)
    with open('doc/cookies.json', 'w') as f:
        f.write(jsonCookies)

def FirstDataToJson():
    empty_list = []
    empty_list_json = json.dumps(empty_list)
    with open('doc/data.json', 'w') as f:
        f.write(empty_list_json)

def DataToJSON(copy_data_template):
    try:
        with open('doc/data.json', 'r', encoding='utf-8') as f:
            listJson = json.loads(f.read())
    except:
        FirstDataToJson()
        time.sleep(2)
        with open('doc/data.json', 'r', encoding='utf-8') as f:
            listJson = json.loads(f.read())

    listJson.append(copy_data_template)
    jsonData = json.dumps(listJson)
    with open('doc/data.json', 'w') as f:
        f.write(jsonData)
        f.close()



def JcookiesExport():
    return_data=[]
    with open('doc/cookies.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())


    for cookie in listCookies:
        return_data.append({
            'domain': cookie['domain'],
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })
    return return_data

def Jdata_export():
    with open('doc/data.json','r',encoding='utf-8') as f:
        listData = json.loads(f.read())
    return listData
