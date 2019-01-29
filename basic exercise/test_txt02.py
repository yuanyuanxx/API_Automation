import pytest

def add(a,b):
    return a+b

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        print(f())


def test_sum():
   assert  add(2,4)==6


