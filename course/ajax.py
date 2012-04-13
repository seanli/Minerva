from dajaxice.decorators import dajaxice_register
from django.contrib.auth.decorators import login_required
from course.models import Course
from django.utils import simplejson


@dajaxice_register
@login_required
def rate_course(request, course_id, interesting_rating=None, practical_rating=None, difficult_rating=None):
    status = 'OK'
    user = request.user
    try:
        course = Course.objects.get(id=course_id)
        user.rate_course(course, interesting_rating, practical_rating, difficult_rating)
    except Course.DoesNotExist:
        status = 'INVALID'
    return simplejson.dumps({'status': status})
