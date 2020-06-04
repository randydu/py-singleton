""" Singleton Utility """

__version__ = "1.0.0"
__license__ = "MIT"
__author__ = "Randy Du <randydu@gmail.com>"


def singleton(cls):
    """ class decorator to implement singleton pattern

        @singleton
        class A: pass

        a1 = A()
        a2 = A.instance()

        assert a1 is a2

    """

    # pylint: disable=too-few-public-methods
    class SingleCls(cls):
        ''' inner wrapper class '''

        inst = None
        inited = False

        def __new__(cls, *args, **kwargs):
            if cls.inst is None:
                cls.inst = object.__new__(cls, *args, **kwargs)
            return cls.inst

        def __init__(self, *args, **kwargs):
            if not self.inited:
                self.inited = True
                super(SingleCls, self).__init__(*args, **kwargs)

        @classmethod
        def instance(cls):
            ''' get the singleton instance '''
            return cls.inst if cls.inst else cls()

    # simulate the name of input class
    SingleCls.__name__ = cls.__name__
    if hasattr(cls, "__qualname__"):  # python 2
        SingleCls.__qualname__ = cls.__qualname__

    SingleCls.__module__ = cls.__module__
    SingleCls.__doc__ = cls.__doc__

    return SingleCls
