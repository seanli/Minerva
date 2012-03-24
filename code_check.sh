#!/bin/bash

echo 'Pylint: account'
pylint --rcfile=tools/pylint.rc account
echo 'Pylint: backstage'
pylint --rcfile=tools/pylint.rc backstage
echo 'Pylint: bulletin'
pylint --rcfile=tools/pylint.rc bulletin
echo 'Pylint: core'
pylint --rcfile=tools/pylint.rc core
echo 'Pylint: course'
pylint --rcfile=tools/pylint.rc course
echo 'Pylint: crowd'
pylint --rcfile=tools/pylint.rc crowd
echo 'Pylint: data'
pylint --rcfile=tools/pylint.rc data
echo 'Pylint: homeroom'
pylint --rcfile=tools/pylint.rc homeroom
echo 'Pylint: schoolax'
pylint --rcfile=tools/pylint.rc schoolax
echo 'PEP8'
pep8 --repeat --ignore=E501 --exclude='migrations' .
