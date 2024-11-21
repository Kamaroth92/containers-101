IMAGE_NAME := devcom-slides:local
DOCKER_VOL := -v ${CURDIR}:/work
VIEW_PORT := 8000
DOCKER_CMD := docker run --rm -it ${DOCKER_VOL}

CONVERT_OPTS := \
	-c title=DevCom \
	-c controls=true \
	-c controls_tutorial=false \
	-c embedded=false \
	-c data_uri=false \
	-c preview_links=true \
	-c preload_iframes=true \
	--force

FILE ?= src/main.py
SCENES ?= Main


build:
	docker build -f docker/Dockerfile . -t ${IMAGE_NAME}

run:
	${DOCKER_CMD}

jupyter:
	${DOCKER_CMD} ${DOCKER_8888} --workdir /work ${IMAGE_NAME} jupyter lab --ip=0.0.0.0

gen:
	${DOCKER_CMD} ${IMAGE_NAME} manim ${FILE} ${SCENES}
	${DOCKER_CMD} ${IMAGE_NAME} manim-slides convert ${CONVERT_OPTS} ${SCENES} out/index.html

view:
	${DOCKER_CMD} --rm -d -p ${VIEW_PORT}:${VIEW_PORT} --name http-viewer ${IMAGE_NAME} python -m http.server ${VIEW_PORT} --directory out
	@echo http://localhost:${VIEW_PORT}

stop:
	-docker stop http-viewer
	-docker rm http-viewer

clean:
	${DOCKER_CMD} ${IMAGE_NAME} rm -rf slides media 
	${DOCKER_CMD} ${IMAGE_NAME} find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

clean-all: clean
	${DOCKER_CMD} ${IMAGE_NAME} rm -rf out

convert_opts:
	${DOCKER_CMD} ${IMAGE_NAME} manim-slides convert --help
	${DOCKER_CMD} ${IMAGE_NAME} manim-slides convert --show-config
	${DOCKER_CMD} ${IMAGE_NAME} manim-slides convert --show-template