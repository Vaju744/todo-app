#!/bin/bash

echo "Running cleanup before deployment..."
sudo rm -rf /home/ec2-user/todo/sonar-scanner-5.0.1.3006-linux || true
sudo rm -rf /home/ec2-user/todo/* || true
echo "Cleanup completed."
