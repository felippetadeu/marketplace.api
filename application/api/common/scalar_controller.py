from configuration import Configuration
from scalar_fastapi import get_scalar_api_reference

@Configuration.app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=Configuration.app.openapi_url,
        title=Configuration.app.title
    )