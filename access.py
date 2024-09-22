import inspect

class AccessControlMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and attr_name.startswith('__') and not attr_name.startswith('___') and attr_name != '__init__':
                attrs[attr_name] = cls.private_method(attr_value)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def private_method(func):
        def wrapper(self, *args, **kwargs):
            original_class = func.__qualname__.split('.')[0]
            if self.__class__.__name__ != original_class:
                raise AttributeError(f"Private method '{func.__name__}' cannot be accessed.")
            return func(self, *args, **kwargs)
        return wrapper

def public(func):
    return func

def protected(func):
    def wrapper(self, *args, **kwargs):
        if not isinstance(self, self.__class__):
            raise AttributeError(f"'{func.__name__}' is protected and cannot be accessed outside its class or subclasses.")
        return func(self, *args, **kwargs)
    return wrapper

def private(func):
    def wrapper(self, *args, **kwargs):
        if func.__name__ == '__init__':
            return func(self, *args, **kwargs)
        if type(self) is func.__qualname__.split('.')[0]:
            return func(self, *args, **kwargs)

        raise AttributeError(f"'{func.__name__}' is private and cannot be accessed outside its class.")
    return wrapper


def public_class(cls):
    return cls

def protected_class(cls):
    class Wrapped(cls, metaclass=AccessControlMeta):
        def __init__(self, *args, **kwargs):
            if type(self) is Wrapped:
                raise AttributeError(f"{cls.__name__} is a protected class and cannot be instantiated directly.")
            super().__init__(*args, **kwargs)

    return Wrapped

def private_class(cls):
    class Wrapped(cls, metaclass=AccessControlMeta):
        def __init__(self, *args, **kwargs):
            if type(self) is Wrapped:
                raise AttributeError(f"{cls.__name__} is a private class and cannot be instantiated directly.")
            super().__init__(*args, **kwargs)

    return Wrapped