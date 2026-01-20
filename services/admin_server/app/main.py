import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from erf_shared.logging import configure_json_logging
from erf_shared.settings import get_settings

settings = get_settings()
configure_json_logging(settings.service_name, settings.log_level)
log = logging.getLogger(__name__)

app = FastAPI(title="ERF Admin Server", version=settings.version)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": settings.service_name, "version": settings.version}


@app.get("/version")
def version() -> dict:
    return {"version": settings.version}


@app.get("/datasets")
def list_datasets() -> JSONResponse:
    """Placeholder endpoint.

    In the full ERF, this will return routing tables / number ranges / destination mappings.
    """
    log.info("list_datasets_called")
    return JSONResponse(status_code=501, content={"error": "not_implemented"})
