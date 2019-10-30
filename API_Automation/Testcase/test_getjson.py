import  os,json,codecs
import unittest
print(os.getcwd())

def get_case():
    with codecs.open('data.json','r',encoding='utf-8') as jsonfile:
        f_dict=json.load(jsonfile)
        for collection,cases in f_dict.items():
            for case in cases['interface_info']:
                yield {collection:case}

def test_get_data():
    cases = get_case()
    datas = []
    for case_d in cases:
        for collection, case in case_d.items():
            url_method = case['interface_method']
            method = case['method']
            headers = case["headers"]
            url_data = case['url_data'] # if case['url_data'] is None else tuple(case['url_data'])
            data = case['data']
            params = case['params']
            auth = case['auth']
            cookies = case['cookies']
            hooks = case['hooks']
            json = case['json']
            except_data = case['except']
            t = (url_method, method, headers, url_data, data, params, auth, cookies, hooks, json, except_data)
            datas.append(t)

    print(datas)
