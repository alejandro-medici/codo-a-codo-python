FROM python:3

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install django

#RUN python *.py