from __future__ import annotations

from enum import Enum


class NodeRole(str, Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    ACTIVE = "active"
    STANDBY = "standby"
