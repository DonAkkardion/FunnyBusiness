# pull the official base image
FROM python:3.10.0

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy django.sh
COPY ./django.sh /usr/local/bin/django.sh
# 
RUN chmod +x /usr/local/bin/django.sh
# 
CMD ["django.sh"]