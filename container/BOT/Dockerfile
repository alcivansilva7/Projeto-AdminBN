FROM python:latest

WORKDIR /app

COPY requisitos.txt .

RUN pip install --no-cache-dir -r requisitos.txt

#COPY bot.py ./

EXPOSE 5000

CMD ["python", "bot.py"]