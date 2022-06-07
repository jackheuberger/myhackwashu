FROM python:3.9

WORKDIR /registration

COPY requirements.txt /registration/

# install required packages
COPY . /registration/
RUN mkdir /etc/nginx & mkdir /etc/nginx/sites-available & mv nginx.conf /etc/nginx/sites-available/default
RUN apt update
RUN DEBIAN_FRONTEND="noninteractive" apt install python3 python3-pip nginx git -y
RUN pip3 install --upgrade setuptools pip
RUN pip install -r requirements.txt


RUN sh restart-docker.sh

RUN nginx -s reload
