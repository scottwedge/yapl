#!/bin/bash

exec docker-compose -f ../.docker/docker-compose.yml up -d
exec docker exec -it tf_container bash