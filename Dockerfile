FROM ubuntu

WORKDIR /usr/src/app
COPY . .
EXPOSE 8000

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install --no-cache-dir -r requirements.txt