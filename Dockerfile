FROM python:3.12.0a4-slim-buster

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install django

#RUN python *.py