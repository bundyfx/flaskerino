#!/bin/bash
yum -y update
yum install epel-release -y
yum install ruby -y
yum install python35 -y
yum install python35-pip -y
pip-3.5 install flask pylint
iptables -A INPUT -p tcp -m multiport --dports 80,443,5000 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp -m multiport --dports 80,443,5000 -m conntrack --ctstate ESTABLISHED -j ACCEPT
cd /home/ec2-user
curl -O https://aws-codedeploy-eu-west-1.s3.amazonaws.com/latest/install
chmod +x ./install
./install auto
