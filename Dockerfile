FROM python:3.8.0-alpine3.10 AS template-generator
WORKDIR /build
COPY transcription ./transcription
COPY bin ./bin
RUN python bin/generate_index.py transcription > index.html

FROM nginx:1.17.6-alpine

LABEL org.opencontainers.image.title="Codex Zacynthius Transcription"
LABEL org.opencontainers.image.description="The Codex Zacynthius transcriptions used on Cambridge Digital Library (https://cudl.lib.cam.ac.uk), served by NGINX."
LABEL org.opencontainers.image.licenses="CC-BY-SA-4.0 AND MIT"
LABEL org.opencontainers.image.url="https://hub.docker.com/r/camdl/codex-zacynthius-transcription"
LABEL org.opencontainers.image.source="https://bitbucket.org/CUDL/codex-zacynthius-transcription"
LABEL maintainer="https://bitbucket.org/CUDL/"

COPY transcription /usr/share/nginx/html
COPY --from=template-generator /build/index.html /usr/share/nginx/html/
