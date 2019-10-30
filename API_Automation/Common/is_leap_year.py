
def is_leap_year(year):
    if isinstance(year,int) is not True:
        raise  TypeError('传入的参数不是整数')
    elif year == 0:
        raise ValueError('传入的参数不能为0')
    elif abs(year)!=year:
        raise ValueError('传入的参数不是正整数！')
    elif (year %4==0 and year % 100!=0) or year % 400==0:
        print('%d年是闰年' % year)
        return True
    else:
        print('%d年不是闰年' % year)
        return False