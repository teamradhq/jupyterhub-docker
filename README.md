# Jupyter Hub Docker

This is a Docker Compose file to run Jupyter Hub with Docker Spawner.


---


## Overview

This repository creates a single user Jupyter Lab. The Jupyter Lab server is accessible via a reverse
proxy (Traefik). 


### Jupyter Lab

Jupyter Lab should be accessible via a web browser at:

- `http://jupyter.docker.localhost/lab`

Add `{{JUPYTER_TOKEN}}` to `.env` and use this as the login.

You can also set `JUPYTER_LAB_HOST` in `.env` to change the hostname as desired.


#### Traefik Admin

The Traefik Admin can be access at:

- `http://traefik.docker.localhost/`


---


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

