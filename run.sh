#!/bin/bash

image_name="zizza-ui"
container_name="zizza-ui"
host_port=8080
container_port=8080


docker build -t "$image_name" zizza-ui
docker stop "$container_name" &>/dev/null || true
docker rm "$container_name" &>/dev/null || true

docker run -d -p "$host_port":"$container_port" \
    --add-host=host.docker.internal:host-gateway \
    -v "${image_name}:/app/backend/data" \
    --name "$container_name" \
    --restart always \
    --network host \
    "$image_name"


image_name="zizza-blockchain-intents-server"
container_name="zizza-blockchain-intents-server"
host_port=5001
container_port=5001


docker build -t "$image_name" zizza-blockchain-intents-server
docker stop "$container_name" &>/dev/null || true
docker rm "$container_name" &>/dev/null || true

docker run -d -p "$host_port":"$container_port" \
    --add-host=host.docker.internal:host-gateway \
    --name "$container_name" \
    --restart always \
    --network host \
    "$image_name"