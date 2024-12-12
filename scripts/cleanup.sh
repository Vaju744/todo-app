#!/bin/bash
echo "Running cleanup..."
sudo rm -rf /home/ec2-user/todo/* || true
echo "Cleanup completed."
