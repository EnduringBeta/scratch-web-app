# scratch-web-app

Example building container with database, data retrieved by API, and UI to view

This uses Docker with Linux, MySQL, Python, and React with JS

## TODO

* Build `dockerfile` to automate this setup

## Setup

### Set up Docker

1. Download [Docker Desktop](git@github.com:EnduringBeta/scratch-web-app.git) and install. Sign in.
2. In Docker Desktop "Images", search "mysql". Click "Run" for the official entry. A "Run a new container" modal should appear.
3. In "Optional Settings", specify the name "scratch-web-app" and add the environment variable "MYSQL_ALLOW_EMPTY_PASSWORD" set to "TRUE". (This is bad practice for anything other than light testing like for this repo.)
4. In the resulting container view, select "Exec" and run `mysql --version` to confirm MySQL is present.

### Set up project and dependencies

All of these steps, unless specified, are done inside the Docker container

5. Run `git clone git@github.com:EnduringBeta/scratch-web-app.git`
6. Run `pip install -r requirements.txt` to install Flask

### Run the API

7. Run `./run-app.sh`, which starts the server API (`python3 app.py` and `flask run` also work)
8. 

## Troubleshooting

* `docker build -t scratch-web-app .`
* `docker run -d -p 3306:3306 -p 5000:5000 scratch-web-app`

* Docker setup steps can also be accomplished via command line
* `docker run -d --name my-scratch-web-app -e MYSQL_ROOT_PASSWORD=insecure -p 5001:5000 mysql`
* 
