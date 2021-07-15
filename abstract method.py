from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod 
    def process(self):
         pass


com = abstract()
com.process()