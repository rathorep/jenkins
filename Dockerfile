FROM python:3.6-alpine

COPY second.py /opt/

WORKDIR /opt

ENTRYPOINT ["python", "second.py"]