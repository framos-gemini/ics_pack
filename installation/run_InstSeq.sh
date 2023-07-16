#!/bin/bash

# The $HOME is a enviroment variable defined on linux with user script execution path. 
#HOME=/home/ics
echo $USER
echo $HOME
source /home/$USER/.bashrc
conda activate igos2n
PYTHONBIN=$HOME/miniconda3/envs/igos2n/bin/python
cd $HOME/giapi-gluecc
source ./defineGiapiglueEnv.sh

$PYTHONBIN $HOME/ics_pack/code/InstSeq/InstSeq.py



