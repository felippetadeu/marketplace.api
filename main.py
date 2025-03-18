from application.startup import Startup
import asyncio

if __name__ == '__main__':
    asyncio.run(Startup().run())
    #asyncio.create_task(Startup().run())