# Velonx12 MAX‑ROI Release

This package bundles everything you need to **run the Velonx12 high‑frequency trading stack in production**.

* **Docker** image references ready for `k3d`/`k3s` clusters.
* **Helm chart** (`chart/velonx12`) for repeatable Kubernetes installs.
* Updated `deploy_maxroi.sh` that:
  * Ensures Docker/K3d are installed
  * Creates (or reuses) a `velonx12` cluster
  * Installs/updates the helm release

## Quick start on your VPS

```bash
# copy files to the VPS and extract
scp velonx12_maxroi_release.zip root@209.54.107.102:/root/
ssh root@209.54.107.102
unzip velonx12_maxroi_release.zip -d velonx12
cd velonx12
bash scripts/deploy_maxroi.sh
```

Within ~2 minutes you’ll have the core services reachable inside the cluster:

```bash
k3d kubeconfig merge velonx12 --switch
kubectl get pods -n velonx12
```

## Local testing

```bash
docker compose up
```

> **Tip:** Use the provided `docker-compose.override.yml` to toggle between paper‑trading and live modes.

---

© 2025 Velonx12 Project