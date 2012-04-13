from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from course.models import Course, CourseRating


@login_required
def courses(request, course_id=None):
    user = request.user
    context = RequestContext(request)
    try:
        course_obj = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        course_obj = None
    if course_obj is not None:
        course_ratings = CourseRating.objects.filter(course=course_obj)
        course_data = {}
        interesting_rating_sum = sum([rating.interesting_value for rating in course_ratings])
        interesting_total_ratings = course_ratings.filter(interesting_value__gt=0).count()
        if interesting_total_ratings > 0:
            course_data['interesting_average_rating'] = round(interesting_rating_sum / float(interesting_total_ratings), 2)
        else:
            course_data['interesting_average_rating'] = 0
        course_data['interesting_total_ratings'] = interesting_total_ratings
        practical_rating_sum = sum([rating.practical_value for rating in course_ratings])
        practical_total_ratings = course_ratings.filter(practical_value__gt=0).count()
        if practical_total_ratings > 0:
            course_data['practical_average_rating'] = round(practical_rating_sum / float(practical_total_ratings), 2)
        else:
            course_data['practical_average_rating'] = 0
        course_data['practical_total_ratings'] = practical_total_ratings
        difficult_rating_sum = sum([rating.difficult_value for rating in course_ratings])
        difficult_total_ratings = course_ratings.filter(difficult_value__gt=0).count()
        if difficult_total_ratings > 0:
            course_data['difficult_average_rating'] = round(difficult_rating_sum / float(difficult_total_ratings), 2)
        else:
            course_data['difficult_average_rating'] = 0
        course_data['difficult_total_ratings'] = difficult_total_ratings
        try:
            user_course_rating = CourseRating.objects.get(rater=user, course=course_obj)
        except CourseRating.DoesNotExist:
            user_course_rating = None
        course_data['user_course_rating'] = user_course_rating
        context['course'] = course_obj
        context['course_data'] = course_data
        return render_to_response('course/course_detail.html', context)
    else:
        return HttpResponse('Course Not Found!')
