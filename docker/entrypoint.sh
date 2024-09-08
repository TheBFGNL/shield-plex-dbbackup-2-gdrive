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

gosu plexdb2gdrive poetry run plexdb2gdrive $@
