from dataclasses import dataclass


@dataclass(frozen=True)
class NodeIdentity:
    node_id: str
    role: str = "member"  # member|leader|standby etc.
