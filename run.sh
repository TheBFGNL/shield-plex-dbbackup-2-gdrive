#!/bin/sh

docker run -v ${LOCAL_WORKSPACE_FOLDER}/data/gdrive_service_account.json:/appl/data/gdrive_service_account.json -it --rm --env-file .docker_env plexdb2gdrive "-m copy2gdrive"
