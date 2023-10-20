FROM python:3.11.0-buster AS compile-image

ARG REQUIREMENTS

RUN set -ex

RUN addgroup --system --gid 666 app && adduser --system --uid 666 --gid 666 app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc libc-dev wget libgeos-dev libmaxminddb0 \
        libmaxminddb-dev mmdb-bin libxml2-dev libxmlsec1-dev libxmlsec1-openssl

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && chown root:root /usr/local/bin/dockerize

RUN wget https://github.com/go-task/task/releases/download/v3.12.1/task_linux_amd64.tar.gz \
    && tar -C /usr/local/bin -xzvf task_linux_amd64.tar.gz \
    && rm task_linux_amd64.tar.gz \
    && chown root:root /usr/local/bin/task

RUN wget https://github.com/vmware-tanzu/carvel-ytt/releases/download/v0.39.0/ytt-linux-amd64 \
    && echo "7a472b8c62bfec5c12586bb39065beda42c6fe43cf24271275e4dbc0a04acb8b  ytt-linux-amd64" | sha256sum --check --status \
    && mv ytt-linux-amd64 /usr/local/bin/ytt \
    && chmod +x /usr/local/bin/ytt \
    && chown root:root /usr/local/bin/ytt

COPY ./requirements.txt .
COPY ./requirements.dev.txt .
RUN pip install --user -r ${REQUIREMENTS}

FROM python:3.11.0-slim-buster AS build-image
ENV PYTHONUNBUFFERED 1
ENV PATH=/home/app/.local/bin:$PATH

RUN addgroup --system --gid 666 app && adduser --system --uid 666 --gid 666 app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        locales gnupg2 curl libpq-dev binutils libgeos-dev libproj-dev gdal-bin gosu vim libmaxminddb0 \
        libmaxminddb-dev mmdb-bin libmagic-dev lm-sensors \
        libxml2-dev libxmlsec1-dev libxmlsec1-openssl git-crypt openssh-client jq gettext \
    && rm -rf /var/cache/apt/* /var/lib/apt/lists/*

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen

ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8

COPY --chown=app:app --from=compile-image /root/.local /home/app/.local
COPY --from=compile-image /usr/local/bin/dockerize /usr/local/bin/dockerize
COPY --from=compile-image /usr/local/bin/task /usr/local/bin/task
COPY --from=compile-image /usr/local/bin/ytt /usr/local/bin/ytt

COPY --chown=app:app . /app
WORKDIR /app/src

EXPOSE 8232
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["runserver"]
