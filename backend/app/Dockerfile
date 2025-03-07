FROM python:3.10-slim
WORKDIR /backend

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /backend

# Set the FLASK_APP environment variable 
# This is where you tell Flask which file to use as the entry point for your application
ENV FLASK_APP=endpoints.py 

EXPOSE $API_DOCKER_PORT

CMD ["flask", "run", "--host=0.0.0.0"] 
# The --host=0.0.0.0 option makes Flask listen on any other network the container is connected to. 
# This is necessary for Docker to map the port correctly from the container to your host machine.