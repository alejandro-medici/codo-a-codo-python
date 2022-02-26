FROM python:3.10.2-slim-buster

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install django

#RUN python *.py