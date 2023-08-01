FROM ubuntu:20.04

# Let us install tzdata painlessly
ENV DEBIAN_FRONTEND=noninteractive

# Needed for string substitution
SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y --no-install-recommends \
	python3-pip \
	python3-dev \
        texlive-xetex \
        texlive-fonts-recommended \
        texlive-plain-generic \
        pandoc \
        build-essential \
        ffmpeg \
        g++ \
        zip \
        zlib1g-dev \
        curl \
        libfreetype6-dev \
        libhdf5-serial-dev \
        libzmq3-dev \
        libcairo2-dev \
        pkg-config \
        software-properties-common \
        unzip \
        wget \
	protobuf-compiler \
	python3-wxgtk4.0 \
	libgl1-mesa-glx \
	libgl1-mesa-dri \
	libcanberra-gtk-module \
	libcanberra-gtk3-module \
	nvtop \
	cmake \
	libpcl-dev

WORKDIR /home

COPY requirements.txt .
# RUN python3 -m pip install --no-deps -r requirements.txt 
RUN python3 -m pip install -r requirements.txt

# RUN git clone https://github.com/tensorflow/models.git && \
#     cd /app/models/research/ && \
#     protoc object_detection/protos/*.proto --python_out=. && \
#     cp object_detection/packages/tf2/setup.py . && \
#     python -m pip install .

# # Install google cloud SDK
# RUN curl -sSL https://sdk.cloud.google.com > /tmp/gcl && bash /tmp/gcl --install-dir=~/gcloud --disable-prompts
# ENV PATH="$PATH:/root/gcloud/google-cloud-sdk/bin"

# # TensorRT depends on libnvinfer{_plugin}7 
# RUN cd /usr/lib/x86_64-linux-gnu && \
#     ln -s libnvinfer_plugin.so.8 libnvinfer_plugin.so.7 && \
#     ln -s libnvinfer.so.8 libnvinfer.so.7

# pip-installed OpenCV causes circular import
# RUN pip uninstall -y opencv && \
#     apt-get install -y python3-opencv

RUN ln -s /usr/bin/make /usr/bin/gmake

RUN apt-get install -y --no-install-recommends x11-apps mesa-utils
