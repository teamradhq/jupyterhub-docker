# Jupyter Hub Docker

This is a Docker Compose file to run Jupyter Hub with Docker Spawner.


---


## Access

This repository creates a single user Jupyter Lab. The Jupyter Lab server is accessible via a reverse
proxy (Traefik). 

### Jupyter Hub

Jupyter Hub should be accessible via a web browser at:

- `http://hub.docker.localhost`

You can also set `HUB_HOST` in `.env` to change this hostname as desired.


### Jupyter Lab

Jupyter Lab should be accessible via a web browser at:

- `http://jupyter.docker.localhost/lab`

Add `LAB_TOKEN` to `.env` and use this as the login.

You can also set `LAB_HOST` in `.env` to change this hostname as desired.


#### Traefik Admin

The Traefik Admin can be access at:

- `http://traefik.docker.localhost/`


---


## Setup


### Environment

Copy `.example.env` to `env` and edit the values to suit your needs. 

Create Docker Network:

```bash
docker network create hub_network
```

Run Docker Compose: 

```bash
docker compose up
docker compose down
docker compose build --no-cache
```




