#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
import time
from os import path


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    today = time.strftime("%Y%m%d%H%M%S", time.gmtime())
    print(today)
    local("mkdir -p versions/")
    filename = "versions/web_static_" + today + ".tgz"
    try:
        local("tar -cvzf " + filename + "web_static")
        return filename
    except:
        return None
