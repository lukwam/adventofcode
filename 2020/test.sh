#!/bin/bash


docker run -it --rm \
    -w /usr/src \
    -v "$(pwd):/usr/src" \
    python:3.8 \
    python main.py ${*}
