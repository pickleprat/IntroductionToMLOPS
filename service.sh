#!/bin/bash

for i in {1..10}; do
  if curl -s http://localhost:8000/; then
    echo "Service is up!"
    break
  fi
  echo "Waiting for service to start..."
  sleep 5
done
