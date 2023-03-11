FROM arm64v8/ubuntu

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
        python3-tk \
        python3-opencv \
        wget \
        python3-ipykernel \
        python3-ipywidgets \
        python3-octave-kernel \
        python3-pip \
        octave \
        gnuplot \
        fonts-freefont-otf \
        ghostscript
#    && rm -rf /var/lib/apt/lists/* \
#    && rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY requirements.txt /tmp/pip-tmp/

RUN pip install --upgrade pip \
    && pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp
