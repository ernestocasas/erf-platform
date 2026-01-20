from __future__ import annotations

import logging

from fastapi import FastAPI

from shared.logging import configure_logging
from shared.settings import CommonSettings

settings = CommonSettings(service_name="cluster_manager")
configure_logging(settings.service_name, settings.log_level)
log = logging.getLogger(__name__)

app = FastAPI(title="ERF Cluster Manager", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": settings.service_name}


@app.get("/cluster/nodes")
def nodes() -> dict:
    """Placeholder cluster node list.

    Later: node discovery, heartbeat, sync status.
    """
    return {"nodes": []}
