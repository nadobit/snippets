# -*- coding: utf-8 -*-
import os
from fabric import colors
from fabric.api import env, task, lcd, local, roles, cd, run, prefix

BASE_DIR = os.path.dirname(__file__)
DJANGO_DIR = os.path.join(BASE_DIR, 'source')

DEBIAN_USERNAME = 'XXXXXXXXXXXXXXXXXXXXXXX'

env.roledefs = {
    'web': ['root@asdasdasdasdasdsadadasd'],
}


def lcd_basedir(subdir=DJANGO_DIR):
    path = os.path.dirname(env.real_fabfile)
    if subdir:
        path = os.path.join(path, subdir)
    return lcd(path)


# Live System operations ------------------------------------------------------


@task
@roles('web')
def deploy():
    deploy_webserver()


# Inner cals ------------------------------------------------------------------


def deploy_webserver():

    print(colors.green("stopping uwsgi"))
    run("service uwsgi stop")

    with cd('/home/%s/server' % DEBIAN_USERNAME):

        print(colors.green("updating git repository"))
        run('su %s -c "git pull"' % DEBIAN_USERNAME)

        print(colors.green("cleaning python tmp files"))
        run('find . -name \*.pyc -delete')

        with prefix('source /home/%s/.virtualenvs/%s/bin/activate' % (DEBIAN_USERNAME, DEBIAN_USERNAME)):

            print(colors.green("install required python packages"))
            run("TMPDIR=/home/%s/tmp pip install -q -r requirements/freezed/production.txt" % (DEBIAN_USERNAME, ))

            print(colors.green("migrating models"))
            run("python ./%s/manage.py migrate" % (DEBIAN_USERNAME, ))

            print(colors.green("compiling locales"))
            run("django-admin compilemessages")

            print(colors.green("collecting static files"))
            run("python ./%s/manage.py collectstatic --noinput" % (DEBIAN_USERNAME, ))

    print(colors.green("starting uwsgi"))
    run("service uwsgi start")

    print(colors.green("reloading nginx"))
    if run("service nginx reload", warn_only=True).failed:
        run("service nginx restart")

    print(colors.green(""))
    print(colors.red("❤️  ready"))


# Helper ----------------------------------------------------------------------


@task
def req(update=False):
    with lcd_basedir():
        local('pip install -%sr ../requirements/common.txt' % (
            'U' if update else ''
        ))
        local('pip freeze > ../requirements/freezed.dev.txt')


@task
def log():
    with lcd_basedir(BASE_DIR):
        local('git log --pretty=format:\'%B\' --graph > changelog.txt')


@task
def clean():
    with lcd_basedir(''):
        local('find . -name \*.pyc -print -delete')
        local('find . -name __pycache__ -print -delete')


@task
def pipu():
    if env.host is not None:
        return

    with lcd_basedir():
        local("pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U")


# Local only tasks ------------------------------------------------------------


@task
def go(*args):

    pub = 'pub' in args

    with lcd_basedir():
        print(colors.green("Starting Server..."))

        local('python manage.py runserver %s' % (
            '0.0.0.0:8000' if pub else '',
        ))


@task
def lng():
    if env.host is not None:
        return

    with lcd_basedir(''):
        local('django-admin makemessages --ignore .virtualenv --ignore fixtures -a --no-location')
        local('django-admin compilemessages')


@task
def mam():
    if env.host is not None:
        return

    with lcd_basedir():
        local('python manage.py makemigrations')
        local('python manage.py migrate')
