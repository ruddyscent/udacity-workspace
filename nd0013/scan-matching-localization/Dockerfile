ARG CARLA_VER=0.9.14
FROM carlasim/carla:${CARLA_VER}

ARG CARLA_VER

USER root

# Let us install tzdata painlessly
ENV DEBIAN_FRONTEND=noninteractive

# https://developer.nvidia.com/blog/updating-the-cuda-linux-gpg-repository-key/
RUN apt-key del 7fa2af80 \
 && apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub

RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
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
    libflann-dev \
    libglew-dev \
    libvtk7-dev \
    libbz2-dev \
    nvidia-cuda-dev \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-8/bin/clang++ 180 \
 && update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-8/bin/clang 180

COPY requirements.txt .
RUN python3 -m pip install --no-deps -r requirements.txt 

RUN ln -s /usr/bin/vtk6 /usr/bin/vtk && \
    ln -s /usr/lib/python2.7/dist-packages/vtk/libvtkRenderingPythonTkWidgets.x86_64-linux-gnu.so /usr/lib/x86_64-linux-gnu/libvtkRenderingPythonTkWidgets.so 

ARG EIGEN_VER=3.3.7
RUN cd /home \
 && wget -qO- https://gitlab.com/libeigen/eigen/-/archive/${EIGEN_VER}/eigen-${EIGEN_VER}.tar.gz | tar xz \
 && cd eigen-${EIGEN_VER} && mkdir build && cd build \
 && cmake .. \
 && make install \
 && cd ../.. && rm -rf eigen-${EIGEN_VER}/ && rm -f eigen-${EIGEN_VER}.tar.gz

ARG BOOST_VER=1.75.0
ARG BOOST_VER_=1_75_0
RUN cd /home \
 && wget https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VER}/source/boost_1_75_0.tar.gz \
 && tar xvf boost_${BOOST_VER_}.tar.gz \
 && cd boost_${BOOST_VER_} \
 && ./bootstrap.sh --prefix=/usr/local/ \
 && ./b2 install 

ARG PCL_VER=1.13.1
RUN cd /home \
 && wget https://github.com/PointCloudLibrary/pcl/archive/pcl-${PCL_VER}.tar.gz \
 && tar -xf pcl-${PCL_VER}.tar.gz \
 && cd pcl-pcl-${PCL_VER}/ \
 && mkdir build && cd build \
 && cmake .. \
 && make -j6 \
 && make install

# Apply patch
# https://www.boost.org/patches/1_80_0/0003-unordered-valid-after-move.patch
ARG BASE_DIR=/home/libcarla-install
RUN cd /home \
 && git clone https://github.com/carla-simulator/carla.git carla-${CARLA_VER} \
 && cd carla-${CARLA_VER} \
 && git checkout ${CARLA_VER} \
 && sed -i 's/BOOST_VERSION=1.80.0/BOOST_VERSION=${BOOST_VER}/g' ./Util/BuildTools/Setup.sh \
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

