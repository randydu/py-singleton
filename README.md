py-singleton
============

Singleton pattern for python 2 & 3.


Install
-------

```sh
pip install py-singleton
```

Test
----

in the root folder, run pytest:

```bash
pytest
```

Dependencies
------------

None

unit test needs __pytest__.

API
----

- Apply class decorator _singleton_ to any class;
- Expected behaviors:
  - class can be instantiated as usual, but only one instance is created;
  - apis to access the class instance:

  ```python
    @singleton
    class Server(object):
      pass

    srv = Server()
  ```

    or

  ```python
    srv = Server.instance()
  ```

  - the function \__init\__() of decorated class will be called once and only once when the instance is created.

Example
--------

```python

from py_singleton import singleton

    @singleton
    class A(object):
        count = 0
        def __init__(self):
            A.count += 1

    a1 = A()
    a2 = A()
    a3 = A.instance()

    assert A.count == 1
    assert a1 is a2
    assert a1 is a3
```

Limitation
----------

For best performance, the code to create instance is not thread-safe, however, after the instance is created it should
be safe for multi-threading.

It is recommended to call __instance()__ once during the initial phrase of your app in a single thread.