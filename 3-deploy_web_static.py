#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local, env, run, put
import time
from os import path

env.hosts = ['34.75.82.215', '34.138.61.91']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    today = time.strftime("%Y%m%d%H%M%S", time.gmtime())
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

    if path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            file_name = archive_path.split("/")[1]
            file_name2 = file_name.split(".")[0]
            final_name = "/data/web_static/releases/" + file_name2 + "/"
            run("mkdir -p " + final_name)
            run("tar -xzf /tmp/" + file_name + " -C " + final_name)
            run("rm /tmp/" + file_name)
            run("mv " + final_name + "web_static/* " + final_name)
            run("rm -rf " + final_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + final_name + " /data/web_static/current")
            print("New version deployed!")
            return True
        except:
            return False
    else:
        return False


def deploy():
    """creates and distributes an archive to your web servers,
    using the function deploy"""
    filepath = do_pack()
    if filepath is None:
        return False
    answ = do_deploy(filepath)
    return answ
