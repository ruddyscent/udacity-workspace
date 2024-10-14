FROM nvcr.io/nvidia/pytorch:24.01-py3

# Let us install tzdata painlessly
ENV DEBIAN_FRONTEND=noninteractive

# Needed for string substitution
SHELL ["/bin/bash", "-c"]

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update  && apt-get -y install --no-install-recommends \
    neovim 

COPY requirements.txt /tmp/pip-tmp/

# RUN python -m pip install --upgrade pip \
#  && pip install --upgrade --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
#  && rm -rf /tmp/pip-tmp

RUN pip install --upgrade pip \
 && pip install --upgrade --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
 && rm -rf /tmp/pip-tmp

RUN echo "alias vi=nvim" >> ~/.bash_aliases \
 && echo "alias vim=nvim" >> ~/.bash_aliases
 
