#!/bin/bash
echo "Starting tf_container"
exec docker-compose -f ../.docker/docker-compose.yml up -d
echo "tf_container started"

echo "run following command to go inside container 'docker exec -it tf_container bash'"