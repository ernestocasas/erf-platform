from dataclasses import dataclass


@dataclass(frozen=True)
class Peer:
    name: str
    base_url: str
