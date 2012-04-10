from django.contrib.auth.models import User
from core.models import (SkillRating, SpecializationAssign,
    SkillAssign)
from course.models import SectionAssign


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


def add_specialization(self, specialization):
    assign = SpecializationAssign()
    assign.specialization = specialization
    assign.user = self
    assign.save()
User.add_to_class('add_specialization', add_specialization)


def has_specialization(self, specialization):
    return SpecializationAssign.objects.filter(specialization=specialization, user=self).count() > 0
User.add_to_class('has_specialization', has_specialization)


def add_skill(self, skill):
    assign = SkillAssign()
    assign.skill = skill
    assign.user = self
    assign.save()
User.add_to_class('add_skill', add_skill)


def has_skill(self, skill):
    return SkillAssign.objects.filter(skill=skill, user=self).count() > 0
User.add_to_class('has_skill', has_skill)


def add_section(self, section):
    assign = SectionAssign()
    assign.section = section
    assign.user = self
    assign.save()
User.add_to_class('add_section', add_section)


def has_section(self, section):
    return SectionAssign.objects.filter(section=section, user=self).count() > 0
User.add_to_class('has_section', has_section)


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
