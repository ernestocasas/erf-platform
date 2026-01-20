from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field


class Destination(BaseModel):
    id: str
    name: str
    type: Literal["sip", "teams", "pbx", "pstn"] = "sip"
    address: str
    enabled: bool = True


class RouteRule(BaseModel):
    id: str
    name: str
    priority: int = Field(default=100, ge=0)
    match: dict = Field(default_factory=dict)
    action: dict = Field(default_factory=dict)
    enabled: bool = True


class ERFConfig(BaseModel):
    version: str = "1"
    node_id: str = "node-1"
    cluster_enabled: bool = False
    destinations: list[Destination] = Field(default_factory=list)
    rules: list[RouteRule] = Field(default_factory=list)
    metadata: Optional[dict] = None
