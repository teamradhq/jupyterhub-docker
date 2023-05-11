FROM jupyterhub/jupyterhub:latest

COPY jupyterhub_config.py .

# Update the package list and install necessary packages
#RUN apt-get update && \
#    apt-get install -y passwd

RUN apt-get install -y passwd

# Create the new user and set the password
ARG HUB_ADMIN_USER
ARG HUB_ADMIN_PASSWORD
RUN useradd -m ${HUB_ADMIN_USER} && \
    echo "${HUB_ADMIN_USER}:${HUB_ADMIN_PASSWORD}" | chpasswd

RUN pip install \
    dockerspawner==0.10.0
