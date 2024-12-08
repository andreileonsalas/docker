FROM python:2.7

MAINTAINER Piero Steinger <piero@steinger.eu>

ENV DNDTOOLS_VERSION master
ENV DNDTOOLS_DIR /dndtoolsrepo
ENV DATA_DIR /data

COPY prod-master/files/ $DATA_DIR/

# Instalar dependencias y DnDTools
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    ca-certificates \
    gcc \
    libmariadb-dev \
    wget \
  && wget https://srd.dndtools.org/dndtools-master2.zip -q -O dndtools-master.zip && unzip -o dndtools-master.zip \
  && mv /dndtools-$DNDTOOLS_VERSION $DNDTOOLS_DIR \
  && cd $DNDTOOLS_DIR \
  && pip install https://github.com/etianen/django-reversion/archive/release-1.3.3.zip \
  && pip install -r requirements.txt \
  && pip install mysqlclient \ 
  && apt-get purge -y \
    ca-certificates \
    gcc \
    wget \
  && apt-get autoremove --purge -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD ["/data/runscript.sh"]
