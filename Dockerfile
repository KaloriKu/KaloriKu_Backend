# base image  
FROM python:3.12-alpine
# setup environment variable  

# where your code lives  
WORKDIR /usr/src/app

ARG DB_HOST
ARG DB_NAME
ARG DB_PASSWORD
ARG DB_PORT
ARG DB_USER
ARG SECRET_KEY

# set environment variables  
ENV DB_HOST ${DB_HOST}
ENV DB_NAME ${DB_NAME}
ENV DB_PASSWORD ${DB_PASSWORD}
ENV DB_PORT ${DB_PORT}
ENV DB_USER ${DB_USER}
ENV SECRET_KEY ${SECRET_KEY}

# install dependencies  
RUN pip install --upgrade pip  
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt  

COPY . /usr/src/app

EXPOSE 8000  
# start server  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]