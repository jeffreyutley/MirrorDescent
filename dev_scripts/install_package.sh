#!/bin/bash
# This script just installs MirrorDescent along with all requirements
# for the package, demos, and documentation.
# However, it does not remove the existing installation of MirrorDescent.

conda activate MirrorDescent
cd ..
pip install -r requirements.txt
pip install -e .
pip install -r demo/requirements.txt
cd dev_scripts

