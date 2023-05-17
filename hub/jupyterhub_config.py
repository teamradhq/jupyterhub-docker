import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['HUB_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['HUB_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# Admin Access
c.JupyterHub.admin_access = True
c.Authenticator.delete_invalid_users = True
c.Authenticator.admin_users = {'admin'}

# Persistent Storage
host_dir = os.environ['HUB_HOST_DIR'] + '/{username}'
notebook_dir = '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { host_dir: notebook_dir }
