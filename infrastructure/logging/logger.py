from abc import ABC, abstractmethod
import logging

class Logger(ABC):

    @abstractmethod
    def log(self, message: str, level: int = None) -> None:
        """Registra uma mensagem de log com o nível especificado
        Args:
            message (str): Mensagem de erro
            level (int, optional): Default Logging Level, pode ser passado o logging.X, caso não seja passado será
            utilizado o valor que consta no arquivo de settings.
        """
        pass

