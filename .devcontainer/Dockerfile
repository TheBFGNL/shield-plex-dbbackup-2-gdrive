FROM mcr.microsoft.com/devcontainers/base:jammy

USER root
RUN apt update
RUN apt install -y dos2unix
RUN rm -rf /var/lib/apt/lists/*

USER vscode
ENV POETRY_VIRTUALENVS_IN_PROJECT true