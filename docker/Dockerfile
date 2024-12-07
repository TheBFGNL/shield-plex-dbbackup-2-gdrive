FROM python:3.13

# RUN set -eux; \
# 	apt-get update; \
# 	apt-get install -y gosu; \
# 	rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash plexdb2gdrive

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1

RUN pip install poetry


WORKDIR /usr/src/app
# VOLUME [ "/appl/data" ]

COPY docker/entrypoint.sh .
COPY ./poetry.lock .
COPY ./pyproject.toml .
COPY ./README.md .
COPY ./shield_plex_dbbackup_2_gdrive ./shield_plex_dbbackup_2_gdrive

RUN poetry install

ENTRYPOINT [ "/bin/bash", "./entrypoint.sh" ]
