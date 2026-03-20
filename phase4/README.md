# Phase 4 Walkthrough: Local Kubernetes Deployment

Phase 4 of the Todo Application project focused on containerizing the application and executing it locally using a Minikube cluster.

## Accomplishments

### 1. Dockerization
- Created a [Dockerfile](file:///Users/mac/Desktop/hackathon2/phase4/backend/Dockerfile) for the Next.js `frontend` optimized for production using a multi-stage standalone build.
- Created a multi-stage [Dockerfile](file:///Users/mac/Desktop/hackathon2/phase4/backend/Dockerfile) for the FastAPI `backend` which fetches dependencies safely via `uv`.
- Configured [.dockerignore](file:///Users/mac/Desktop/hackathon2/phase4/backend/.dockerignore) files for both context directories to reduce image bloatedness.

### 2. Kubernetes Configuration Setup
A `k8s` directory was added with explicit, robust manifests for full application setup:
- [backend-deployment.yaml](file:///Users/mac/Desktop/hackathon2/phase4/k8s/backend-deployment.yaml) and [backend-service.yaml](file:///Users/mac/Desktop/hackathon2/phase4/k8s/backend-service.yaml) (ClusterIP).
- [frontend-deployment.yaml](file:///Users/mac/Desktop/hackathon2/phase4/k8s/frontend-deployment.yaml) and [frontend-service.yaml](file:///Users/mac/Desktop/hackathon2/phase4/k8s/frontend-service.yaml) (NodePort to expose it securely to the host).
- [frontend-config.yaml](file:///Users/mac/Desktop/hackathon2/phase4/k8s/frontend-config.yaml) to route internal service requests across namespaces seamlessly (`backend-service.default.svc.cluster.local`).

### 3. Minikube Execution
- Initialized Docker Desktop on MacOS.
- Started the `minikube` cluster using the `docker` driver.
- Configured the Docker daemon scope to target Minikube (`eval $(minikube docker-env)`) allowing the images to be cached perfectly within the deployment context.
- Safely exported environment variables (e.g. `DATABASE_URL`, `OPENAI_API_KEY`) safely directly to Kubernetes via `kubectl create secret`.

## Validation & Verification
After launching [.yaml](file:///Users/mac/Desktop/hackathon2/phase4/frontend/pnpm-lock.yaml) manifests to the control plane, all pods spun up successfully cleanly:
- **Backend Logs**: The database engine verified schemas (`user`, `task`, `conversation`, `message`) over an external Neondb without connectivity errors.
- **Frontend Logs**: The Next.js 16.2.0 server started without fatal build errors and responds proactively.

## Next Steps
To explore the deployed app locally through Minikube in your browser, perform the following in your terminal:
```bash
minikube service frontend-service
```
This action automatically opens the proper allocated internal port safely in your browser.
