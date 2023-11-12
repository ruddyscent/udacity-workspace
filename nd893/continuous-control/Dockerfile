FROM pytorch/pytorch:latest

# RUN apt-get update \
#  && export DEBIAN_FRONTEND=noninteractive \
#  && apt-get -y install --no-install-recommends libsndfile1-dev \
#  && apt-get clean autoclean \
#  && apt-get autoremove --yes \
#  && rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY requirements.txt /tmp/pip-tmp/

RUN pip install --upgrade pip \
 && pip install --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
 && rm -rf /tmp/pip-tmp
