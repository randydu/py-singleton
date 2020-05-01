"""
    function utilities
"""

__version__ = "0.9.2"



def _singleton1(cls):
    """ class decorator to implement singleton pattern 
    
        @singleton
        class A: pass

        a1 = A()
        a2 = A.instance()

        assert(id(a1) == id(a2))
    
    Advantage:

        the input class is not wrapped by another class

    Side Effects:

        a private field '_singleton' is injected to the input class
    """
    cls._singleton = { "inst": None, "inited": False, "__init__": None }

    @classmethod
    def new(c, *args):
        if c._singleton['inst'] is None:
            c._singleton['inst'] = object.__new__(c)
        return c._singleton['inst']
        
    def init(self, *args, **kwargs):
        if not self._singleton['inited']:
            self._singleton['inited'] = True
            self._singleton['__init__'](self, *args, **kwargs) 

    @classmethod
    def instance(c):
        return c._singleton['inst'] if c._singleton['inst'] else c()

    cls.__new__ = new
    cls._singleton['__init__'] = cls.__init__
    cls.__init__ = init
    cls.instance = instance

    return cls


def _singleton2(cls):
    """ class decorator to implement singleton pattern 
    
        @singleton
        class A: pass

        a1 = A()
        a2 = A.instance()

        assert(id(a1) == id(a2))
    
    Advantage:

        no field injection to input class

    Side Effects:

        the input class is wrapped by another class
    """
    class SingleCls(cls):
        inst = None
        inited = False

        def __new__(cls, *args):
            if cls.inst is None:
                cls.inst = object.__new__(cls)
            return cls.inst
        
        def __init__(self, *args, **kwargs):
            if not self.inited:
                self.inited = True
                super(SingleCls, self).__init__(*args, **kwargs) 

        @classmethod
        def instance(cls):
            return cls.inst if cls.inst else cls()

    # simulate the name of input class
    SingleCls.__name__ = cls.__name__
    if hasattr(cls, "__qualname__"): # python 2
        SingleCls.__qualname__ = cls.__qualname__

    return SingleCls


# select which impl to use?
singleton = _singleton2

