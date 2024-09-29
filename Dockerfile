FROM python:3.11.9-slim-bookworm
ADD . /
RUN apt-get update --fix-missing && apt-get install -y --fix-missing build-essential
RUN apt-get -y update && apt-get -y install curl
RUN make install 
RUN make lint
RUN make serve & sleep 5 && make test 
EXPOSE 8000
