# FROM nvcr.io/nvidia/tensorflow:22.10-tf1-py3
FROM nvcr.io/nvidia/tensorflow:22.11-tf1-py3

ENV TF_ALLOW_IOLIBS=1

RUN apt-get update \
 && export DEBIAN_FRONTEND=noninteractive \
 && apt-get -y install --no-install-recommends libsndfile1-dev \
 && apt-get clean autoclean \
 && apt-get autoremove --yes \
 && rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY requirements.txt /tmp/pip-tmp/

RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
 && rm -rf /tmp/pip-tmp

# RUN conda install -c conda-forge wordcloud

# RUN python -m nltk.downloader averaged_perceptron_tagger \
#  && python -m nltk.downloader maxent_ne_chunker \
#  && python -m nltk.downloader punkt

