FROM python:latest

RUN pip install requests

WORKDIR /app

COPY . .

CMD ["python", "hello.py"]
