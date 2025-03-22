# scratch-web-app

Example building container with database, data retrieved by API, and UI to view

This uses Docker with Linux, MySQL, Python, and React with JS

## Containerized Setup

0. Clone this repository first: `git clone git@github.com:EnduringBeta/scratch-web-app.git`

### Run Docker container

1. Download [Docker Desktop](https://www.docker.com/) and install. Probably sign in. (This program is useful, but following steps will only use the command line functionality.)
2. Inside the repo directory from step 0, run `docker build -t scratch-web-app .` to build the Docker image
3. Run `docker run -d -p 3306:3306 -p 5000:5000 scratch-web-app` to start the server

## Local Setup

0. Clone this repository first: `git clone git@github.com:EnduringBeta/scratch-web-app.git`
1. Setup MySQL?
2. TODOROSS: set up same as Docker internally
3. Run `./run-app.sh`, which starts the server API (`python3 app.py` and `flask run` also work)

## Troubleshooting

* On Docker run, "Bind for 0.0.0.0:3306 failed: port is already allocated" - stop existing Docker container
* .
