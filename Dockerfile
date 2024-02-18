ARG PYTHON_VERSION=3.11
FROM python:$PYTHON_VERSION as builder

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
    build-essential gcc cmake git \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/var/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv $VIRTUAL_ENV

WORKDIR /var/app

# Install Python packages
RUN python3 -m pip install --no-cache --upgrade pip wheel setuptools
COPY requirements.production.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY app/ /var/app

ARG DJANGO_SETTINGS_MODULE config.settings.production
ARG DJANGO_SECRET_KEY=${RANDOM}
RUN python manage.py collectstatic --noinput --no-color

## ------------------------------------------------------------------
## Build the devcontainer image
## - install the development and testing packages
## - change entry point to use debugpy and runserver
## ------------------------------------------------------------------
FROM builder as devcontainer

ENV VIRTUAL_ENV=/var/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

# Create and use non-root user and install sudo
RUN groupadd --force --gid 1000 bowls \
    && useradd --uid 1000 --gid 1000 --home-dir /var/tmp/bowls bowls \
    && mkdir -p /var/tmp/bowls \
    && apt-get update \
    && apt-get install -y sudo postgresql-client vim bash-completion curl \
    && echo bowls ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/bowls \
    && chmod 0440 /etc/sudoers.d/bowls \
    && curl -o /etc/bash_completion.d/git-completion 'https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash' \
    && echo 'source /etc/bash_completion.d/git-completion' >>/var/tmp/bowls/.bashrc \
    && curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin

USER bowls
WORKDIR /var/app

EXPOSE 8000 9000
ENTRYPOINT ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "/var/app/manage.py", "runserver", "0.0.0.0:8000"]


## ------------------------------------------------------------------
FROM python:$PYTHON_VERSION as production

COPY --from=builder /var/venv /var/venv
COPY --from=builder /var/app /var/app

ENV DJANGO_SETTINGS_MODULE config.settings.production
ENV VIRTUAL_ENV=/var/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create and use non-root user
RUN groupadd --force --gid 1000 bowls \
    && useradd --uid 1000 --gid 1000 --no-create-home bowls

# Run the app as a non-root user.
# Note that the source files are NOT owned by the application user.
USER bowls
WORKDIR /var/app

EXPOSE 8000
ENTRYPOINT ["gunicorn", "bowls:wsgi", "-w", "2", "--threads", "2", "-b", "0.0.0.0:8000"]
