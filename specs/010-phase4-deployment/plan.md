# Phase 4 Deployment Implementation Plan

## Summary
Dockerize the FastAPI backend and NextJS frontend into two isolated containers and deploy them to an integrated standard local Minikube Kubernetes cluster. Networking will be securely restricted inside the cluster environment utilizing K8s DNS to tunnel all React proxied calls directly to the FastAPI container without traversing localhost NAT origin errors.

## Technical Context
The `backend` is a Python 3.12 FastAPI server running SQLModel and `fastmcp`. It integrates to an external Neon DB. The `frontend` is a standalone NextJS 15 React application relying on BetterAuth for session verification.

## Implementation Steps

1. **Dockerize**: Create multi-stage `Dockerfile`s in `phase4/frontend/` and `phase4/backend/` to ensure small and secure standalone container builds.
2. **K8s Manifests**: Write `deployment.yaml` and `service.yaml` abstractions (ClusterIP for backend, NodePort for frontend) in `phase4/k8s/`.
3. **Proxies/Networking**: Update Next.js `next.config.ts` to utilize internal Next.js rewrites, resolving `/api/*` endpoints securely to `http://backend-service:8000` via K8s DNS.
4. **Secret Injection**: Inject database keys (`CONNECTION_STRING`, `GOOGLE_API_KEY`) correctly through K8s mounted `Secret` specs to ensure the MCP tool execution context and generic server dependencies don't degrade to a mock local memory instance.

## Dependencies & Restrictions
- Requires local Minikube integration.
- Must ensure that sensitive credentials are kept entirely out of repository history using `.dockerignore` and cluster mapping.
