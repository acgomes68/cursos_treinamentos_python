# Define Anaconda version
ARG ANACONDA_VERSION=2019.10

# Define source image
FROM continuumio/anaconda3:${ANACONDA_VERSION}-alpine

# Information about building
LABEL maintainer = "Antonio Carlos Gomes <acgomes68@gmail.com>"
LABEL description = "Anaconda 2.19.10 based on Alpine Linux and Python 3.7"

# 1.Update packages from main repositories
# 2.Update repositories and install required system packages
# 3.Install required python packages
# 4.Clean building
RUN \
    # apk update && apk upgrade && \
    rm -rf \
            /var/cache/apk/* \ 
            /tmp/* \
            /var/tmp/*

# Define app work directory and copy files
WORKDIR /app
COPY ./app /app

# Execute project default python file
# CMD [ "python", "teste.py" ]