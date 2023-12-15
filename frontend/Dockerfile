FROM node:latest AS build

WORKDIR /build

COPY package.json package.json

COPY yarn.lock yarn.lock
COPY tsconfig.json tsconfig.json
COPY api-spec.json api-spec.json

RUN corepack enable
RUN yarn install

COPY public/ public

COPY src/ src

RUN yarn run codegen
RUN yarn run build

FROM nginx:alpine

COPY --from=build /build/build/ /usr/share/nginx/html
