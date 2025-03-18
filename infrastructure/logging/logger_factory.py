from infrastructure.logging.logger import Logger
from infrastructure.logging.abstract_logger import AbstractLogger

class LoggerFactory:
    
    @staticmethod
    def get_logger(default_level: int = None) -> AbstractLogger:
        """
        Args:
            default_level (int, optional): _description_. Defaults to None.

        Returns:
            AbstractLogger: _description_
        """
        return Logger(default_level)