FROM base-jupyter-hub

COPY jupyterhub_config.py .

# Create hub user accounts
COPY users.txt /tmp/users.txt

RUN while IFS=: read -r username password; do \
        useradd -m "$username" -p "$(openssl passwd -1 "$password")"; \
    done < /tmp/users.txt && \
    rm /tmp/users.txt

CMD ["jupyterhub"]
