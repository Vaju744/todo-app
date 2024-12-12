#!/bin/bash

echo "Stopping Gunicorn and Nginx services..."
sudo systemctl stop gunicorn
sudo systemctl stop nginx

# Define the deployment directory dynamically
#DEPLOYMENT_DIR=/opt/codedeploy-agent/deployment-root/${DEPLOYMENT_GROUP_ID}/${DEPLOYMENT_ID}/deployment-archive

# Check if the deployment directory exists
#if [ ! -d "$DEPLOYMENT_DIR" ]; then
 # echo "Deployment directory does not exist: $DEPLOYMENT_DIR"
#  exit 1
#fi

# Clean up old files while preserving the scripts directory
#echo "Cleaning up old files in /home/ec2-user/todo but preserving scripts directory..."
#sudo find /home/ec2-user/todo -mindepth 1 ! -name "scripts" -exec rm -rf {} +

# Copy new files from the deployment directory
#echo "Copying new files from $DEPLOYMENT_DIR to /home/ec2-user/todo..."
#sudo cp -r $DEPLOYMENT_DIR/* /home/ec2-user/todo

# Ensure necessary system packages are installed
sudo yum update -y
sudo yum install -y python3 python3-pip

cd /home/ec2-user/todo

# Install Python dependencies
pip3 install -r requirements.txt

# Set ownership and permissions for the new files
echo "Setting permissions for /home/ec2-user/todo..."
sudo chown -R ec2-user:ec2-user /home/ec2-user/todo
sudo chmod -R 755 /home/ec2-user/todo

# Run Django database migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

# Start Gunicorn and Nginx services
echo "Starting Gunicorn and Nginx services..."
sudo systemctl start gunicorn
sudo systemctl start nginx

echo "Deployment completed successfully!"
