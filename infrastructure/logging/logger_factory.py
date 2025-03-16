from infrastructure.logging.console_logger import ConsoleLogger
from infrastructure.logging.logger import Logger

class LoggerFactory:
    
    @staticmethod
    def get_logger(default_level: int = None) -> Logger:
        return ConsoleLogger(default_level)