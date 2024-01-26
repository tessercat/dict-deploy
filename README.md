# Debian stack

This repo contains Ansible roles
to install the [`dict-web`](http://github.com/tessercat/dict-web) site
on the [`stack-deploy`](https://github.com/tessercat/stack-deploy) stack.

Dictionary entries are copied and pasted from Kroll
into `var/data/kroll.txt` and imported by hand.

    cd /opt/dictionary/web
    . var/venv/activate
    python manage.py importdictionary
