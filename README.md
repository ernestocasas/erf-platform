# Educronix ERF Platform (Scaffold)

This repository contains the initial **scaffolding** for the **Educronix REST Routing Framework (ERF)**.

The goal of this baseline is to establish a clean monorepo structure, service boundaries, configuration patterns,
logging conventions, CI, and health endpoints. **Production routing logic is intentionally not implemented yet.**

## Repository layout

```
services/
  routing_server/
  admin_server/
packages/
  shared/
  config_engine/
  cluster_manager/
tests/
```

## Components

- **Routing Server** (`services/routing_server`): SBC-facing REST routing service.
- **Admin Server** (`services/admin_server`): Admin API for managing datasets/config (placeholder).
- **Config Engine** (`packages/config_engine`): configuration loading + validation hooks.
- **Cluster Manager** (`packages/cluster_manager`): clustering/synchronization primitives (placeholder).
- **Shared** (`packages/shared`): logging + settings used by all services.

## Quick start

### Local (venv)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Routing server (port 8000)
uvicorn services.routing_server.app.main:app --reload --port 8000

# Admin server (port 8001)
uvicorn services.admin_server.app.main:app --reload --port 8001
```

Or run both:

```bash
./run_local.sh
```

### Docker

```bash
docker compose up --build
```

## Endpoints

- Routing: `GET /health`, `GET /version`, `POST /route` (placeholder)
- Admin: `GET /health`, `GET /datasets` (placeholder)

## Next steps

1. Add ERF data models (tenants, numbers, destinations, rules)
2. Implement dataset persistence (file-based first, then database)
3. Add cluster sync (peer replication + conflict handling)
4. Add SBC adapters (AudioCodes, Ribbon, Oracle, Ingate)
