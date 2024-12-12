#!/bin/bash
echo "Stopping Gunicorn and Nginx services..."
sudo systemctl stop gunicorn
sudo systemctl stop nginx
 
#To  Define the dynamic deployment directory
#DEPLOYMENT_DIR=/opt/codedeploy-agent/deployment-root/${DEPLOYMENT_GROUP_ID}/${DEPLOYMENT_ID}/deployment-archive
 
# Clean up old files
echo "Cleaning up old files in /home/ec2-user/todo..."
sudo rm -rf /home/ec2-user/todo/*
 
# Copy new files from the dynamic deployment directory
#echo "Copying new files from $DEPLOYMENT_DIR to /home/ec2-user/todo..."
#sudo cp -r $DEPLOYMENT_DIR/* /home/ec2-user/todo
 
sudo yum update -y
sudo yum install -y python3 python3-pip
cd /home/ec2-user/todo
 
pip3 install -r requirements.txt
 
echo "Setting ownership and permissions for /home/ec2-user/todo..."
sudo chown -R ec2-user:ec2-user /home/ec2-user/todo
sudo chmod -R 755 /home/ec2-user/todo
# Set proper permissions to access directoryies and files
#echo "Setting ownership and permissions for /home/ec2-user/todo..."
 
python3 manage.py makemigrations
python3 manage.py migrate
 
python3 manage.py collectstatic --noinput
 
echo "Starting Gunicorn and Nginx services..."
sudo systemctl start gunicorn
sudo systemctl start nginx
 
echo "Deployment completed successfully!"