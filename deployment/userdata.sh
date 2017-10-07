#!/bin/bash
yum -y update
yum install epel-release -y
yum install ruby -y
yum install python35 -y
alias python='/usr/bin/python3.5'
pip install flask pylint
cd /home/ec2-user
curl -O https://aws-codedeploy-eu-west-1.s3.amazonaws.com/latest/install
chmod +x ./install
./install auto
