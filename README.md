# Flask Telegram Bot Application

This document describes a Flask-based web application that uses the Telegram Bot API to send messages to a Telegram channel. The application uses Jinja2 to render HTML messages, and it is deployed using Docker and Gunicorn.

## Application Structure
The application has the following structure:

```
├── app.py
├── config (User mounted configuration folder)
│   └── config.py
├── Dockerfile
├── requirements.txt
├── config.py (This is just a template)
├── templates
│   ├── example.html
│   ├── movie.html
│   └── series.html
└── README.md
```

### config
You need to edit the config.py, with your own BOT TOKEN and your channel id, put it in a config folder, and mount it to docker as Run section below.

### templates
You can configure your own template, just edit the html in templates folder.


## Setup and Deployment

### Build
In the main directory, execute the following command
```
docker build -t my-flask-app .
```
Replace my-flask-app with a name that suits your project.

### Run
Run the Docker container by executing the following command:

```
docker run -d -p 8099:8099 -v /path/to/config:/app/config --name my-flask-app-container my-flask-app
```
Replace /path/to/config with the path to the user's config folder on the host system, and my-flask-app-container with a name that suits your project.

## Usage
In the emby, install the webhooks plug-in if not already. In the webhooks URL section put 
```
your.server.ip.address:8099/webhook
```
Remeber check for Library in the event section.

## Troubleshooting
If you encounter any issues while deploying or running the application, you can debug by checking the Docker container logs or running the container interactively.

### Check the logs of the container:
```
docker logs my-flask-app-container
```
Replace my-flask-app-container with the name of your container.

### Run the container interactively:
```
docker run -it --rm -p 8099:8099 -v /path/to/config:/app/config --entrypoint /bin/bash my-flask-app
```
Replace /path/to/config with the path to the user's config folder on the host system, and my-flask-app with the name of your Docker image.

## Credit
[ChatGPT](https://chat.openai.com/)
