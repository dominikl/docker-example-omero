# OMERO.server and OMERO.web (docker-compose)

[![Actions Status](https://github.com/ome/docker-example-omero/workflows/Build/badge.svg)](https://github.com/ome/docker-example-omero/actions)

This is an example of running OMERO.server and OMERO.web in Docker.

OMERO.server is listening on the standard OMERO ports `4063` and `4064`.
OMERO.web is listening on port `4080` (http://localhost:4080/).

Log in as user `root` password `omero`.
The initial password can be changed in [`docker-compose.yml`](docker-compose.yml).


## Run

First pull the latest major versions of the containers:

    docker compose pull

Then start the containers:

    docker compose up -d
    docker compose logs -f

For more configuration options see:
- https://github.com/ome/omero-server-docker/blob/master/README.md
- https://github.com/ome/omero-web-docker/blob/master/README.md

## omero-zarr-pixel-buffer

Before spinning up the docker, adjust line https://github.com/dominikl/docker-example-omero/blob/455b64c3c4ceb609f472a4c771d49ba636a2cff8/docker-compose.yml#L34 to include the directory to your zarr files.

Spin up and get a shell:

    docker exec -it SOME_ID bash

Import only metadata:

    source /opt/omero/server/venv3/bin/activate
    /opt/omero/server/OMERO.server/bin/omero import -T Dataset:123 /zarr/SOME.ome.zarr/OME/METADATA.ome.xml

Then use extinfo.py script to set the path:

    python extinfo.py IMAGE_ID /zarr/SOME.ome.zarr/0
