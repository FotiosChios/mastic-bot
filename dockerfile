FROM ubuntu:22.04

RUN apt update && apt install -y curl python3 python3-pip git

RUN curl -fsSL https://ollama.com/install.sh | sh

EXPOSE 11434

CMD ["ollama", "serve"]