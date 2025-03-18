from configuration import Configuration

@Configuration.app.get("/healthcheck", tags=["Health Check"])
def healthcheck():
    return {"status": "ok"}