FROM jupyter/scipy-notebook:ubuntu-22.04

USER root

COPY requirements.txt /tmp/pip-tmp/

RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
 && rm -rf /tmp/pip-tmp

