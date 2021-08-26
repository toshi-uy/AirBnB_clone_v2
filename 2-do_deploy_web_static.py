#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local, env, run, put
import time
from os import path


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    today = time.strftime("%Y%m%d%H%M%S", time.gmtime())
    print(today)
    local("mkdir -p versions/")
    filename = "versions/web_static_" + today + ".tgz"
    try:
        local("tar -cvzf " + filename + " web_static")
        return filename
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers, using the function do_deploy"""
    
    env.hosts = ['34.75.82.215', '34.138.61.91']
    env.user = ['ubuntu']
    env.password = ['ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC8cEVnchZu0PYnKnSc\
                    YEs8tI2HxBchidGlKBjeXZ2pVnwg33aUvq7MxeSaqkA7C7cKb4mz4P1/Fg\
                    qrU4XXRmFosjxkl93cNs0dEfutAzErdeu7gOeeEza8SfUiSRo3pl7O/YJ\
                    1QBDNUhR1RipH/9fJ03rdZu+5Y5z108ZLCpgz7odhlic0v99tS99K5RgQ\
                    TP5WQzI9gtbbuUnDfwVIASLKrC4yfdPgGH5gJ2IwPqLKupoIxJMHq5ozX\
                    MU4wJ3STd63wyeoR52FQ0SoiV13AjPWcRl8Ub7T3wMMc/Ctg69UdcQnB6\
                    1MSwSVu2nTEM16x3oRlT8Mr70Zs5/cW1Y8LWv3LMnyGLkcf7MjRlttne7\
                    sfQjG8hkz0MICPdB4eoqzndomvfYnXfI5GL+xvCXZd8vG+sV52Ea95HoX\
                    BiLMTft4FFSumy5AQuZn7vO4jryvOH2P+hIg4/cAoIkDTmawBW23KDS98\
                    h7OGcqFoCjOuIw7MhErbmi4m/m6pZAreO0EzQx50SmOYJCdchvsTo3E4C\
                    HZZc3snUVP5HtqaPp19jxkHRuK1lRRfG7Mg76aok8jyQ8sN+CMTXI5Dam\
                    ECfU2e9A2l5v+60yHJEJcBNHzvLOJBakd0NKaTqIWwxBh16QK3BTrTWHS\
                    FLL13fJWrWYfmjMv9ORqf96lOEUCweCeOKcwQQ== root@c078547f2c\
                    df']
    if not archive_path:
        return False
    try:
        filename = archive_path[9:-4]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(filename))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename + ".tgz", filename))
        run("rm /tmp/{}".format(filename + ".tgz"))
        run("mv /data/web_static/releases/{1}/web_static/*\
             /data/web_static/releases/{1}}/".format(filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename))
        return True
    except:
        return False