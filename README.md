# Codex Zacynthius Transcription

This repo contains the Codex Zacynthius transcriptions used on [CUDL](https://cudl.lib.cam.ac.uk).

Currently we have static HTML transcriptions for all the pages. In the future we expect to have access to the TEI XML and XSLT which generates these HTML transcriptions.

## Hosting

The transcriptions are hosted at:

* Production: [codex-zacynthius-transcription.cudl.lib.cam.ac.uk][production]
* Staging: [staging.codex-zacynthius-transcription.cudl.lib.cam.ac.uk][staging]

[production]: http://codex-zacynthius-transcription.cudl.lib.cam.ac.uk/
[staging]: http://staging.codex-zacynthius-transcription.cudl.lib.cam.ac.uk/

The sites are hosted as static sites via public AWS S3 buckets:

* Production: http://codex-zacynthius-transcription.cudl.lib.cam.ac.uk.s3-website.eu-west-2.amazonaws.com/
* Staging: http://staging.codex-zacynthius-transcription.cudl.lib.cam.ac.uk.s3-website.eu-west-2.amazonaws.com/

## Publishing

Publishing is done primarily via the Bitbucket Pipelines build in this repo. The `production` branch is automatically published to the production site, and `master` is published to staging.

The build creates a `.git_revision` file which can be used to determine which version is currently published:

```commandline
curl http://staging.codex-zacynthius-transcription.cudl.lib.cam.ac.uk.s3-website.eu-west-2.amazonaws.com/.git_revision

d672731c6e714991310c2513f6d43cd6e3d6a39b
```

Publishing can also be done via the Makefile in this repo:

```commandline
$ git checkout $REVISION
$ make clean build
$ # This simulates publishing (checks permissions) without actually changing anything
$ export DRYRUN=true
# AWS credentials are required to update S3
$ export AWS_ACCESS_KEY_ID=XXX
$ export AWS_SECRET_ACCESS_KEY=XXX
$ # sudo is required because publishing is done by running a docker container
$ sudo --preserve-env=DRYRUN,AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY make publish-staging
$ sudo make publish-production
```

## Docker image

A Docker container image is automatically built from the production branch and pushed to docker hub with the name [`camdl/codex-zacynthius-transcription`][dh].

### Image tags

The image is tagged with:

- `latest` — The most recent `production` build.
- short git commit hash — The commit hash of the revision the image was built from.

### Usage

Running the image will give you a webserver (currently NGINX) hosting the transcriptions. To run the server on http://localhost:8080/ :

```commandline
$ docker run --rm -p 8080:80 camdl/codex-zacynthius-transcription
```

[dh]: https://hub.docker.com/repository/docker/camdl/codex-zacynthius-transcription
