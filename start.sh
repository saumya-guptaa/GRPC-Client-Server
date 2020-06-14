#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/saumya/Downloads/GPRC-00f2e673070c.json"
cd server/
sudo service haproxy restart
python3 speech_server.py | gnome-terminal --command="bash -c 'export GOOGLE_APPLICATION_CREDENTIALS="/home/saumya/Downloads/GPRC-00f2e673070c.json"; python3 translator_server.py; $SHELL'" | gnome-terminal --command="bash -c 'cd ../client ;python3 client.py; $SHELL'"