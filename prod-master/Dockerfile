FROM debian:stable

MAINTAINER Piero Steinger <piero@steinger.eu>

ENV DEBIAN_FRONTEND noninteractive
ENV DNDTOOLS_VERSION master
ENV DNDTOOLS_DIR /dndtoolsrepo
ENV DATA_DIR /data

COPY prod-master/files/ $DATA_DIR/

# Instalar dependencias y Python 2.7
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    ca-certificates \
    gcc \
    wget \
  && wget https://debian.sipwise.com/debian/pool/main/p/python2.7/python2.7_2.7.18-5_amd64.deb -O python2.7.deb \
  && dpkg -i python2.7.deb \
  && apt-get install -f -y \
  && rm python2.7.deb \
  && apt-get install -y python-pip python-dev \
  && wget https://github.com/dndtools/dndtools/archive/$DNDTOOLS_VERSION.tar.gz -q -O- | tar -xz \
  && mv /dndtools-$DNDTOOLS_VERSION $DNDTOOLS_DIR \
  && cd $DNDTOOLS_DIR \
  && pip install https://github.com/etianen/django-reversion/archive/release-1.3.3.zip \
  && pip install -r requirements.txt \
  && apt-get purge -y \
    ca-certificates \
    gcc \
    python-dev \
    python-pip \
    wget \
  && apt-get autoremove --purge -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && ln -s $(which python2.7) /usr/bin/python

EXPOSE 8000

CMD ["/data/runscript.sh"]
