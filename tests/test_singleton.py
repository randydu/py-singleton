from py_singleton import singleton

def test_singleton():
    @singleton
    class A(object):
        count = 0
        def __init__(self):
            A.count += 1

    a1 = A()
    a2 = A()
    a3 = A.instance()

    assert A.count == 1
    assert id(a1) == id(a2)
    assert id(a1) == id(a3)


    