#!/bin/bash
CURRENT_DIR=$(pwd)
TOOLS_APP_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
ROOT_DIR="$(dirname "$TOOLS_APP_DIR")"

cd "${ROOT_DIR}/src"

echo "--> Regenerating PIP Requirements..."
pip freeze > "${ROOT_DIR}/doc/requirements.txt"

echo "--> Validating Django models..."
./manage.py validate

echo "--> Generating fixtures for current JobTrak core models..."
./manage.py dumpdata --format=json jobtrak_core > "${ROOT_DIR}/tools/fixtures/jobtrak_core_all.json"

echo "--> Generate model map..."
./manage.py graph_models -a -g -o "${ROOT_DIR}/doc/model_maps/all.png"

cd ${CURRENT_DIR}
