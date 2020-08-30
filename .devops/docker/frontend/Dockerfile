FROM node:12.18.3-buster-slim

ARG USER_ID=1000

ENV NPM_CONFIG_PREFIX=/home/node/.npm-global \
    PATH=${PATH}:/home/node/.npm-global/bin

RUN apt-get -qq update \
    && apt-get -qq -y install \
        bash \
        tini \
    && apt-get -qq -y autoremove \
    && apt-get -qq -y clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN groupmod -g ${USER_ID} node \
    && usermod -u ${USER_ID} -g ${USER_ID} node \
    && chown -R node:node /app

USER node

RUN mkdir -p ${NPM_CONFIG_PREFIX}
COPY ./frontend/package*.json /app/
RUN npm install --global @quasar/cli && npm install

VOLUME ["/app/node_modules"]
ENTRYPOINT ["/usr/bin/tini", "--"]
