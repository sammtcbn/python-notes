#!/bin/bash
docker run --rm -it --name python -v $PWD/src:/root/src --workdir="/root/src" python bash
