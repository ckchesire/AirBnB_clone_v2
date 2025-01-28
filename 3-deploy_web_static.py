#!/usr/bin/python3
"""
   Module based on the fab file 2-do_deploy_web_static.py that creates and
   distributes an archive to the web servers

   usage: fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""


from datetime import datetime
from fabric.api import env, local, put, run
from os.path import exists, isdir
env.hosts = ['34.204.101.197', '75.101.179.225']


def do_pack():
    """Method that generates .tgz archive on web_static folder
    """
    try:
        time = datetime.now()
        archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
        if isdir("versions") is False:
            local("mkdir versions")
        local('tar -cvzf versions/{} web_static'.format(archive))
        return archive
    except Exception:
        return None


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
    except FileNotFoundError:
        return False


def deploy():
    """Function to create and distribute an archive to the web servers
    """
    archive_folder = do_pack()
    if archive_folder is None:
        return False
    return do_deploy(archive_folder)
