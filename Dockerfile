FROM python:3.8.0-alpine3.10 AS template-generator
WORKDIR /build
COPY transcription ./transcription
COPY bin ./bin
RUN python bin/generate_index.py transcription > index.html

FROM nginx:1.17.6-alpine
COPY transcription /usr/share/nginx/html
COPY --from=template-generator /build/index.html /usr/share/nginx/html/
