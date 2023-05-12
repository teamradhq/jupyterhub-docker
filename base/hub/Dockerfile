FROM jupyterhub/jupyterhub:latest

# Update the package list and install necessary packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y passwd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install \
    dockerspawner