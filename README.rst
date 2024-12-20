MirrorDescent
=============

An implementation of Mirror Descent from Chapter 9 of "First-Order Methods in Optimization" by Amir Beck

This is the final project for MA 75400 at Purdue University (course webpage
https://www.math.purdue.edu/~zhan1966/teaching/574/index.html), taught by Prof. Xiangxiong Zhang. The demo files
contain examples of Mirror Descent.

This GitHub repository is based on the package_template repository (https://github.com/gbuzzard/package_template)
created by Prof. Greg Buzzard at Purdue University.

Installing
----------
1. *Clone or download the repository:*

    .. code-block::

        git clone git@github.com:jeffreyutley/MirrorDescent

2. Install the conda environment and package

    a. Option 1: Clean install from dev_scripts

        *******You can skip all other steps if you do a clean install.******

        To do a clean install, use the command:

        .. code-block::

            cd dev_scripts
            source clean_install_all.sh

    b. Option 2: Manual install

        1. *Create conda environment:*

            Create a new conda environment named ``MirrorDescent`` using the following commands:

            .. code-block::

                conda create --name MirrorDescent python=3.11
                conda activate MirrorDescent
                pip install -r requirements.txt

            Anytime you want to use this package, this ``MirrorDescent`` environment should be activated with the following:

            .. code-block::

                conda activate MirrorDescent


        2. *Install MirrorDescent package:*

            Navigate to the main directory ``MirrorDescent/`` and run the following:

            .. code-block::

                pip install .

            To allow editing of the package source while using the package, use

            .. code-block::

                pip install -e .


Running Demo(s)
---------------

Run any of the available demo scripts with something like the following:

    .. code-block::

        python demo/<demo_file>.py

