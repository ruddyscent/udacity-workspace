FROM nvcr.io/nvidia/pytorch:23.01-py3

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        texlive-xetex \
        texlive-fonts-recommended \
        texlive-plain-generic \
        pandoc \
        neovim \
    && apt-get clean autoclean \
    && apt-get autoremove --yes
# && rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY requirements.txt /tmp/pip-tmp/

RUN pip install --upgrade pip \
    && pip --disable-pip-version-check --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

RUN echo "alias vi=nvim" >> ~/.bash_aliases \
 && echo "alias vim=nvim" >> ~/.bash_aliases
 
