ARG CARLA_VER=0.9.14
FROM carlasim/carla:${CARLA_VER}

ARG CARLA_VER

USER root

# Let us install tzdata painlessly
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    libpcl-dev \
    mesa-utils \
    zsh \
    libusb-1.0-0-dev \
    libvtk7.1 \
    neovim \
    build-essential \
    clang-8 \
    lld-8 \
    g++-7 \
    cmake \
    ninja-build \
    libvulkan1 \
    python \
    python-pip \
    python-dev \
    python3-dev \
    python3-pip \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev \
    tzdata \
    sed \
    curl \
    unzip \
    autoconf \
    libtool \
    rsync \
    libxml2-dev \
    git \ 
    wget \
    automake \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-8/bin/clang++ 180 \
 && update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-8/bin/clang 180

# COPY requirements.txt .
# RUN python3 -m pip install --no-deps -r requirements.txt 

# RUN ln -s /usr/bin/vtk6 /usr/bin/vtk && \
#     ln -s /usr/lib/python2.7/dist-packages/vtk/libvtkRenderingPythonTkWidgets.x86_64-linux-gnu.so /usr/lib/x86_64-linux-gnu/libvtkRenderingPythonTkWidgets.so 

ARG BASE_DIR=/home/libcarla-install
RUN cd /home \
 && git clone https://github.com/carla-simulator/carla.git carla-${CARLA_VER} \
 && cd carla-${CARLA_VER} \
 && git checkout ${CARLA_VER} \
 && make setup \
 && make LibCarla \
 && mkdir -p ${BASE_DIR}/include \
 && mkdir -p ${BASE_DIR}/lib \
 && find /home/carla-${CARLA_VER} -name *.so* -exec cp {} ${BASE_DIR}/lib \; \
 && find /home/carla-${CARLA_VER} -name *.a -exec cp {} ${BASE_DIR}/lib \; \
 && cp -r /home/carla-${CARLA_VER}/LibCarla/source/* ${BASE_DIR}/include/

RUN cd /home \
 && git clone https://github.com/rpclib/rpclib.git \
 && cd rpclib \
 && mkdir build \
 && cd build \
 && cmake .. \
 && cmake --build . \
 && mkdir ${BASE_DIR}/include/system \
 && cp -r ../include/* ${BASE_DIR}/include/system \
 && cp *.a ${BASE_DIR}/lib/

RUN cd /home/carla-${CARLA_VER}/Build/boost-1.80.0-c8-install/ \
 && cp -r include/boost ${BASE_DIR}/include/system \
 && find lib/* -name *.so* -exec cp {} ${BASE_DIR}/lib \; \
 && find lib/* -name *.a -exec cp {} ${BASE_DIR}/lib \; 

RUN cd /home/carla-${CARLA_VER}/Build/recast-0b13b0-c8-install/ \
 && cp -r include/recast/ ${BASE_DIR}/include/system \
 && cp lib/* ${BASE_DIR}/lib

