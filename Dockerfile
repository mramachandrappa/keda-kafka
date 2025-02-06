FROM docker-dp-common-releases-local.rt.artifactory.tio.systems/dp-document-alv3-python-3.10.14:1.8

# Set work directory.
WORKDIR /app

COPY src/* .
# COPY src/consumer.py data.py
# COPY src/data.py data.py
# COPY src/producer.py producer.py
# COPY src/requirements.txt requirements.txt

RUN pip install -r requirements.txt
