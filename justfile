set dotenv-load := true
VERSION := "1.0.0-rc-0"

# This list of available targets
default:
    @just --list

# Install the dependancies
install:
    #!/usr/bin/env bash
    [ -d venv ] || just venv
    source venv/bin/activate
    [ -f requirements.txt ] || just pip-compile
    just pip-sync
    pre-commit install --hook-type pre-commit --hook-type commit-msg

# Create Python virtual environment
venv:
    #!/usr/bin/env bash
    python3.11 -m venv venv --prompt bowls
    source venv/bin/activate
    python3 -m pip install pip-tools
    just install

# https://github.com/jazzband/pip-tools#updating-requirements
#     just pip-upgrade --upgrade-package "cryptography>=41.0.6"
# Upgrade a pip package
pip-upgrade package:
    CUSTOM_COMPILE_COMMAND="just pip-compile" python3 -m piptools compile \
        --upgrade-package '{{package}}' \
        --extra dev --resolver=backtracking -o requirements.txt pyproject.toml
    CUSTOM_COMPILE_COMMAND="just pip-compile" python3 -m piptools compile \
        --upgrade-package '{{package}}' \
        --resolver=backtracking -o requirements.production.txt pyproject.toml  requirements-prod-constraint.in

# Compile the production and dev requirements.txt files
pip-compile:
    CUSTOM_COMPILE_COMMAND="just pip-compile" python3 -m piptools compile \
        --extra dev --resolver=backtracking -o requirements.txt pyproject.toml
    CUSTOM_COMPILE_COMMAND="just pip-compile" python3 -m piptools compile \
        --resolver=backtracking -o requirements.production.txt pyproject.toml requirements-prod-constraint.in

# Add/remove packages based on current requirements.txt
pip-sync:
    #!/usr/bin/env bash
    [ -d venv ] || just venv
    source venv/bin/activate
    pip-sync requirements.txt

# Uninstall the python packages
uninstall_pip:
    #!/usr/bin/env bash
    [ -d venv ] || just venv
    source venv/bin/activate
    pip uninstall -y -r <(pip freeze)

# Build the docker image
build:
    docker build -f Dockerfile \
    --label "org.opencontainers.image.revision"="{{VERSION}}" \
    -t bowls:latest \
    -t bowls:{{VERSION}} \
    .

# Run the bump2version command, build will increment the release candidate
# Use 'bump3version <part> --commit' where part is either MAJOR, MINOR, or PATCH
bumpversion +options="build":
    bump2version {{options}}

# Start new develpment cycle with new patch and release candidate
patch_version +options="":
    bump2version patch {{options}} --commit
    git push

# Bump the version for a release. Make tag and commit
release_version +options="":
    bump2version release {{options}} --tag --commit
    git push && git push --tags

# Setup the database
db_install:
    #!/usr/bin/env bash
    just db_permissions
    just db_timezone
    python ./manage.py migrate
    echo "Remove conflicting data"
    echo "DELETE FROM ava_configuration;" | python ./manage.py dbshell
    echo "Loading initial data"
    just db_load

# Set user permissions on database
db_permissions:
    #!/usr/bin/env bash
    echo "Grant permissions to databases"
    [ -z "${DB_PASSWORD}" ] && DB_PASSWORD=${DJANGO_DATABASE_PASSWORD}
    echo "GRANT ALL ON ${DJANGO_DATABASE_NAME:-bowls} . * TO '${DJANGO_DATABASE_USER:-bowls}'@'%';" | mysql -h ${DJANGO_DATABASE_HOST} -u root -p${DB_PASSWORD}
    echo "GRANT ALL ON ${DJANGO_TEST_DATABASE_NAME:-test_db} . * TO '${DJANGO_DATABASE_USER:-bowls}'@'%';" | mysql -h ${DJANGO_DATABASE_HOST} -u root -p${DB_PASSWORD}
    echo "GRANT ALL ON \`${DJANGO_DATABASE_NAME:-bowls}%\` . * TO '${DJANGO_DATABASE_USER:-bowls}'@'%';" | mysql -h ${DJANGO_DATABASE_HOST} -u root -p${DB_PASSWORD}
    echo "GRANT ALL ON \`${DJANGO_TEST_DATABASE_NAME:-test_db}%\` . * TO '${DJANGO_DATABASE_USER:-bowls}'@'%';" | mysql -h ${DJANGO_DATABASE_HOST} -u root -p${DB_PASSWORD}

# Drop and recreate the database
db_reset:
    #!/usr/bin/env bash
    [ -z "${DB_PASSWORD}" ] && DB_PASSWORD=${DJANGO_DATABASE_PASSWORD}
    echo "Dropping database..."
    echo "DROP DATABASE IF EXISTS ${DJANGO_DATABASE_NAME:-bowls};" | mysql -h ${DJANGO_DATABASE_HOST} -u root -p${DB_PASSWORD}
    echo "CREATE DATABASE ${DJANGO_DATABASE_NAME:-bowls};" | mysql -h ${DJANGO_DATABASE_HOST} -u root -p${DB_PASSWORD}
    echo "ALTER DATABASE ${DJANGO_DATABASE_NAME:-bowls} CHARACTER SET 'utf8mb3' COLLATE 'utf8mb3_general_ci';" | mysql -h ${DJANGO_DATABASE_HOST} -u root -p${DB_PASSWORD}
    echo "DROP USER IF EXISTS ${DJANGO_DATABASE_USER:-bowls};" | mysql -h ${DJANGO_DATABASE_HOST} -u root -p${DB_PASSWORD}
    echo "CREATE USER ${DJANGO_DATABASE_USER:-bowls} IDENTIFIED BY '${DJANGO_DATABASE_PASSWORD}';" | mysql -h ${DJANGO_DATABASE_HOST} -u root -p${DB_PASSWORD}
    just db_permissions

# Load the tzinfo files into MySQL
db_timezone:
    #!/usr/bin/env bash
    [ -z "${DB_PASSWORD}" ] && DB_PASSWORD=${DJANGO_DATABASE_PASSWORD}
    zcat ./tools/tzinfo.sql.gz | mysql -h ${DJANGO_DATABASE_HOST} -u root -p${DB_PASSWORD} mysql
