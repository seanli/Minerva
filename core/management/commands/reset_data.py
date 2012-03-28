from django.contrib.sessions.models import Session
from django.contrib.admin.models import LogEntry
from backstage.models import LogMessage, Wiki, Ticket
from core.models import Badge, Institute
from course.models import Section, Review
from account.models import Profile
from django.contrib.auth.models import User, Group
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):

    help = 'Resets database with essential data.'

    def handle_noargs(self, **options):
        users = User.objects.all()
        counter = 0
        for user in users:
            user.delete()
            counter += 1
        print '%s user(s) deleted.' % counter
        user = User()
        user.username = 'admin'
        user.email = 'admin@schoolax.com'
        user.set_password('1990106')
        user.first_name = 'Admin'
        user.last_name = 'Schoolax'
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        profile = Profile()
        profile.user = user
        profile.institute = Institute.objects.get(name='University of Waterloo')
        profile.role = 'S'
        profile.save()
        print 'Superuser created.'
        groups = Group.objects.all()
        counter = 0
        for group in groups:
            group.delete()
            counter += 1
        print '%s group(s) deleted.' % counter
        wikis = Wiki.objects.all()
        counter = 0
        for wiki in wikis:
            wiki.delete()
            counter += 1
        print '%s wiki(s) deleted.' % counter
        tickets = Ticket.objects.all()
        counter = 0
        for ticket in tickets:
            ticket.delete()
            counter += 1
        print '%s ticket(s) deleted.' % counter
        badges = Badge.objects.all()
        counter = 0
        for badge in badges:
            badge.delete()
            counter += 1
        print '%s badges(s) deleted.' % counter
        sections = Section.objects.all()
        counter = 0
        for section in sections:
            section.delete()
            counter += 1
        print '%s section(s) deleted.' % counter
        reviews = Review.objects.all()
        counter = 0
        for review in reviews:
            review.delete()
            counter += 1
        print '%s review(s) deleted.' % counter
        sessions = Session.objects.all()
        counter = 0
        for session in sessions:
            session.delete()
            counter += 1
        print '%s session(s) deleted.' % counter
        counter = 0
        admin_logs = LogEntry.objects.all()
        for admin_log in admin_logs:
            admin_log.delete()
            counter += 1
        print '%s admin log(s) deleted.' % counter
        counter = 0
        log_messages = LogMessage.objects.all()
        for log_message in log_messages:
            log_message.delete()
            counter += 1
        print '%s log message(s) deleted.' % counter
