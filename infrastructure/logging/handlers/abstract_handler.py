from abc import ABC, abstractmethod
from logging import Handler

class AbstractHandler(ABC, Handler):
    
    def __init__(self):
        Handler.__init__(self)

    @abstractmethod
    def _configure(self):
        pass