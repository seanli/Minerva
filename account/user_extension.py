from django.contrib.auth.models import User
from core.models import SkillRating


# Adding functions to User class

def user_role(self):
    return self.get_profile().get_role_display()
user_role.short_description = 'Role'
User.add_to_class('user_role', user_role)


def user_institute(self):
    return '<a href="/admin/core/institute/%s/" target="_blank">%s</a>' % (self.get_profile().institute.id, self.get_profile().institute)
user_institute.allow_tags = True
user_institute.short_description = 'Institute'
User.add_to_class('user_institute', user_institute)


def rate_skill(self, skill_assign, rating):
    try:
        skill_rating = SkillRating.objects.get(rater=self, skill_assign=skill_assign)
    except SkillRating.DoesNotExist:
        skill_rating = SkillRating()
        skill_rating.rater = self
        skill_rating.skill_assign = skill_assign
    skill_rating.value = rating
    skill_rating.save()
User.add_to_class('rate_skill', rate_skill)
