FROM quay.io/jupyter/datascience-notebook

COPY requirements.txt /tmp

RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r /tmp/requirements.txt
