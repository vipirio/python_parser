from abc import ABC, abstractmethod


class PyParser(ABC):
    """ This is Abstract class of python parser and accept only file_path as input """
    def __init__(self,file_path):
        self.file_data = open(file_path).read().split('\n')

    @abstractmethod
    def parse_log(self):
        """ This is abstract method for generate output """
        pass


