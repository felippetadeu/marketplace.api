from fastapi import APIRouter
from configuration import Configuration

@Configuration.app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}