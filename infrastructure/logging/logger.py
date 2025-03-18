from infrastructure.logging.abstract_logger import AbstractLogger
from infrastructure.logging.handlers.handler_factory import HandlerFactory, AbstractHandler
from configuration import Configuration
from typing import List
import logging

loggers = {}

class Logger(AbstractLogger):

    def __init__(self, default_level: int = None):
        """
        Args:
            default_level (int, optional): Default Logging Level, pode ser passado o logging.X, caso não seja passado será
            utilizado o valor que consta no arquivo de settings.
        """
        self._handlers = []
        if loggers.get(Configuration.get_settings("application.name"), None) is None:
            self.default_level = default_level
            self.logger = logging.getLogger(Configuration.get_settings("application.name"))
            logging_settings: dict = Configuration.get_settings("logging")
            if self.default_level is None:
                # /* CRITICAL = 50, FATAL = CRITICAL, ERROR = 40, WARNING = 30, WARN = WARNING, INFO = 20, DEBUG = 10, NOTSET = 0*/
                self.default_level = self.get_log_level(logging_settings['level'])

            self.logger.setLevel(self.default_level)

            handlers: List[AbstractHandler] = HandlerFactory.get_handlers()
            for handler in handlers:
                self.logger.addHandler(handler)
                self._handlers.append(handler)
            
            loggers[Configuration.get_settings("application.name")] = self.logger
        else:
            self.logger = loggers[Configuration.get_settings("application.name")]

    @property
    def handlers(self):
        return self._handlers

    async def log(self, message, level = None):
        if level is None:
            level = self.default_level

        self.logger.log(level, message)