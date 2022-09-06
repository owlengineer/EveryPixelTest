FROM tknerr/baseimage-ubuntu:20.04

RUN apt-get update
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y python3-pip python3.8 build-essential libssl-dev libffi-dev

RUN python3.8 -m pip install --upgrade pip

ADD . /code
WORKDIR /code

ARG INPUT_PATH
ARG OUTPUT_PATH
RUN mkdir -p $INPUT_PATH
RUN mkdir -p $OUTPUT_PATH

RUN python3.8 -m pip install -r requirements.txt

CMD python3.8 main.py -i $INPUT_PATH -o $OUTPUT_PATH