import requests
import  json

class RunMethon:
    def get_moethon(self, url, data=None, headers=None):
        res=None
        if headers!= None:
            res=requests.get(url=url, data=data, headers=headers, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.json()

    def post_moethon( url, data=None, headers=None):
        res = None
        if headers != None:
            res = requests.post(url=url, data=data, headers=headers, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    # def run_main(self, method, url, data=None, header=None):
    #     res = None
    #     if method == 'Post':
    #         res = self.post_main(url, data, header)
    #     else:
    #         res = self.get_main(url, data, header)
    #
    #     return json.dumps(res, ensure_ascii=False)


