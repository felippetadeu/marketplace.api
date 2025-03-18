from configuration import Configuration
from infrastructure.logging.logger_factory import LoggerFactory
import logging

class Startup():

    async def run(self) -> None:
        api_controller = Configuration.get_env('API_CONTROLLER')
        consumer_name = Configuration.get_env('CONSUMER_NAME')

        logger = LoggerFactory.get_logger()
        await logger.log(f'API Controller: {api_controller}', logging.INFO)
        await logger.log(f'Consumer Name: {consumer_name}', logging.INFO)

        if api_controller is not None:
            await logger.log(f'Iniciando API Controller: {api_controller}', logging.INFO)
            from application.api.startup import Startup as APIStartup
            await APIStartup().run()
        elif consumer_name is not None:
            await logger.log(f'Iniciando Consumer Name: {consumer_name}', logging.INFO)
            import application.queue
        else:
            await logger.log('API Controller or Consumer Name not found in environment variables.', logging.ERROR)