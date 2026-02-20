COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD bash -c "ollama serve & python bot.py"