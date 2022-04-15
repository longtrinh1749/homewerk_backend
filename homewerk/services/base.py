from homewerk import models

class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError('This is singleton class')

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance