# pylint: disable=W0614,W0401,W0611
from django.contrib.sessions.models import Session
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User, Group
from backstage.models import *
from core.models import *
from course.models import *
from account.models import *


def class_clean(classes):
    # Make sure these classes are imported
    for klass in classes:
        obj_list = eval(klass).objects.all()
        counter = 0
        for obj in obj_list:
            obj.delete()
            counter += 1
        print '%s %s(s) deleted.' % (counter, klass)
