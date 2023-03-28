FROM arm64v8/ubuntu:latest

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        texlive-xetex \
        texlive-fonts-recommended \
        texlive-plain-generic \
        pandoc \
        nodejs \
        npm \
        wget \
        python3-ipykernel \
        python3-ipywidgets \
        python3-pip \
        python3-psycopg2 \
        python3-pandas \
        postgresql-client-common \
        postgresql-client-14 \
        boto3 \
        python3-matplotlib
#    && rm -rf /var/lib/apt/lists/* \
#    && rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY requirements.txt /tmp/pip-tmp/

RUN pip install --upgrade pip \
    && pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

