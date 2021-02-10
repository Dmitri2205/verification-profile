FROM python:3.8.2
ENV DEBIAN_FRONTEND="noninteractive"
ENV PYTHONPATH=.
WORKDIR /code
COPY ./back/requirements.txt ./
COPY ./back /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install default-libmysqlclient-dev && apt-get install build-essential
CMD ["python", "./service/app.py"]