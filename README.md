# Client-Server Application Using GRPC

[![Generic badge](https://img.shields.io/badge/GRPC-Python-<BLUE>.svg)](https://shields.io/)

## Setup

Make Sure to install python3, grpc for python.

Be sure that you have [Google Cloud Translator](https://cloud.google.com/translate/docs/basic/setup-basic) and [Google Cloud Speech to Text Translator](https://pypi.org/project/google-cloud-speech/) enabled on your google cloud.

1. Install all the Python libraries and dependencies needed.

2. Copy Haproxy configuration to specified location.
    ```
    sudo cp /path/to/haproxy.cnf /etc/haproxy
    ```

3. Copy Haproxy Credentials to specific location.
    ```
    sudo cp /path/to/(example).cert /etc/ssl/creds
    sudo cp /path/to/(example).pem /etc/ssl/private
    ```

4. Set Google Cloud Authentication Credentials.
    ```
    export GOOGLE_APPLICATION_CREDENTIALS=path\to\json\file.
    ```

5. Start Haproxy
    ```
    sudo service haproxy restart
    ```

6. Start Translator Server
    ```
    cd /GRPC-Client-Server/server/
    python3 translator_server.py
    ```

7.  In another terminal start Speech to Text Translator Server
    ```
    cd /GRPC-Client-Server/server/
    python3 speech_server.py
    ```
8. In another terminal start Client
    ```
    cd /GRPC-Client-Server/client/
    python3 client.py
    ```

You can see a Client-Server Application Running
Output received with also be stored in a file at location "/GRPC-Client-Server/client/result.txt"