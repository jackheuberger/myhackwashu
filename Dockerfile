FROM python:3.9

WORKDIR /registration

COPY requirements.txt /registration/

# install required packages
COPY . /registration/
RUN apt update
RUN DEBIAN_FRONTEND="noninteractive" apt install python3 python3-pip git -y

RUN pip3 install --upgrade setuptools pip
RUN pip install -r requirements.txt

RUN sh restart-docker.sh
