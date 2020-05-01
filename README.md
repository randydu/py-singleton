# py-singleton

Singleton pattern for python 2 & 3.

## Usage

### install

```sh
pip install py-singleton
```

### API

- Apply class decorator _singleton_ to any class;
- Expected behaviors:
  - class can be instantiated as usual, but only one instance is created;
  - apis to access the class instance:

    ```python
    @singleton
    class Server(object):pass

    srv = Server()
    ```

    or

    ```python
    srv = Server.instace()
    ```

  - the function \__init\__() of decorated class will be called only once when the first instance is created.

### Example

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
    assert id(a1) == id(a2)
    assert id(a1) == id(a3)
```
