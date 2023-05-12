FROM base-jupyter-hub

COPY jupyterhub_config.py .

# Create the new user and set the password
ARG HUB_ADMIN_USER
ARG HUB_ADMIN_PASSWORD
RUN useradd -m ${HUB_ADMIN_USER} && \
    echo "${HUB_ADMIN_USER}:${HUB_ADMIN_PASSWORD}" | chpasswd


CMD ["jupyterhub"]
