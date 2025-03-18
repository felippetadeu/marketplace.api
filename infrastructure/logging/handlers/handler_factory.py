from configuration import Configuration
from infrastructure.logging.handlers.abstract_handler import AbstractHandler
from infrastructure.logging.handlers.stream_handler import StreamHandler
from typing import List

class HandlerFactory:

    @staticmethod
    def get_handlers() -> List[AbstractHandler]:
        handlers = []
        console_settings: dict = Configuration.get_settings("logging.handlers")
        for i in console_settings:
            if i['class'] == 'StreamHandler':
                handlers.append(StreamHandler(i))
        return handlers