I have created basic dockerfile 

FROM python:3.9-slim  #Platform/Environment
WORKDIR /app #working directory
COPY . .  #copy all the files in working directory
RUN pip install requirements.txt  #install all dependency
CMD ["python", "app.py"]  #run app

###################################################
Make build image of flask app
docker build -t flask-app .  # where -t is a tag name for image and "dot" is means looking for current directory

###################################################

Run on Container
docker run -d --name flask-app-container -p 5000:5000 flask-app  

# "-d" flag means detach mode where you can run image silently, and 5000:5000 (first one is host port and second one is internal port)