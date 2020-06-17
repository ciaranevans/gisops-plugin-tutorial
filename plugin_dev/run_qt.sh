#!/bin/bash

xhost +
docker build -t qgis-development:latest -f qgis_development/Dockerfile .
docker run -it --rm --privileged --net=host --env="DISPLAY" -v $(pwd):/qgis-workspace \
qgis-development:latest qgis
