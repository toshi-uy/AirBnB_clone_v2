#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
apt-get upodate
apt-get install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/

printf %s "server {
    location /hbnb_static/ {
        alias /data/web_static/current/;
        autoindex off;
    }
}" > /etc/nginx/sites-available/default                           
service nginx restart
