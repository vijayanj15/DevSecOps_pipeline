STREAMING_CHUNK:Setting the base image...

Use an official, minimal Python runtime to reduce the attack surface

FROM python:3.9-slim

STREAMING_CHUNK:Configuring the working directory...

Set the working directory in the container

WORKDIR /app

Copy the current directory contents into the container

COPY . .

STREAMING_CHUNK:Installing dependencies...

Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

Make port 5000 available to the world outside this container

EXPOSE 5000

STREAMING_CHUNK:Defining the run command...

Run app.py when the container launches

CMD ["python", "app.py"]