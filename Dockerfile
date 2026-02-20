FROM ubuntu:22.04

# install system dependencies
RUN zstd \
    apt update && apt install -y \
    curl \
    python3 \
    python3-pip \
    git \

# install ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

EXPOSE 11434


CMD ["ollama", "serve"]
