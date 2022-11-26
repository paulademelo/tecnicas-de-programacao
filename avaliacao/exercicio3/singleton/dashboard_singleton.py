from abc import ABC, abstractclassmethod, abstractmethod

class AbstractCalculatePointsSingleton(ABC):

    @abstractclassmethod
    def get_instance():
        raise RuntimeError('TODO: Método ainda não implementado')

class CalculatePointsSingleton(AbstractCalculatePointsSingleton):

    def __init__(self):
        raise RuntimeError('Singleton!!')

    @classmethod
    def instance__(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            return cls._instance
        else:
            print("Instance has already been created")          
            return cls._instance