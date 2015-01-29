#!/bin/bash
CURRENT_DIR=$(pwd)
TOOLS_APP_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
ROOT_DIR="$(dirname """$TOOLS_APP_DIR""")"
WIKI_ROOT="$(dirname """$ROOT_DIR""")/JobTrak.wiki"

echo "====================================================================="
echo "  Current Directory: ${CURRENT_DIR}"
#echo "Tools App Directory: ${TOOLS_APP_DIR}"
#echo "     Root Directory: ${ROOT_DIR}"
# echo "Wiki Root Directory: ${WIKI_ROOT}" 
echo "====================================================================="
echo  ""
cd "${ROOT_DIR}/src"

echo "--> Regenerating PIP Requirements..."
pip freeze > "${ROOT_DIR}/doc/requirements.txt"

echo "--> Validating Django models..."
./manage.py validate

# -- skipping fixture generation to prevent sensitive data from being pushed
#echo "--> Generating fixtures for current JobTrak core models..."
#./manage.py dumpdata --format=json > "${ROOT_DIR}/tools/fixtures/all.json"
#echo ""

echo "--> Handling language files..."
./manage.py runscript generate_messages

echo "--> Generating Dynamic Wiki Docs..."
if [ ! -d "$WIKI_ROOT" ]; then
	echo "    - Skipping. JobTrak.wiki repo not found."
else
	./manage.py runscript generate_wiki
fi

echo ""
echo ""
cd ${CURRENT_DIR}
