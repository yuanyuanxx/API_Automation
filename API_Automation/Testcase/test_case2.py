import pytest
import allure
import requests, urllib3
urllib3.disable_warnings()

test_login_data = [{'user':'QQ:88428977', 'psw':'111111', 'uri':'xxxx'},
                   {'user':'xxxx', 'psw':'111111', 'uri':'xxxx'}]

#s = requests.session()

@pytest.fixture(scope='module')
#@allure.feature('登陆测试方法2')
def login(request):
    '''登陆测试'''
    user = request.param['user']
    psw = request.param['psw']
    uri = request.param['uri']
    print("登陆账户：%s" % user)
    print("登陆密码：%s" % psw)
    print("登陆网址：%s" % uri)


# indirect=True  声明login是个函数
@pytest.mark.parametrize("login", test_login_data, indirect=True)
def test_login(login):
    '''登陆用例'''
    result = login
    print(result)
    # print("测试用例中login的返回值：%s" % result)
    # assert result['status'] == 202



