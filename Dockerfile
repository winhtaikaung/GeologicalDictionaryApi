#FROM ubuntu:14.04
FROM python:2.7
MAINTAINER winhtaikaung(winhtaikaung28@hotmail.com)

RUN apt-get update
RUN apt-get install varnish -y 
COPY geo_dict_cache_config.vcl /etc/varnish/
# Install basic packages
#RUN apt-get -qq -y install git curl build-essential openssl libssl-dev python-software-properties g++ make 

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app
COPY run.sh /usr/src/app/
EXPOSE 3000

CMD service varnish restart

CMD sh /usr/src/app/run.sh 
