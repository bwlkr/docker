FROM python:3.7.2-alpine3.9

WORKDIR /aio

COPY server.py /aio
COPY requirements.txt /aio

RUN pip install -r requirements.txt

EXPOSE 8888

CMD [ "python", "-u", "server.py"]
