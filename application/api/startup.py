from configuration import Configuration
from application.api.tags import tags_metadata
from infrastructure.logging.logger_factory import LoggerFactory
import pkgutil
import importlib
import logging
import uvicorn

class Startup:
    async def run(self) -> None:
        from fastapi import FastAPI
        api_controller = Configuration.get_env('API_CONTROLLER')
        tags = []
        if api_controller in tags_metadata:
            tags = tags_metadata[api_controller]
        app = FastAPI(openapi_tags=tags)
        Configuration.app = app
        await self.import_all_modules(f"application.api.common")

        if api_controller is not None:
            await self.import_all_modules(f"application.api.{api_controller}")

        config = uvicorn.Config(app)
        server = uvicorn.Server(config)
        await server.serve()

    async def import_all_modules(self, package_name: str) -> None:
        logger = LoggerFactory.get_logger()
        try:
            await logger.log(f"Importing all modules from {package_name}", logging.INFO)
            package = importlib.import_module(package_name)
            for _, module_name, _ in pkgutil.iter_modules(package.__path__):
                full_module_name = f"{package_name}.{module_name}"
                importlib.import_module(full_module_name)
        except ModuleNotFoundError as e:
            await logger.log(f"Error importing module {package_name}: {e}", logging.ERROR)
