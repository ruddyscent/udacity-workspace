FROM nvcr.io/nvidia/tensorflow:23.03-tf2-py3
# FROM nvcr.io/nvidia/pytorch:23.06-py3

# Let us install tzdata painlessly
ENV DEBIAN_FRONTEND=noninteractive

# Needed for string substitution
SHELL ["/bin/bash", "-c"]
# Pick up some TF dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
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
	python3-wxgtk4.0

WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install --no-deps -r requirements.txt 
# RUN python3 -m pip install --no-deps waymo-open-dataset-tf-2-11-0==1.5.2

RUN git clone https://github.com/tensorflow/models.git && \
    cd /app/models/research/ && \
    protoc object_detection/protos/*.proto --python_out=. && \
    cp object_detection/packages/tf2/setup.py . && \
    python -m pip install .

# Install google cloud SDK
RUN curl -sSL https://sdk.cloud.google.com > /tmp/gcl && bash /tmp/gcl --install-dir=~/gcloud --disable-prompts
ENV PATH="$PATH:/root/gcloud/google-cloud-sdk/bin"

# TensorRT depends on libnvinfer{_plugin}7 
RUN cd /usr/lib/x86_64-linux-gnu && \
    ln -s libnvinfer_plugin.so.8 libnvinfer_plugin.so.7 && \
    ln -s libnvinfer.so.8 libnvinfer.so.7

# pip-installed OpenCV causes circular import
RUN pip uninstall -y opencv-python
