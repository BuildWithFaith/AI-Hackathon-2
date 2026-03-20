# 010 Phase 4 Deployment Tasks

## Phase 1: Dockerization
- [x] T001 [P] Verify Docker daemon is running locally
- [x] T002 Implement backend multi-stage `Dockerfile` and `.dockerignore`
- [x] T003 Implement frontend standalone `Dockerfile` and `.dockerignore`

## Phase 2: Kubernetes Manifests
- [x] T004 [P] Ensure Minikube cluster is active
- [x] T005 Implement `backend-deployment.yaml` and `backend-service.yaml`
- [x] T006 Implement `frontend-deployment.yaml` and `frontend-service.yaml`
- [x] T007 Implement Secrets and ConfigMaps for environment variables

## Phase 3: Networking and Verification
- [x] T008 [P] Test internal DNS routing manually inside pod
- [x] T009 Update `next.config.ts` to implement API proxying directly to backend-service
- [x] T010 Update MCP server `add_task` to handle environment variables gracefully
