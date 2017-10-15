sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/django.py /etc/gunicorn.d/django.py
sudo /etc/init.d/gunicorn restart﻿﻿

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'admin'@'localhost'"
mysql -uroot -e "SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('admin')"
mysql -uroot -e "CREATE DATABASE qa"
mysql -uroot -e "GRANT ALL ON qa.* TO 'admin'@'localhost'"
cd /home/box/web/ask
sudo python manage.py makemigrations qa
sudo python manage.py migrate