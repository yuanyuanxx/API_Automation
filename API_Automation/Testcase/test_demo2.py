# -*- coding:utf-8 -*-
import pytest

# @pytest.fixture(params=[1, 2, 3])
# def fixture_param(request):
#     request.param
#     print("\033[31;1m我是fixture_param，这是第%s次打印\033[0m" % request.param)
#     return request.param
#
# def test_fixture_param(fixture_param):
#     print("我是test_fixture_param函数")
#
# @pytest.mark.parametrize("fixture_param",["a",'b'],indirect=True)
# @pytest.mark.parametrize('a,b',[(1,6),(3,5)])
# #参数indirect=True，一定不能少，要不就会直接把 fixture_param当成测试函数的一个参数来用，
# # 加上indirect=True这个参数，才会在fixture的函数中查找,否则不会执行"我是fixture_param,这是第a次打印"
# def test_fixture_param_parametrize(a,b,fixture_param):
#     print("是测试函数test_fixture_param_and_parametrize,a=%s,b=%s"%(a,b))

def test_demo7():
    p=range(2,9)
    a=[i for i in p]
    print(a)


class DB(object):
    def __init__(self):
        self.intransaction = []
    def begin(self, name):
        self.intransaction.append(name)
    def rollback(self):
        self.intransaction.pop()

@pytest.fixture(scope="module")
def db():
    return DB()

class TestClass(object):
    @pytest.fixture(autouse=True)
    #当autouse为true时，类中的所有测试方法都将使用此fixture，
    # 无需在测试函数添加或使用类级别的fixture
    def transact(self, request, db):
        db.begin(request.function.__name__)
        yield
        db.rollback()
    def test_method1(self, db):
        assert db.intransaction == ["test_method1"]
    def test_method2(self, db):
        assert db.intransaction == ["test_method2"]



import os

@pytest.fixture(autouse=True)
def abc():
    print('I am abc')

@pytest.mark.repeat(3) #重复执行测方法3次
def test_create_file(tmpdir):
    '''重复执行功能'''
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    assert p.read() == "content"
    a=tmpdir.listdir()
    print(a)
    #assert 0

