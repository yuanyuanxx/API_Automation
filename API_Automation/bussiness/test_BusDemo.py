from API_AuCommon.RunMethon import RunMethon
from Config.testinterfance_info import InterInfo
import json
from Common import check


# class TestBaseDemo():
#
#     def test_hj_read(self):
#         data = {
#                 "langs": "en",
#                 "subscribeType": 1,
#                 "subscribeTypeId": 2
#             }
#         headers = {
#             "Content-Type": "application/json",
#             "ClubAuth": "3130313335333137332e3530623233633638633738306232356233373133376239303963316639333034"
#         }
#
#         url1 = InterInfo().hujiangUrl()
#         url3 = url1 + '/art/v1/subscribe'
#         respons = RunMethon.post_moethon(self, url=url3, data=data, headers=headers)
#         # ensure_ascii=False 使编码返回正常的中文
#         responsresult = json.dumps(respons, ensure_ascii=False)
#         responsresult.encode('UTF-8')
#         print(responsresult)
        #print(responsresult[1])
        #assert int(result) == status

    # def test_mukestudyUrl_read(self):
    #     ipinfo = InterInfo().mukestudyUrl()
    #     url = ipinfo+'/api/topics/hot.json'
    #     respons = RunMethon.get_moethon(self, url=url, data=None, header=None)
    #     # responsresult=json.dumps(respons)
          # 返回的json是列表格式，以列表类型取值
    #     res = respons[0]
    #     lst = list(res)
    #     #print(lst)
    #    check.checkKeysInDict(['node', 'member'], lst)












