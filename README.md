# SLC Python Meetup (July 2024): How to Containerize a Python Application 
#### July 10, 2024
#### Presenter: David Gardner

## Overview
This talk will explain what Docker is, why developers would want to containerize their Python application, and then demonstrate how to dockerize two simple Python applications: 
- a terminal-based random movie picker 
- a FastAPI server that returns json 

## Talk Slides
https://docs.google.com/presentation/d/1N2zL_QdybmDZHZExydKP7ida5qZIqDF9Sz9X9WS69WA/edit?usp=sharing 

## Demo

### Pre-requisites
1. Install Docker Desktop (if installed)
2. Install Python 3 (if not installed)
3. clone the `July-2024-Docker-Meetup` repo to your machine


### Demo1: Containerize a random movie picker python app
1. cd into `example1` directory
2. set up a Python env running Python 3.9: `python3.9 -m venv .venv`
(if you don't have python 3.9 already installed on your machine, you'll need to install it using your preferred package manager. I use homebrew, so I ran: `brew install python@3.9`)
3. activate the new virtual env: `. .venv/bin/activate` 
4. confirm the Python version is 3.9: `python --version` 
5. install the required packages into your virtual env: `pip install requests bs4` 
6. play around with the "movie picker app" to get familiar with how it works: `python main.py`
7. containerize this movie picker app using: `docker build -t random-movie-picker .` (`-t` parameter gives the container image a tag of "random-movie-picker", making it easier to identify)
8. run the newly containerized app: `docker run -i -t random-movie-picker` ( `-i` parameter ensures the running container interactive while the `-t` parameter creates a pseudo-terminal connection to the Docker container)
9. Done! The movie picker app is now running inside a Docker container. 
10. clean up by hitting `command-C` to stop the container and typing `deactivate` to end the virtual env python session

### Demo2: Containerize a FastAPI python service 
1. cd into the `example2` directory
2. set up a Python env running Python 3.12: `python3.12 -m venv .venv`
(if you don't have python 3.9 already installed on your machine, you'll need to install it using your preferred package manager. I use homebrew, so I ran: `brew install python@3.12`)
3. activate the new virtual env: `. .venv/bin/activate` 
4. confirm the Python version is 3.12: `python --version` 
5. install the fastAPI and uvicorn packages into your virtual env: `pip install fastapi uvicorn`
6. in the root directory, start the uvicorn server to understand how it works: `uvicorn app.main:app`. Open the link where Uvicorn is running: `127.0.0.1:8000` and check the HTTP responses from `/`, `/docs`, and `/items/foobar` 
7. run `pip freeze --local > requirements.txt` to generate the required packages file
8. containerize the api service: `docker build -t fastapi-demo .` 
9. run the containerized api service: `docker run -p 8000:8000 fastapi-demo` (`-p 8000:8000` tells docker to expose the local port 8000 to the container's port 8000) 
10. open `0.0.0.0:8000/` on your browser (`localhost:8000/` should work too) and interact with the service. Sending the `localhost:8000/items/foobar` should return `{"item": "foobar"}` 
11. Done! The api service is running inside a Docker container. You can view the running containers on the "Docker Desktop > Containers" page
12. clean up by hitting `command-C` to stop the container and typing `deactivate` to end the virtual env python session

### Notes
I didn't cover the `.dockerignore` file, but basically it works just like a `.gitignore` file, except it tells Docker what to ignore when copying files from the local "source" directory (`.`) into the docker image "working" directory.

### DG: Remaining steps
- [x] add .gitignore file 
- [x] Skipped - consolidate instructions by using 3.12 for both apps
- [x] add a comment about .dockerignore to instructions
- [x] validate instructions
- [ ] commit to github
- [x] Add link to google slides 
- [ ] send info to faris