sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/django.py /etc/gunicorn.d/django.py
sudo /etc/init.d/gunicorn restart﻿﻿

sudo gunicorn -c /home/box/web/etc/hello.py hello:app --daemon
sudo gunicorn -c /home/box/web/etc/django.py ask.wsgi:application --daemon