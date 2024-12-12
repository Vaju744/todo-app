#!/bin/bash

echo "Cleaning up old files..."
sudo rm -rf /home/ec2-user/todo/*
sudo rm -rf /home/ec2-user/todo/sonar-scanner-5.0.1.3006-linux || true
echo "Cleanup completed successfully."
