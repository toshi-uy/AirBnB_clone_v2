# Puppet for setup - Redo the task #0 but by using Puppet:

exec {'Nginx':
     command  => 'sudo apt-get update; sudo apt-get install nginx -y',
     provider => shell
}

exec {'folders':
     command  => 'sudo mkdir -p /data/web_static/releases/test/ && sudo mkdir -p /data/web_static/shared/',
     provider => shell,
     require  => Exec['Nginx']
}

exec {'index':
     command  => 'echo "Holberton School" > /data/web_static/releases/test/index.html',
     provider => shell,
     require  => Exec['folders']
}

exec {'Soft Link':
     command  => 'ln -sf /data/web_static/releases/test /data/web_static/current',
     provider => shell,
     require  => Exec['index']
}

exec {'chown':
     command  => 'sudo chown -hR ubuntu:ubuntu /data/',
     provider => shell,
     require  => Exec['Soft Link']
}

exec {'Location':
     command  => 'printf %s "server {
          location /hbnb_static/ {
               alias /data/web_static/current/;
          }
     }" > /etc/nginx/sites-available/default',
     provider => shell,
     require  => Exec['chown']
}

exec {'Restart':
     command  => 'service nginx restart',
     provider => shell,
     require  => Exec['Location']
}
