FROM nvcr.io/nvidia/pytorch:21.11-py3

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update \
# && export DEBIAN_FRONTEND=noninteractive \
# && apt-get -y install --no-install-recommends <your-package-list-here> \
# && apt-get clean autoclean \
# && apt-get autoremove --yes \
# && rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY requirements.txt /tmp/pip-tmp/

RUN pip install --upgrade pip \
&& pip install --upgrade --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
&& rm -rf /tmp/pip-tmp

