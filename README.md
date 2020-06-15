Demonstrates proxying gRPC traffic with HAProxy.

## Set Up

Be sure that you have [Docker](https://docs.docker.com/v17.12/install/) and [Docker Compose](https://docs.docker.com/compose/install/) (version 3 or newer) installed. Then, run:

Also add the google translator project key to server3 folder and update the environment variable in docker-compose.yaml
```
volumes:
- "./sample/server3/<key-file>:/etc/<key-file>"
environment:
- "GOOGLE_APPLICATION_CREDENTIALS=/etc/<key-file>"
```
Next do: 

```
sudo docker-compose build
sudo docker-compose up
```

You should see the client connect through HAProxy to the gRPC server and get a stream of "codenames".
