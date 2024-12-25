#!/bin/bash

# Build and deploy the application
echo "Starting deployment..."

# Export environment variables
export $(cat .env | xargs)

# Build Docker images
echo "Building Docker images..."
docker-compose build

# Stop existing containers
echo "Stopping existing containers..."
docker-compose down

# Start new containers
echo "Starting new containers..."
docker-compose up -d

# Run database migrations
echo "Running database migrations..."
docker-compose exec web python -c "from database import Database; db = Database(); db.connect()"

echo "Deployment complete!"
