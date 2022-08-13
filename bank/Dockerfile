FROM python:3.10.1

RUN mkdir -p /django_app
WORKDIR /django_app
COPY . /django_app
RUN pip3 install -r /django_app/requirements.txt; exit 0
EXPOSE 8000