from haystack import indexes
from course.models import Course


class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='title')

    def get_model(self):
        return Course
