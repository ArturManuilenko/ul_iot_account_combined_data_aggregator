FROM gitlab.neroelectronics.by:5050/unic-lab/system/docker-images/basic-python:1.3.0

COPY Pipfile /docker_app/Pipfile
COPY Pipfile.lock /docker_app/Pipfile.lock
RUN pipenv install --dev --system

COPY ./src /docker_app/src
COPY ./data_aggregator_sdk /docker_app/data_aggregator_sdk
