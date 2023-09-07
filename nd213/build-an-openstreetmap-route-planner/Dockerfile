# FROM arm64v8/ubuntu:22.04
FROM ubuntu:22.04

RUN apt-get update \
 && export DEBIAN_FRONTEND=noninteractive \
 && apt-get -y install --no-install-recommends \
        cmake \
        build-essential \
	libcairo2-dev \
	libgraphicsmagick1-dev \
	libpng-dev \
	git \
	neovim \
	x11-apps \
	mesa-utils \
 && apt-get clean autoclean \
 && apt-get autoremove --yes 
# && rm -rf /var/lib/{apt,dpkg,cache,log}/

# COPY requirements.txt /tmp/pip-tmp/
# 
# RUN pip install --upgrade pip \
#  && pip install --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#  && rm -rf /tmp/pip-tmp


# Build IO2D
# https://github.com/cpp-io2d/P0267_RefImpl/blob/master/BUILDING.md
 # https://m.blog.naver.com/jamsuham75/221846244985
RUN git config --global http.sslVerify false \ 
 && git clone --recurse-submodules https://github.com/cpp-io2d/P0267_RefImpl \
 && cd P0267_RefImpl \
 && mkdir build \
 && cd build \
 # https://github.com/cpp-io2d/P0267_RefImpl/issues/147
 && cmake .. -DIO2D_WITHOUT_TESTS=1 \ 
 && make \
 && make install

RUN echo "alias vi=nvim" >> ~/.bash_aliases \
 && echo "alias vim=nvim" >> ~/.bash_aliases
