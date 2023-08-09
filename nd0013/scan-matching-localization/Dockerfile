FROM carlasim/carla:0.9.14

USER root

# Let us install tzdata painlessly
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
	sudo \
	python3-pip \
        g++ \
	cmake \
	libpcl-dev \
	mesa-utils

COPY requirements.txt .
RUN python3 -m pip install --no-deps -r requirements.txt 

