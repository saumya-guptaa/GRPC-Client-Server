#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/saumya/Downloads/sample1-280419-d0c1e2c533c6.json"
cd server/
sudo service haproxy restart
python3 speech_server.py | gnome-terminal --command="bash -c 'export GOOGLE_APPLICATION_CREDENTIALS="/home/saumya/Downloads/sample1-280419-d0c1e2c533c6.json"; python3 translator_server.py; $SHELL'" | gnome-terminal --command="bash -c 'export GOOGLE_APPLICATION_CREDENTIALS="/home/saumya/Downloads/sample1-280419-d0c1e2c533c6.json"; python3 translator_server1.py; $SHELL'" | gnome-terminal --command="bash -c 'export GOOGLE_APPLICATION_CREDENTIALS="/home/saumya/Downloads/sample1-280419-d0c1e2c533c6.json"; python3 translator_server2.py; $SHELL'" | gnome-terminal --command="bash -c 'cd ../client ;python3 client.py; $SHELL'"
