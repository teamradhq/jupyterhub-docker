# Jupyter Hub Docker

This is a Docker Compose file to run Jupyter Hub with Docker Spawner.


## Setup

### Environment

Copy `.example.env` to `env` and edit the values to suit your needs. 

Run Docker Compose: 

```bash
docker compose up
docker compose down
docker compose build --no-cache
```

### Access 

#### Access Jupyter Lab

Jupyter Lab should be accessible via a web browser at:

- `http://jupyter.docker.localhost:{{JUPYTER_PORT}}/lab`
- `http://localhost:{{JUPYTER_PORT}}/lab`

Use`{{JUPYTER_TOKEN}}` as the login if required.

#### Access Traefik Admin

The Traefik Admin can be access at:

- `http://traefik.docker.localhost/`

