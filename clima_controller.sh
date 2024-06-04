#!/bin/sh
DIR=$(dirname "$(readlink -f "$0")")
. $DIR/.venv/bin/activate
python $DIR/clima_controller.py