FROM python:latest

WORKDIR /app

COPY requisitos.txt .

RUN pip install --no-cache-dir -r requisitos.txt

#COPY servidor.py ./
#COPY conexao.py ./
#COPY conf_acesso.py ./
#COPY adminbn.db ./

EXPOSE 5000

CMD ["python", "servidor.py"]