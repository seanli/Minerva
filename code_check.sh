#!/bin/bash

echo 'Checking: account'
pylint --rcfile=tools/pylint.rc account
pep8 --repeat --ignore=E501 --exclude='migrations' account
echo 'Checking: backstage'
pylint --rcfile=tools/pylint.rc backstage
pep8 --repeat --ignore=E501 --exclude='migrations' backstage
echo 'Checking: bulletin'
pylint --rcfile=tools/pylint.rc bulletin
pep8 --repeat --ignore=E501 --exclude='migrations' bulletin
echo 'Checking: core'
pylint --rcfile=tools/pylint.rc core
pep8 --repeat --ignore=E501 --exclude='migrations' core
echo 'Checking: course'
pylint --rcfile=tools/pylint.rc course
pep8 --repeat --ignore=E501 --exclude='migrations' course
echo 'Checking: portfolio'
pylint --rcfile=tools/pylint.rc portfolio
pep8 --repeat --ignore=E501 --exclude='migrations' portfolio
echo 'Checking: data'
pylint --rcfile=tools/pylint.rc data
pep8 --repeat --ignore=E501 --exclude='migrations' data
echo 'Checking: homeroom'
pylint --rcfile=tools/pylint.rc homeroom
pep8 --repeat --ignore=E501 --exclude='migrations' homeroom
echo 'Checking: schoolax'
pylint --rcfile=tools/pylint.rc schoolax
pep8 --repeat --ignore=E501 --exclude='migrations' schoolax
