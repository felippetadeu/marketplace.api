import logging
from infrastructure.logging.handlers.abstract_handler import AbstractHandler

class StreamHandler(AbstractHandler, logging.StreamHandler):

    def __init__(self, settings: dict):
        self.settings = settings
        super().__init__()
        logging.StreamHandler.__init__(self)
        self._configure()

    def _configure(self):
        formatter = logging.Formatter(self.settings['formatter'])
        self.setFormatter(formatter)