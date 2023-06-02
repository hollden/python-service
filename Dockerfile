FROM python:3.10.11-slim-buster

WORKDIR /app
ADD app/requirements.txt /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ADD app/service.py /app

CMD ["python3", "-u", "service.py"]
