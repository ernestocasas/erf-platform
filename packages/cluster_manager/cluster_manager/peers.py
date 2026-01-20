from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class Peer:
    name: str
    base_url: str


class PeerRegistry:
    """In-memory peer registry (scaffold)."""

    def __init__(self) -> None:
        self._peers: Dict[str, Peer] = {}

    def add(self, peer: Peer) -> None:
        self._peers[peer.name] = peer

    def list(self) -> List[Peer]:
        return list(self._peers.values())
