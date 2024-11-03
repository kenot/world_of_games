#!/bin/bash

# Define Docker Hub username and image name
DOCKER_USERNAME="tdinkov"
IMAGE_NAME="world_of_games-flask_app"
TAG="latest"

# Build the Docker image
echo "Building the Docker image..."
docker-compose build

# Tag the image
echo "Tagging the image..."
docker tag ${IMAGE_NAME}:latest ${DOCKER_USERNAME}/${IMAGE_NAME}:${TAG}

# Push the image to Docker Hub
echo "Pushing the image to Docker Hub..."
docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${TAG}

echo "Starting the container..."
docker-compose up

echo "Done!"
