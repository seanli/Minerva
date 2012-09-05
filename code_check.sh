#!/bin/bash

for i in account backstage bulletin core course portfolio data homeroom schoolax
do
	echo "Checking: $i"
	pylint --rcfile=tools/pylint.rc $i
	pep8 --repeat --ignore=E501,E128,E124 --exclude='migrations' $i
done
