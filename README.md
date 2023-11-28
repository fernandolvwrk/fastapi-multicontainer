This is an example of fastAPI application in multiple Docker container setup.

The system is made of:
- a primary fastAPI webapp that exposes three services.
- a secondary fastAPI webapp that exposes two services.

The "hidden" service of the primary webapp uses one of the services of the secondary webapp
through the internal network that joins both containers.

The system may be configured so that the services of the secondary webapp are accessible from
the outside or that they remain hidden, being accessible only through the internal network.



To run the app on your local instance of Docker use:
> docker compose up --build

To test the app:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/ping
- http://127.0.0.1:8000/hidden

Uncomment ports section in docker.compose.yml to allow external access to secondary app services:
- http://127.0.0.1:8001
- http://127.0.0.1:8001/secondaryping
