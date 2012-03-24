#!/bin/bash

python2.7 /home/lisean/webapps/minerva/Minerva/manage.py generate_static_dajaxice > /home/lisean/webapps/minerva/Minerva/schoolax/assets/js/dajaxice.core.js
python2.7 /home/lisean/webapps/minerva/Minerva/manage.py collectstatic 
/home/lisean/webapps/minerva/apache2/bin/./restart

