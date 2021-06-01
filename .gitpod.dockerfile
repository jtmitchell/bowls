FROM gitpod/workspace-postgres

# Install redis
RUN sudo apt-get update && \
    sudo apt-get install -y \
    redis-server \
    && sudo rm -rf /var/lib/apt/lists/*