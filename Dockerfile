# Use Ubuntu Docker image
FROM ubuntu:latest

LABEL org.opencontainers.image.authors="Ross Llewallyn"

# Environment variables
ENV MYSQL_ROOT_PASSWORD=insecure
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=insecure

ENV REPO_DIR=scratch-web-app

ENV FLASK_APP=$REPO_DIR/app.py
ENV FLASK_ENV=development

# Get needed packages
RUN apt-get update && \
    apt-get install -y mysql-server python3 python3-pip python3-venv git && \
    apt-get clean

# Ensure MySQL user has a valid home directory
RUN usermod -d /var/lib/mysql mysql

# Set working directory
WORKDIR /app

# Invalidate cache
#ARG CACHEBUST=1

# Get repo
RUN git clone https://github.com/EnduringBeta/scratch-web-app.git

# Use Python virtual environment to install and use project dependencies
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip3 install -r $REPO_DIR/requirements.txt

# Expose MySQL and Flask ports
EXPOSE 3306 5000

# Start web app
CMD ["bash", "$REPO_DIR/run-app.sh"]
