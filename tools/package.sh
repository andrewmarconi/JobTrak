#!/bin/bash
CURRENT_DIR=$(pwd)
TOOLS_APP_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
ROOT_DIR="$(dirname """$TOOLS_APP_DIR""")"
#WIKI_ROOT="$(dirname """$ROOT_DIR""")/JobTrak.wiki"

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
echo ""

echo "--> Validating Django models..."
./manage.py validate
echo ""

# -- skipping fixture generation to prevent sensitive data from being pushed
#echo "--> Generating fixtures for current JobTrak core models..."
#./manage.py dumpdata --format=json > "${ROOT_DIR}/tools/fixtures/all.json"
#echo ""

echo "--> Handling language files..."
if [ ! -f ../.tx/config ]; then
	echo "    - Skipping language file management, since it's not configured."
	echo "      You need the Transifex client configured. Visit this Web site"
	echo "      for more info: http://docs.transifex.com/developer/client/"
else
	echo "    - Regenerating messages source file, looking for new tokens..."
	./manage.py makemessages --all
	echo "    - Pushing source language to Transifex..."
	tx push -s
	echo "    - Pulling translated languages from Transifex..."
	tx pull -a
	echo "    - Compiling language files into .mo archives..."
	./manage.py compilemessages
fi

echo ""

echo "--> Generating Dynamic Wiki Docs..."
if [ ! -d ../../JobTrak.wiki ]; then
	echo "    - Skipping. JobTrak.wiki repo not found."
else
	./manage.py runscript generate_wiki
fi

echo ""
echo ""
cd ${CURRENT_DIR}
