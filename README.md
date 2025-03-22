# scratch-web-app

Example building container with database, data retrieved by API, and UI to view

This uses Docker with Linux, MySQL, Python, and React with JS

## Setup

0. Clone this repository first: `git clone git@github.com:EnduringBeta/scratch-web-app.git`

### Run Docker container

1. Download [Docker Desktop](https://www.docker.com/) and install. Probably sign in. (This program is useful, but following steps will only use the command line functionality.)
2. Inside the repo directory from step 0, run `docker build -t scratch-web-app .`
3. Run `docker run -d -p 3306:3306 -p 5000:5000 scratch-web-app`

### Set up project and dependencies

All of these steps, unless specified, are done inside the Docker container

5. Run ``
6. Run `pip install -r requirements.txt` to install Flask

### Run the API

7. Run `./run-app.sh`, which starts the server API (`python3 app.py` and `flask run` also work)
8. 

## Troubleshooting

* Docker setup steps can also be accomplished via command line
* `docker run -d --name my-scratch-web-app -e MYSQL_ROOT_PASSWORD=insecure -p 5001:5000 mysql`
* 
