#!/bin/bash

python2.7 /home/lisean/webapps/minerva/Minerva/manage.py collectstatic 
/home/lisean/webapps/minerva/apache2/bin/./restart

