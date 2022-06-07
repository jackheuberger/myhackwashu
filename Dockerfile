FROM python:3.9

WORKDIR /registration

COPY requirements.txt /registration/

# install required packages
COPY . /registration/

RUN pip3 install --upgrade setuptools pip
RUN pip install -r requirements.txt

RUN sh restart-docker.sh
