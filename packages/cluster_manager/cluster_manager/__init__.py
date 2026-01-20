"""Cluster manager (scaffold).

Future responsibilities:
- peer discovery / configuration
- active/active replication and conflict resolution
- health & failover coordination
"""

from .peers import Peer, PeerRegistry

__all__ = ["Peer", "PeerRegistry"]
