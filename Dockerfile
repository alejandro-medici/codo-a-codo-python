FROM python:3.11.0a7-slim-buster

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install django

#RUN python *.py