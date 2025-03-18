from abc import ABC, abstractmethod
import logging

class AbstractLogger(ABC):

    @property
    @abstractmethod
    def handlers(self):
        pass


    def get_log_level(self, level_str: str):
        # Convert the string to uppercase to match the logging attributes.
        level = getattr(logging, level_str.upper(), None)
        if not isinstance(level, int):
            raise ValueError(f"Invalid log level: {level_str}")
        return level

    @abstractmethod
    def log(self, message: str, level: int = None) -> None:
        """Registra uma mensagem de log com o nível especificado
        Args:
            message (str): Mensagem de erro
            level (int, optional): Default Logging Level, pode ser passado o logging.X, caso não seja passado será
            utilizado o valor que consta no arquivo de settings.
        """
        pass

