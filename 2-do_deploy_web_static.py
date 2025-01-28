#!/usr/bin/python3
"""
   Script that distributes the web_static archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['34.204.101.197', '75.101.179.225']

def do_deploy(archive_path):
    """Method distributes an archive to the web servers
    """
    if exists(archive_path) is False:
        return False
    try:
        file_p = archive_path.split("/")[-1]
        no_ext = file_p.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_p, path, no_ext))
        run('rm /tmp/{}'.format(file_p))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
