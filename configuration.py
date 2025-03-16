import os
import orjson

from typing import Any
from fastapi import FastAPI

class Configuration():

    settings: dict = None
    app: FastAPI = None

    @staticmethod
    def get_env(environment: str = 'PYTHON_ENVIRONMENT'):
        return os.getenv(environment, None)
    
    @staticmethod
    def set_env(environment: str = 'PYTHON_ENVIRONMENT', value: Any = None):
        os[environment] = value
        
    @staticmethod
    def load_settings():
        settings_file_name: str = f'settings.{Configuration.get_env()}.json'
        data = None
        with open(settings_file_name, 'r', encoding='utf-8') as file:
            data = file.read()

        Configuration.settings = orjson.loads(data)

    @staticmethod
    def get_settings(key: str, default=None):
        keys = key.split(".")
        if Configuration.settings is None:
            Configuration.load_settings()
        value = Configuration.settings
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
            if value is None:
                return default
        return value