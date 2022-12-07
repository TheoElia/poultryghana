# base image  
FROM python:3.7.5 
# setup environment variable  
ENV DockerHOME=/home/app/poultryghana

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

ADD requirements.txt $DockerHOME
# install dependencies  
RUN pip install --upgrade pip  
# run this command to install all dependencies 
RUN pip install -r requirements.txt  
# port where the Django app runs 
# copy whole project to your docker home directory. 
ADD . $DockerHOME  
 
 
EXPOSE 3000
# start server  

# CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]

# CMD python manage.py makemigrations;python manage.py migrate;python manage.py runserver
