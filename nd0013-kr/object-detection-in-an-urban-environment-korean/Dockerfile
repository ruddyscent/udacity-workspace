FROM nvcr.io/nvidia/tensorflow:23.03-tf2-py3

# Let us install tzdata painlessly
ENV DEBIAN_FRONTEND=noninteractive

# Needed for string substitution
SHELL ["/bin/bash", "-c"]
# Pick up some TF dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
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
	protobuf-compiler

# # Install TensorRT if not building for PowerPC
# # NOTE: libnvinfer uses cuda11.1 versions
# RUN [[ "${ARCH}" = "ppc64le" ]] || { apt-get update && \
#         apt-get install -y --no-install-recommends libnvinfer${LIBNVINFER_MAJOR_VERSION}=${LIBNVINFER}+cuda11.0 \
#         libnvinfer-plugin${LIBNVINFER_MAJOR_VERSION}=${LIBNVINFER}+cuda11.0 \
#         && apt-get clean \
#         && rm -rf /var/lib/apt/lists/*; }
# 
# # See http://bugs.python.org/issue19846
# ENV LANG C.UTF-8
# 
# RUN apt update -y && \
#     add-apt-repository ppa:deadsnakes/ppa -y && \
#     apt install -y python3.8 python3-pip
# 
# RUN ln -s $(which python3) /usr/local/bin/python
# 
# RUN python -m pip install --upgrade pip && \
#     pip install tensorflow==2.5.0 tf-models-official==2.5.1 tensorflow_io==0.19.1 pyparsing==2.4.2 pycairo keras==2.5.0rc0

WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
# RUN python3 -m pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
# 
# ENV TF_CPP_MIN_LOG_LEVEL=2
# 
# RUN wget https://github.com/protocolbuffers/protobuf/releases/download/v3.13.0/protoc-3.13.0-linux-x86_64.zip && \
#     unzip protoc-3.13.0-linux-x86_64.zip -d /app/protobuf/
# 
# ENV PATH "$PATH:/app/protobuf/bin"

RUN git clone https://github.com/tensorflow/models.git && \
    cd /app/models/research/ && \
    protoc object_detection/protos/*.proto --python_out=. && \
    cp object_detection/packages/tf2/setup.py . && \
    python -m pip install .

# Install google cloud SDK
RUN curl -sSL https://sdk.cloud.google.com > /tmp/gcl && bash /tmp/gcl --install-dir=~/gcloud --disable-prompts
ENV PATH="$PATH:/root/gcloud/google-cloud-sdk/bin"
