#!/bin/bash

python2.7 /home/lisean/webapps/minerva_qa/Minerva/manage.py generate_static_dajaxice > /home/lisean/webapps/minerva_qa/Minerva/schoolax/assets/js/dajaxice.core.js
python2.7 /home/lisean/webapps/minerva_qa/Minerva/manage.py collectstatic 
/home/lisean/webapps/minerva_qa/apache2/bin/./restart
