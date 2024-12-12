#!/bin/bash
echo "Running cleanup..."
sudo rm -rf /home/ec2-user/todo/* || true
sudo rm -f /home/ec2-user/todo/.pylintrc || true
sudo rm -rf /home/ec2-user/todo/sonar-scanner-5.0.1.3006-linux || true
echo "Cleanup completed."

