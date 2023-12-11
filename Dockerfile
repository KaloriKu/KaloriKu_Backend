# base image  
FROM python:3.12   
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

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

# copy whole project to your docker home directory. 
COPY . $DockerHOME  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver 