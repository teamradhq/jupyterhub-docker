# Jupyter Hub Docker

This is a Docker Compose file to run Jupyter Hub with Docker Spawner.


---


## Access

This repository creates a Jupyter Hub installation. The Hub server is accessible via a reverse
proxy (Traefik). 

Jupyter Hub should be accessible via a web browser at:

- `http://hub.docker.localhost`

You can also set `HUB_HOST` in `.env` to change this hostname as desired. From here, you can login
and spawn a Jupyter Lab instance.

#### Traefik Admin

The Traefik Admin can be access at:

- `http://traefik.docker.localhost/`


---


## Setup


### Environment

Copy `.example.env` to `env` and edit the values to suit your needs.

#### Required Variables

There are a few environment variables that are required for the Jupyter Hub installation to work:

##### Host Data Directory

When a user launches a Lab server, its `work` directory will be linked to a directory on the host:

```bash
/{host_directory}/{username}
```

This requires a full local path for `HUB_HOST_DIR`. This directory should be within the project directory
and once configured, you should see this populated with users' notebook work directories. 

For example, if your root data directory is `/project/data` and you had users, `admin`, `tutor`, 
and `student`, you would see the following directories:

```bash
/project/data/admin
/project/data/student
/project/data/tutor
````


---


### Docker

#### Create Docker Network

A network will need to be configured for the Hub and Lab containers to communicate:

```bash
docker network create hub_network
```



#### Build Base Containers

Docker compose will build services from a collection of `base` images. In order for the project
to start up, these will need to be built locally:

```bash
docker build -t base-jupyter-hub -f base/hub/Dockerfile .
docker build -t base-jupyter-lab -f base/lab/Dockerfile .
```

These are located in `base/hub` and `base/lab` respectively.

When adding new features to a container, it is recommended to test these in the `hub/Dockerfile` and
`lab/Dockerfile` images respectively. These will rebuild much faster than the `base` images allowing 
you to test your changes faster. 

Once the desired change has been implemented successfully, you should integrate them with the appropriate
`base` image and rebuild it and the compose project.



#### Running Docker Compose: 

Before running the compose project, ensure you have completed the previous steps:

- [Environment](#environment)
- [Create Docker Network](#create-docker-network)
- [Build Base Containers](#build-base-containers)

If all of the above steps have been completed, you can run the compose project:

```bash
docker compose up
docker compose down
docker compose build --no-cache
```

When running `docker compose up` you'll see `lab` immediately shutdown, this is because its image 
is only required when a hub user launches their server.

To access hub:

- Visit [`http://hub.docker.localhost`](http://hub.docker.localhost) in your browser.
- Login with admin credentials.




