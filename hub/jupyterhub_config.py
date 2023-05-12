import os
import sys
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['HUB_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['HUB_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# Admin Access
c.JupyterHub.admin_access = False
c.Authenticator.delete_invalid_users = True
# c.Authenticator.admin_users = {os.environ['HUB_ADMIN_USER']}

# Persistent Storage
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyter-data-{username}': notebook_dir }
