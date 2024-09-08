#!/bin/sh
set -e

# use the specified UID for the user
UID="${UID:-1000}"

# use the specified GID for the user
GID="${GID:-1000}"

usermod -u "${UID}" plexdb2gdrive
groupmod -g "${GID}" plexdb2gdrive

chown -R plexdb2gdrive:plexdb2gdrive /usr/src/app
chown -R plexdb2gdrive:plexdb2gdrive /appl/data

su plexdb2gdrive -c "poetry run plexdb2gdrive ${@}"

