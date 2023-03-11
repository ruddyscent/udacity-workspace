FROM arm64v8/ubuntu:trusty

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        cowsay \
        curl \
        unzip \
        man-db \
        bc \
        nano
#    && apt-get clean autoclean \
#    && apt-get autoremove --yes 
#    && rm -rf /var/lib/{apt,dpkg,cache,log}/

# RUN conda install ipykernel ipywidgets pandoc

# COPY requirements.txt /tmp/pip-tmp/
# 
# RUN pip install --upgrade pip \
#     && pip install --upgrade --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#     && rm -rf /tmp/pip-tmp

