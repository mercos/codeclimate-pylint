.PHONY: image

IMAGE_NAME ?= codeclimate/codeclimate-pylint

image:
	docker build --rm -t $(IMAGE_NAME) .
