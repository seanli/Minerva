#!/bin/sh

find -type f -name '*.pyc' -exec rm -f {} ';'
echo "Cleaned *.pyc files."
