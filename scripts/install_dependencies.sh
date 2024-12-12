#!/bin/bash

echo "Stopping Gunicorn and Nginx services..."
sudo systemctl stop gunicorn
sudo systemctl stop nginx
 
# Define the deployment directory dynamically
DEPLOYMENT_DIR=/opt/codedeploy-agent/deployment-root/${DEPLOYMENT_GROUP_ID}/${DEPLOYMENT_ID}/deployment-archive
 
# Clean up old files
echo "Cleaning up old files in /home/ec2-user/todo..."
sudo rm -rf /home/ec2-user/todo/*

# Copy new files from the deployment directory
echo "Copying new files from $DEPLOYMENT_DIR to /home/ec2-user/todo..."
sudo cp -r $DEPLOYMENT_DIR/* /home/ec2-user/todo
 
# Set ownership and permissions for the new files
echo "Setting permissions for /home/ec2-user/todo..."
sudo chown -R ec2-user:ec2-user /home/ec2-user/todo
sudo chmod -R 755 /home/ec2-user/todo

# Ensure necessary system packages are installed
sudo yum update -y
sudo yum install -y python3 python3-pip

cd /home/ec2-user/todo

# Install Python dependencies
pip3 install -r requirements.txt

# Run Django database migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Clean up static files before collecting them
echo "Cleaning up static files directory..."
sudo rm -rf /home/ec2-user/todo/staticfiles

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

# Start Gunicorn and Nginx services
echo "Starting Gunicorn and Nginx services..."
sudo systemctl start gunicorn
sudo systemctl start nginx
 
echo "Deployment completed successfully!"
