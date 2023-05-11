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

Visit `http://localhost:{{ JUPYTER_PORT }}` in a web browser, using `{{JUPYTER_TOKEN}}` as the login if required.


