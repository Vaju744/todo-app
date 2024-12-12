#!/bin/bash
echo "Running cleanup..."
#sudo rm -rf /home/ec2-user/todo/* || true
sudo rm -rf /home/ec2-user/todo/* /home/ec2-user/todo/.[!.]*
echo "Cleanup completed."
