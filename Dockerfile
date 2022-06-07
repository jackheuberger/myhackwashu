FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /registration

WORKDIR /registration

COPY . /registration/

RUN pip3 install -r requirements.txt

RUN sh restart-docker.sh
