import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from erf_shared.logging import configure_json_logging
from erf_shared.settings import get_settings

settings = get_settings()
configure_json_logging(settings.service_name, settings.log_level)
log = logging.getLogger(__name__)

app = FastAPI(title="ERF Routing Server", version=settings.version)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": settings.service_name, "version": settings.version}


@app.get("/version")
def version() -> dict:
    return {"version": settings.version}


@app.post("/route")
def route(payload: dict) -> JSONResponse:
    """Placeholder routing endpoint.

    In the full ERF, this will:
    - validate tenant
    - look up number ranges / routing tables
    - apply rule engine
    - return destination (SBC next hop) or action
    """
    log.info("route_request_received", extra={"payload_keys": list(payload.keys())})
    return JSONResponse(
        status_code=501,
        content={
            "error": "not_implemented",
            "message": "Routing logic not implemented yet. This is scaffolding.",
        },
    )
