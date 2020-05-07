#! /bin/bash
#PATH_TO_MY_VENV=/home/justin/Code/BruiserBoyz/venv_bb/bin/ #this line
PATH_TO_VENV=/venv_bb/bin/ # this line
$PATH_TO_VENV/python -c 'import sys; print(sys.version_info)' # this line
python3 -c 'import sys; print(sys.version_info)' # and this line are all just for testing python versions
source /venv_bb/bin/activate # this is to activate our virtual environment prior to
cd /usr/sb/squadbot # changing directory to where our bot lives
python3 squadbot.py # and running our bot script.

# docker run -ti -v /home/justin/Code/BruiserBoyz:/usr/sb escapebot:v0.01 bash "usr/sb/squadbot/run.sh"

