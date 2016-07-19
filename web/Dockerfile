FROM python:2.7.12

ENV PYTHONUNBUFFERED 1

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

USER root
RUN mkdir -p /app/code && mkdir -p /app/support
RUN mkdir /root/.ptpython && touch /root/.ptpython/config.py

WORKDIR /app/code

RUN apt-get update -y && apt-get install apt-utils gettext -y

ADD ./code/requirements.txt /app/code/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /app/code/requirements.txt

ADD ./code /app/code/

# RUN /app/support/restore.sh
