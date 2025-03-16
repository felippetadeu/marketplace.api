import logging
from infrastructure.logging.logger import Logger
from configuration import Configuration

loggers = {}

class ConsoleLogger(Logger):

    def __init__(self, default_level: int = None):
        """
        Args:
            default_level (int, optional): Default Logging Level, pode ser passado o logging.X, caso não seja passado será
            utilizado o valor que consta no arquivo de settings.
        """
        if loggers.get(Configuration.get_settings("application.name"), None) is None:
            self.default_level = default_level
            self.logger = logging.getLogger(Configuration.get_settings("application.name"))
            console_settings: dict = Configuration.get_settings("logging.console")
            if default_level is None:
                self.default_level = console_settings['level']

            self.logger.setLevel(self.default_level)

            handler = logging.StreamHandler()
            formatter = logging.Formatter(console_settings['formatter'])
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            loggers[Configuration.get_settings("application.name")] = self.logger
        else:
            self.logger = loggers[Configuration.get_settings("application.name")]

    def log(self, message, level = None):
        if level is None:
            level = self.default_level

        self.logger.log(level, message)