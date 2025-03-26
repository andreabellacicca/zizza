#!/bin/bash

image_name="open-webui"
container_name="open-webui"
host_port=3000
container_port=8080


docker build -t "$image_name" .
docker stop "$container_name" &>/dev/null || true
docker rm "$container_name" &>/dev/null || true

docker run -d -p "$host_port":"$container_port" \
    --add-host=host.docker.internal:host-gateway \
    -v "${image_name}:/app/backend/data" \
    --name "$container_name" \
    --restart always \
    --network host \
    "$image_name"


# ZIZZA
image_name="zizza-backend"
container_name="zizza-backend"
host_port=9000
container_port=5001


docker build -t "$image_name" backend/open_webui/zizza
docker stop "$container_name" &>/dev/null || true
docker rm "$container_name" &>/dev/null || true

docker run -d -p "$host_port":"$container_port" \
    --add-host=host.docker.internal:host-gateway \
    --name "$container_name" \
    --restart always \
    --network host \
    "$image_name"