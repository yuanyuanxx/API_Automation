import requests
import json
def checkGetSubject(url,params):
    r = requests.get(url,params)
    #print(r.url)
    jsonresult=r.json()
    #输出可读性高的json,sort_keys=True按照字母排序显示
    #print(json.dumps(jsonresult,indent=2,sort_keys=True))
    #检查接口返回的关键词是否正确
    keys=['subjects','total']
    foundimportantkeys=[k for k in keys if k in jsonresult]
    print('\n',foundimportantkeys)
    #获取json中'subjects'的值
    data=jsonresult["subjects"]
    #获取subject下'alt'的值
    get_alt=data[0]['alt']
    print(get_alt)
    assert len(foundimportantkeys)==2
    if r.status_code==200:
        return True
    elif r.status_code=='345':
        return False
        print("接口返回错误")
