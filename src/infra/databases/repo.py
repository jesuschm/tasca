from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

@dataclass
class Repo(metaclass=ABCMeta):
    
    @classmethod
    def __subclasshook_(cls, subclass):
        return (hasattr(subclass, 'upsert') and 
                callable(subclass.upsert) and
                hasattr(subclass, 'get') and 
                callable(subclass.get))
        
    @abstractmethod
    def upsert(self):
        raise NotImplementedError

    @abstractmethod
    def get(self):
        raise NotImplementedError