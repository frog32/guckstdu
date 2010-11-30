import os

from fabric.api import *
from fabric.contrib import files, console
from fabric import utils
from fabric.decorators import hosts

env.project = 'guckstdu'
env.project_python = 'guckstdu'
env.repository = 'git@github.com:frog32/guckstdu.git'


def _setup_path():
    env.project_root = os.path.join(env.root, env.project)
    env.code_root = os.path.join(env.project_root, env.project_python)
    env.virtualenv_root = os.path.join(env.project_root, 'env')
    env.settings = '%(project)s.settings_%(environment)s' % env


def staging():
    """ use staging environment on remote host"""
    env.user = 'www-data'
    env.environment = 'staging'
    env.hosts = ['interstate.nine.ch']
    env.root = '/var/www/domains/projects/staging'
    env.branch = 'develop'
    env.parent = 'origin'
    _setup_path()


def production():
    """ use production environment on remote host"""
    env.user = 'www-data'
    env.environment = 'production'
    env.hosts = ['interstate.nine.ch']
    env.root = '/var/www/domains/projects'
    env.branch = 'master'
    env.parent = 'origin'
    _setup_path()


def bootstrap():
    """ initialize remote host environment (virtualenv, deploy, update) """
    require('root', provided_by=('staging', 'production'))
    #run('mkdir -p %s' % os.path.join(env.root, 'log'))
    git_clone()
    create_virtualenv()
    update_requirements()
    create_symlinks()
    


def create_virtualenv():
    """ setup virtualenv on remote host """
    require('virtualenv_root', provided_by=('staging', 'production'))
    args = '--clear'
    run('virtualenv %s %s' % (args, env.virtualenv_root))

def git_pull():
    "Updates the repository."
    require('code_root', provided_by=('staging', 'production'))
    with cd(env.code_root):
        run("git pull %s %s" % (env.parent,env.branch))

def git_clone():
    "Updates the repository."
    require('root', provided_by=('staging', 'production'))
    with cd(env.root):
        run("git clone %s %s" % (env.repository, env.project))

def git_reset():
    "Resets the repository to specified version."
    run("cd ~/git/$(repo)/; git reset --hard $(hash)")

def deploy():
    """ rsync code to remote host """
    if env.environment == 'production':
        if not console.confirm('Are you sure you want to deploy production?',
                               default=False):
            utils.abort('Production deployment aborted.')
    git_pull()
    touch()

def update_requirements():
    """ update external dependencies on remote host """
    require('code_root', provided_by=('staging', 'production'))
    with cd(env.code_root):
        cmd = ['pip install']
        cmd += ['-E %(virtualenv_root)s' % env]
        cmd += ['--requirement %s' % 'REQUIREMENTS']
        run(' '.join(cmd))

def syncdb():
    """runs syncdb on the remote host"""
    require('code_root', provided_by=('staging', 'production'))
    manage = os.path.join(env.code_root, 'manage.py')
    with cd(env.project_root):
        run('./env/bin/python %s syncdb' % (manage))


def migrate():
    """migrates all apps on the remote host"""
    require('code_root', provided_by=('staging', 'production'))
    manage = os.path.join(env.code_root, 'manage.py')
    with cd(env.project_root):
        run('./env/bin/python %s migrate' % (manage,))
    touch()

def compilemessages():
    """compiles all translations"""
    require('code_root', provided_by=('staging', 'production'))
    manage = './manage.py'
    with cd(env.code_root):
        run('../env/bin/python %s compilemessages --settings=settings' % (manage,))

def create_symlinks():
    """ create settings feincms and admin media links"""
    require('code_root', provided_by=('staging', 'production'))
    mediafolder = os.path.join(env.code_root, 'media')
    with cd(env.project_root):
        run('ln -s %s.wsgi apache.wsgi' % env.environment)
    with cd(env.code_root):
        run('ln -s settings_%s.py settings.py' % env.environment)
    with cd(mediafolder):
        run('ln -s ../../env/lib/python2.5/site-packages/django/contrib/admin/media/ admin && \
ln -s ../../env/lib/python2.5/site-packages/feincms/media/feincms/ feincms')

def touch():
    """ touch wsgi file to trigger reload """
    require('code_root', provided_by=('staging', 'production'))
    with cd(env.project_root):
        run('touch apache.wsgi')
