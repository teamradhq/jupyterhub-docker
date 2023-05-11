import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['HUB_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['HUB_NETWORK_NAME']

# Admin Access
c.JupyterHub.admin_access = False
c.Authenticator.admin_users = set(os.environ['HUB_ADMIN_USER'])