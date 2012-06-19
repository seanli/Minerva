from haystack import indexes
from course.models import Course


class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Course

    def index_queryset(self):
        """ Used when the entire index for model is updated. """
        return self.get_model().objects.all()
