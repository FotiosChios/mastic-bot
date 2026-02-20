FROM ubuntu:22.04

RUN apt update && apt install -y \
    curl \
    python3 \
    python3-pip \
    git \
    zstd

RUN curl -fsSL https://ollama.com/install.sh | sh

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD bash -c "ollama serve & python bot.py"