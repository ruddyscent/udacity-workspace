ARG CARLA_VER=0.9.14
FROM carlasim/carla:${CARLA_VER}

ARG CARLA_VER

USER root

# Let us install tzdata painlessly
ENV DEBIAN_FRONTEND=noninteractive

# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
# RUN apt-key del 7fa2af80 \ 
#  && wget https://developer.download.nvidia.com/compute/cuda/repos/$distro/$arch/cuda-keyring_1.0-1_all.deb \
#  && dpkg -i cuda-keyring_1.0-1_all.deb

# https://developer.nvidia.com/blog/updating-the-cuda-linux-gpg-repository-key/
RUN apt-key del 7fa2af80 \
 && apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub

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
    python3-setuptools \
    python3-distro \
    python3-wheel \
    gdb \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-8/bin/clang++ 180 \
 && update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-8/bin/clang 180

# COPY requirements.txt .
# RUN python3 -m pip install --no-deps -r requirements.txt 

# RUN ln -s /usr/bin/vtk6 /usr/bin/vtk && \
#     ln -s /usr/lib/python2.7/dist-packages/vtk/libvtkRenderingPythonTkWidgets.x86_64-linux-gnu.so /usr/lib/x86_64-linux-gnu/libvtkRenderingPythonTkWidgets.so 

# Apply patch
# https://www.boost.org/patches/1_80_0/0003-unordered-valid-after-move.patch
ARG BASE_DIR=/home/libcarla-install
RUN cd /home \
 && git clone https://github.com/carla-simulator/carla.git carla-${CARLA_VER} \
 && cd carla-${CARLA_VER} \
 && git checkout ${CARLA_VER} \
 && sed -i 's/BOOST_VERSION=1.80.0/BOOST_VERSION=1.83.0/g' ./Util/BuildTools/Setup.sh \
 && make setup \
 && make LibCarla \
 && make PythonAPI \
 && pip3 install ./PythonAPI/carla/dist/carla-*.whl \
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

RUN cd /home/carla-${CARLA_VER}/Build/boost-*/ \
 && cp -r include/boost ${BASE_DIR}/include/system \
 && find lib/* -name *.so* -exec cp {} ${BASE_DIR}/lib \; \
 && find lib/* -name *.a -exec cp {} ${BASE_DIR}/lib \; 

RUN cd /home/carla-${CARLA_VER}/Build/recast-*/ \
 && cp -r include/recast/ ${BASE_DIR}/include/system \
 && cp lib/* ${BASE_DIR}/lib

