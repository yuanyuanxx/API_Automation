# -*- coding:utf-8 -*-
# 使用Locust进行性能测试
from locust import HttpLocust, TaskSet, task

class performDemo(TaskSet):
    @task(1)
    def open_blog(self):
        header={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
        r=self.client.get("/yoyoketang",headers=header,verify=False)
        print(r.status_code)
        assert r.status_code==200

class websitUser(HttpLocust):

    #指向一个定义了的用户行为类
    task_set=performDemo
    #用户执行任务之间等待时间的下界，单位：毫秒
    min_wait=3000
    #用户执行任务之间等待时间的上界，单位：毫秒。
    max_wait=6000

#终端命令输入：locust -f  performancetest.py --host=https://www.cnblogs.com
#-f 参数是指定运行的脚本,--host是指定运行项目的host地址，
# 这里用的https://www.cnblogs.com，代码里面get访问的是"/yoyoketang"，拼接起来就是完整地址
#在浏览器输入http://localhost:8089/
'''
charts界面的三个图标分别是

吞吐量/每秒响应事务数（rps）实时统计
平均响应时间/平均事务数实时统计
虚拟用户数运行
'''


'''from locust import HttpLocust, TaskSet, task
import subprocess
import json


# 性能测试任务类 TaskSet.
class UserBehavior(TaskSet):
    # 开始
    def on_start(self):
        pass

    # 任务
    @task(1)
    def getTagVals(self):
        u"""
        request_url：请求路径
        request_params：请求头参数
        request_json：请求json参数
        """
        request_url = "/xxx/tag/getTagVals" （待测试的路径）
        request_params = {
            "nonce": "abcdefg",
            "_type": None,
            "target": "CLNJ01",
            "timestamp": 1507860000,
            "apiId": "EC",
            "apiSign": "D41D8CD98F00B204E9800998ECF8427E"
        }
        request_json = {
            "tagKey": 25
        }
        response = self.client.post(
            url=request_url,
            params=request_params,
            json=request_json
        )
        if response.status_code != 200:
            print u"返回异常"
            print u"请求返回状态码:", response.status_code
        elif response.status_code == 200:
            print u"返回正常"

        # 这里可以编写自己需要校验的返回内容
        # content = json.loads(response.content)["content"]
        # if content["tagKey"] == 25:
        #     print u"校验成功"
        #     print json.dumps(content, encoding="UTF-8", ensure_ascii=False)


# 性能测试配置
class MobileUserLocust(HttpLocust):
    u"""
    min_wait ：用户执行任务之间等待时间的下界，单位：毫秒。
    max_wait ：用户执行任务之间等待时间的上界，单位：毫秒。
    """
    # weight = 3
    task_set = UserBehavior
    host = "http://xxx"  （待测试的ip或者域名）
    min_wait = 3000
    max_wait = 6000


'''
