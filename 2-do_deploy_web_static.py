#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local, env, run, put
import time
from os import path

env.hosts = ['34.75.82.215', '34.138.61.91']
env.user = ['ubuntu']


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
    """distributes an archive to your web servers, using the
    function do_deploy"""

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
