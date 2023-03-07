FROM nvcr.io/nvidia/tensorflow:23.02-tf2-py3

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update -y \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        texlive-xetex \
        texlive-fonts-recommended \
        texlive-plain-generic \
        pandoc \
        nodejs \
        npm \
        apt-transport-https \
        ca-certificates \
        gnupg \
        python3-tk \
        python3-opencv
#    && rm -rf /var/lib/apt/lists/* \
#    && rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - \
    && apt-get update -y \
    && apt-get -y install google-cloud-cli
#    && rm -rf /var/lib/apt/lists/* \
#    && rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY requirements.txt /tmp/pip-tmp/

RUN pip install --upgrade pip \
    && pip install --upgrade --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager

