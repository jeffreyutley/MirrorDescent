#!/bin/bash

source remove_package.sh
source install_conda_environment.sh

source install_package.sh

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "Use"
echo "${red}   conda activate MirrorDescent   ${reset}"
echo "to activate the conda environment."
echo " "
