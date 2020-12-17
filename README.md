# Deployment

[README_PREVIOUS.md](./README_PREVIOUS.md)


## Standalone VM using uWSGi
Requirements:
* uWSGI https://uwsgi-docs.readthedocs.io/en/latest/
* apache

Instalation of requirements:
```
# sudo apt-get install uwsgi
# apt-get install uwsgi-plugin-python
# apt-get install python3
# apt-get install python3-venv
apt-get install build-essential python3-dev
# sudo apt-get install apache2 libapache2-mod-wsgi
```

## Clone repo from github
Result:
```
www@ubuntu-s-1vcpu-1gb-fra1-01:/srv/ml_runner$ ll /srv/ml_runner/
total 48
drwxr-xr-x 5 www  www  4096 Dec 17 02:24 ./
drwxr-xr-x 3 root root 4096 Dec 17 02:24 ../
drwxr-xr-x 8 www  www  4096 Dec 17 02:24 .git/
-rw-r--r-- 1 www  www   415 Dec 17 02:24 .gitignore
-rw-r--r-- 1 www  www   800 Dec 17 02:24 INSTRUCTIONS_TO_COPY.md
-rw-r--r-- 1 www  www  1294 Dec 17 02:24 README.md
-rw-r--r-- 1 www  www  1174 Dec 17 02:24 README_PREVIOUS.md
drwxr-xr-x 2 www  www  4096 Dec 17 02:24 auxilary_code/
-rw-r--r-- 1 www  www   169 Dec 17 02:24 environment_template.env
-rw-r--r-- 1 www  www    68 Dec 17 02:24 main.py
drwxr-xr-x 5 www  www  4096 Dec 17 02:24 ml_runner/
-rw-r--r-- 1 www  www   955 Dec 17 02:24 requirements.txt
www@ubuntu-s-1vcpu-1gb-fra1-01:/srv/ml_runner$ git pull
Already up to date.
```

`www` user is owner

## uWSGI deployment
https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/#uwsgi

### Create env
```
(ml_runner_env) www@ubuntu-s-1vcpu-1gb-fra1-01:/srv/ml_runner$ python3 -m venv ~/.envs/ml_runner_env
(ml_runner_env) www@ubuntu-s-1vcpu-1gb-fra1-01:/srv/ml_runner$ source ~/.envs/ml_runner_env/bin/activate
(ml_runner_env) www@ubuntu-s-1vcpu-1gb-fra1-01:/srv/ml_runner$ pip install -r requirements.txt
...
(ml_runner_env) www@ubuntu-s-1vcpu-1gb-fra1-01:/srv/ml_runner$ pip install uwsgi
...
```

### And run uwsgi
```
(ml_runner_env) www@ubuntu-s-1vcpu-1gb-fra1-01:/srv/ml_runner$ source ./deployment/environment.env 
(ml_runner_env) www@ubuntu-s-1vcpu-1gb-fra1-01:/srv/ml_runner$ uwsgi --http 0.0.0.0:5000 --module ml_runner:app
```

And http://46.101.133.20:5000/api/v1/users/ works

## But it should be handled by proper server (Nginx or Apache)
**It's important to have ssl certificate configured**
