# base image  
FROM python:3.12
# setup environment variable  

# where your code lives  
WORKDIR /

ARG DB_HOST=${DB_HOST}
ARG DB_NAME=${DB_NAME}
ARG DB_PASSWORD=${DB_PASSWORD}
ARG DB_PORT=${DB_PORT}
ARG DB_USER=${DB_USER}
ARG SECRET_KEY=${SECRET_KEY}

# set environment variables

ENV DB_HOST ${DB_HOST}
ENV DB_NAME ${DB_NAME}
ENV DB_PASSWORD ${DB_PASSWORD}
ENV DB_PORT ${DB_PORT}
ENV DB_USER ${DB_USER}
ENV SECRET_KEY ${SECRET_KEY}

RUN echo "DB_HOST=$DB_HOST" > .env
RUN echo "DB_NAME=$DB_NAME" >> .env
RUN echo "DB_PASSWORD=$DB_PASSWORD" >> .env
RUN echo "DB_PORT=$DB_PORT" >> .env
RUN echo "DB_USER=$DB_USER" >> .env
RUN echo "SECRET_KEY=$SECRET_KEY" >> .env

# install dependencies  
RUN pip install --upgrade pip  
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt  

COPY . /usr/src/app

EXPOSE 8000  
# start server  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]