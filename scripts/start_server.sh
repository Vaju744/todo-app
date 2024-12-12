#!/bin/bash
echo "Starting Gunicorn and Nginx services..."
sudo systemctl start gunicorn
sudo systemctl start nginx

echo "Server started successfully!"
