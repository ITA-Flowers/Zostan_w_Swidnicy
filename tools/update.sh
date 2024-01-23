#!/bin/bash
#
# Script for updating actual software to the latest version from Github service
#

GROUP=`groups | cut -d ' ' -f 1`

PROJECT_NAME='Zostan_w_Swidnicy'

ROOT_DIR='/srv/Swidnica'
WORK_DIR="${ROOT_DIR}/${PROJECT_NAME}"
SCRIPT_DIR_PROJECT="$WORK_DIR/software/tools"
SCRIPT_DIR_LOCAL="$HOME/Swidnica_Scripts"

GITHUB_URL="https://github.com/ITA-Flowers/${PROJECT_NAME}.git"

echo " [*] Updating App <#Zostan_w_Swidnicy>"

echo "     [-] Checking root directory (${ROOT_DIR})..."
if [[ -d "$ROOT_DIR" ]]; then
	echo "        [+] Directory exists."
else
	echo "        [+] Directory does not exists! Creating..."
	echo "        [CMD] sudo mkdir ${ROOT_DIR} && sudo chgrp $GROUP $ROOT_DIR && sudo chown $USER $ROOT_DIR"
	sudo mkdir ${ROOT_DIR} && sudo chgrp $GROUP $ROOT_DIR && sudo chown $USER $ROOT_DIR
	if [ ! $? -eq 0 ]; then
		echo "     [!] Something went wrong!"
		kill $$ 1
	fi
fi

echo "     [-] Checking work directory ($WORK_DIR)..."
if [[ -d "${WORK_DIR}" ]]; then
	echo "        [+] Workdir ($WORK_DIR) exists :: Pulling changes..."
	GIT_CMD='git pull --rebase'
	cd $WORK_DIR
else
	echo "        [+] Workdir ($WORK_DIR) does not exists :: Cloning repository..."
	GIT_CMD="git clone ${GITHUB_URL}"
	cd $ROOT_DIR
fi

echo "        [CMD] $GIT_CMD"
echo
$GIT_CMD

echo "     [-] Checking local scripts directory (${SCRIPT_DIR_LOCAL})..."
if [[ ! -d $SCRIPT_DIR_LOCAL ]]; then
	echo "        [+] Directory does not exists! Creating..."
	echo "        [CMD] sudo mkdir ${SCRIPT_DIR_LOCAL}"
	sudo mkdir ${SCRIPT_DIR_LOCAL}
fi

echo "     [-] Checking project scripts directory (${SCRIPT_DIR_PROJECT})..."
if [[ ! -d $SCRIPT_DIR_PROJECT ]]; then
	echo "        [!] Directory does not exists!"
	echo " [!] Something went wrong!"
	exit 1
else
	echo "        [+] Directory exists :: Updating scripts..."
	echo "     [CMD] cp ${SCRIPT_DIR_PROJECT}/* ${SCRIPT_DIR_LOCAL}/"
	cp ${SCRIPT_DIR_PROJECT}/* ${SCRIPT_DIR_LOCAL}/
fi

echo "     [-] Granting permissions to scripts..."
for file in ${SCRIPT_DIR_LOCAL}/*; do
	if [[ -f $file ]]; then
		echo "        [CMD] chmod u=rwx,g=rx,o=r $file"
		chmod u=rwx,g=rx,o=r $file
	fi
done

if [ $? -eq 0 ]; then
	echo
	echo " [*] Repository updated successfully!"
	exit 0
else
	echo
	echo " [!] Something went wrong!"
	exit 1
fi
