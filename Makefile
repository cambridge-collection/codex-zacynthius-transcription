ifeq ($(shell [ -n "$$DRYRUN" ] && echo true),true)
	aws_dryrun := --dryrun
else
	aws_dryrun :=
endif

default:

dist:
	mkdir -p dist

dist/.git_revision:
	git rev-parse HEAD > $@

dist/index.html:
	python bin/generate_index.py ./transcription > $@

copy-html: dist
	cp -a ./transcription/* dist/

build: copy-html dist/index.html dist/.git_revision

clean:
	rm -r dist

publish_cmd:=docker container run \
					-e S3_BUCKET \
					-e AWS_ACCESS_KEY_ID \
					-e AWS_SECRET_ACCESS_KEY \
					-e AWS_DEFAULT_REGION=eu-west-1 \
					-e LOCAL_PATH=dist \
					-e EXTRA_ARGS=$(aws_dryrun) \
			 		--mount type=bind,src=$(shell pwd),dst=/code -w /code --rm \
			 		bitbucketpipelines/aws-s3-deploy:0.3.8

publish-staging:
	env S3_BUCKET=staging.codex-zacynthius-transcription.cudl.lib.cam.ac.uk \
		$(publish_cmd)

publish-production:
	env S3_BUCKET=codex-zacynthius-transcription.cudl.lib.cam.ac.uk \
			$(publish_cmd)

.PHONY: clean build copy-html default
