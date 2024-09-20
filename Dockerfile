FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY . /app

RUN sudo apt-get update && \
    sudo apt-get upgrade && \
    sudo apt install openslide-tools python3-openslide
RUN uv pip install --system --no-cache .
