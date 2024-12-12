#!/bin/bash
echo "Running cleanup..."
sudo rm -rf /home/ec2-user/todo/*
sudo rm -rf /opt/codedeploy-agent/deployment-root/*
echo "Cleanup completed."
