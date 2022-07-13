FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /registration

WORKDIR /registration

COPY . /registration/

RUN pip3 install -r requirements.txt

EXPOSE 8000 2222

ENTRYPOINT sh restart-docker.sh && python manage.py runserver 0.0.0.0:8000
