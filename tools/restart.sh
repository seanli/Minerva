#!/bin/bash

python2.7 ../manage.py collectstatic 
/home/lisean/webapps/minerva/apache2/bin/./restart

