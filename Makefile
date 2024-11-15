IMAGE_NAME := devcom-slides:local
DOCKER_VOL := -v ${CURDIR}:/work
DOCKER_8000 := -p 8000:8000
VIEW_PORT := 8000
DOCKER_CMD := docker run --rm -it ${DOCKER_VOL}

CONVERT_OPTS := \
	-c controls=true \
	-c controls_tutorial=false \
	--force

FILE ?= src/main.py
SCENE ?= Main


build:
	docker build -f docker/Dockerfile . -t ${IMAGE_NAME}

run:
	${DOCKER_CMD}

jupyter:
	${DOCKER_CMD} ${DOCKER_8888} --workdir /work ${IMAGE_NAME} jupyter lab --ip=0.0.0.0

gen:
	${DOCKER_CMD} ${IMAGE_NAME} manim ${FILE} ${SCENE}
	${DOCKER_CMD} ${IMAGE_NAME} manim-slides convert ${CONVERT_OPTS} ${SCENE} out/index.html

present:
	${DOCKER_CMD} ${IMAGE_NAME} manim-slides present ${SCENE}

view:
	${DOCKER_CMD} -d -p ${VIEW_PORT}:${VIEW_PORT} --name http-viewer ${IMAGE_NAME} python -m http.server ${VIEW_PORT} --directory out
	@echo http://localhost:${VIEW_PORT}

stop:
	docker stop http-viewer

clean:
	${DOCKER_CMD} ${IMAGE_NAME} rm -rf slides media 
	${DOCKER_CMD} ${IMAGE_NAME} find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

clean-all: clean
	${DOCKER_CMD} ${IMAGE_NAME} rm -rf out
