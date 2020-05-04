#! /bin/bash
#PATH_TO_MY_VENV=/home/justin/Code/BruiserBoyz/venv_bb/bin/
PATH_TO_VENV=/venv_bb/bin/
$PATH_TO_VENV/python -c 'import sys; print(sys.version_info)'
python3 -c 'import sys; print(sys.version_info)'
source /venv_escbot/bin/activate
cd /usr/sb
#ls
python3 squadbot.py
