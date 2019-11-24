# Define Python version
ARG PYTHON_VERSION=3.7.3

# Define source image
FROM python:${PYTHON_VERSION}-alpine

# Information about building
LABEL maintainer = "Antonio Carlos Gomes <acgomes68@gmail.com>"
LABEL description = "Python 3.7.3 based on Alpine Linux"

#Copy python requirements file
COPY ./requirements.txt /tmp/requirements.txt

# 1.Update packages from main repositories
# 2.Update repositories and install required system packages
# 3.Install required python packages
# 4.Clean building
RUN \
    # apk update && apk upgrade && \
    pip3 install --no-cache-dir --upgrade --force-reinstall pip setuptools && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf \
            /var/cache/apk/* \ 
            /tmp/* \
            /var/tmp/*

# Define app work directory and copy files
WORKDIR /app
COPY ./app /app

# Execute project default python file
CMD [ "python", "teste.py" ]