#!/bin/bash

sudo yum update -y

sudo yum install -y python3 python3-pip

cd /home/ec2-user/todo

pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py collectstatic --noinput
