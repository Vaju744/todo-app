#!/bin/bash

echo "Cleaning up old project files..."

# Delete old files to avoid file conflict errors
sudo rm -rf /home/ec2-user/todo/*

echo "Cleanup completed successfully."
