IMAGE ?= jackma00/01-unzip
IMAGE_TAG ?= latest

.PHONY: venv install format lint test local_launch build run

venv:
	python3 -m venv .venv

install: setup.py
	. ./.venv/bin/activate && \
	pip install --upgrade pip &&\
	pip install .[dev]

format:
	. ./.venv/bin/activate && \
	black .

local_launch: venv 
	. .venv/bin/activate && \
	python ./src/main.py 

build:
	docker build --tag $(IMAGE):$(IMAGE_TAG) .

push:
	docker push $(IMAGE):$(IMAGE_TAG)

run:
	docker run --rm $(IMAGE):$(IMAGE_TAG)
