# -*- coding:utf-8 -*-
import os
import random
from collections import namedtuple
from collections import OrderedDict
import pytest
import requests




class  Testclass():
    @pytest.mark.skip(reason="not execute")
    def test_demo1(self):
        a={'a':1,'v':2,'d':3,'t':4}
        print(a.get('s'))
        c=a.pop('t')
        print(c)
        print(a)

    def test_demo2(self):
        a=['cat','window','defenestrate']
        for w in a[:]:
            if len(w)<4:
                a.insert(0,w)
                print(a)

    @pytest.mark.xfail()
    def test_a(self):
        a=3
        assert a%2==0,'value was odd, should be even'

    def test_b(self):
        data=[2,4,7]
        sumdata=[n+1 for n in data if n%2==1]
        print(sumdata)

    def test_get_cookie(self):
        '''
        获取cookie的jar文件
        '''
        url = "http://m.imooc.com/passport/user/login&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        print(cookie)

    #判断2-100中哪些是素数
#     def test_demo3():
#         i = 2
#         while (i < 100):
#             j = 2
#             while (j <= (i / j)):
#                 if not (i % j):
#                     break
#                 j = j + 1
#             if (j > i / j):
#                 print(i, " 是素数")
#             i = i + 1
#         print ("Good bye!")
#
#     def test_demo4():
#         print("当前工作目录：%s" % os.getcwd())
#
#     def test_demo5():
#         articleInfo = [{"tid": 101115, "lang": "en", "subjectId": 1043},
#                             {"tid": 101111, "lang": "jp", "subjectId": 1050},
#                             {"tid": 101133, "lang": "kr", "subjectId": 1056}
#                        ]
#         # i=random.randint(0,3)
#         # print(i)
#         artinfo=articleInfo[2]
#         print(artinfo)
#         lang=artinfo["lang"]
#         print(lang)
#
#     def test_demo6():
#         point = namedtuple('point', ['x', 'y'])
#         t_point=point('test1','test2')
#         t_dict=t_point._asdict()
#         excepted={'x':'test3','y':'test2'}
#         assert excepted==t_dict
#         print(t_dict)
#         p = point(1, 2)
#         print(p.x)
#         #_replace方法并不是改变point里的x，
#         #而是新建了一个p，这个新建的p中的x=3，
#         #所以要改变原来的p还必须加上p=p._replace的这样的赋值语句
#         p._replace(x=3)
#         print(p.x)
#         p = p._replace(x=3)
#         print(p.x)
#
#
    # def test_demo7():
    #     p=range(2,9)
    #     for i in p:
    #         print(i)
#
#
# '''
# def test_demo2():
#     dictionary = {}
#     flag = 'a'
#     pape = 'a'
#     off = 'a'
#     while flag == 'a' or 'c' :
#         flag = input("添加或查找单词 ?(a/c)")
#         if flag == "a" :                             # 开启
#             word = input("输入单词(key):")
#             defintion = input("输入定义值(value):")
#             dictionary[str(word)] = str(defintion)  # 添加字典
#             print ("添加成功!")
#             pape = input("您是否要查找字典?(a/0)")   #read
#             if pape == 'a':
#                 print (dictionary)
#             else :
#                 continue
#         elif flag == 'c':
#             check_word = input("要查找的单词:")  # 检索
#             for key in sorted(dictionary.keys()):            # yes
#                 if str(check_word) == key:
#                     print ("该单词存在! ",key, dictionary[key])
#                     break
#                 else:                                       # no
#                     off = 'b'
#             if off == 'b':
#                 print ("抱歉，该值不存在！")
#         else:                               # 停止
#             print ("error type")
#             break
# '''


