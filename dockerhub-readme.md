# Codex Zacynthius Transcription

This image contains the Codex Zacynthius transcriptions used on [CUDL](https://cudl.lib.cam.ac.uk).

The HTML transcriptions are created by the [Codex Zacynthius
project][czr] and are licensed under the [Creative Commons
Attribution-ShareAlike 4.0 International License][cc].

[czr]: https://www.birmingham.ac.uk/research/activity/itsee/projects/codex-zacynthius.aspx
[cc]: https://creativecommons.org/licenses/by-sa/4.0/

### Usage

Running the image will give you a webserver (currently NGINX) hosting the transcriptions. To run the server on http://localhost:8080/:

```commandline
$ docker run --rm -p 8080:80 camdl/codex-zacynthius-transcription
```

It's based on the [nginx image](https://hub.docker.com/_/nginx), so all of its configuration options apply.

## Versioning

The image is tagged with:

- `latest` — The most recent `production` build.
- short git commit hash — The commit hash of the revision the image was built from.

[dh]: https://hub.docker.com/repository/docker/camdl/codex-zacynthius-transcription

## Source

https://bitbucket.org/CUDL/codex-zacynthius-transcription
