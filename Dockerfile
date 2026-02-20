FROM ubuntu:22.04

RUN apt update && apt install -y \
    curl \
    python3 \
    python3-pip \
    git \
    zstd

RUN curl -fsSL https://ollama.com/install.sh | sh

ENV OLLAMA_HOST=0.0.0.0

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN ollama serve & sleep 5 && ollama pull qwen2.5:7b

CMD bash -c "ollama serve & python3 bot.py"