FROM python:3.13

RUN useradd -ms /bin/bash plexdb2gdrive

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1

RUN pip install poetry

WORKDIR /usr/src/app

COPY docker/entrypoint.sh .
COPY ./poetry.lock .
COPY ./pyproject.toml .
COPY ./README.md .
COPY ./shield_plex_dbbackup_2_gdrive ./shield_plex_dbbackup_2_gdrive

RUN poetry install --without dev

ENTRYPOINT [ "/bin/bash", "./entrypoint.sh" ]
