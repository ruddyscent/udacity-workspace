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
        python3-pip
#    && rm -rf /var/lib/apt/lists/* \
#    && rm -rf /var/lib/{apt,dpkg,cache,log}/

