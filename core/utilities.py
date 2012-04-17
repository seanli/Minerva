from django.contrib.auth.models import User
import random


def titlecase(text):
    words = text.split(' ')
    capitalized_words = []
    for word in words:
        title_case_word = word[0].upper() + word[1:].lower()
        capitalized_words.append(title_case_word)
    merged = ' '.join(capitalized_words)
    return merged


def generate_random_string(min_length, max_length):
    ret = ''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(max_length)])
    return ret[:random.randint(min_length, max_length)]


def generate_username():
    min_length = 6
    max_length = 30
    random_string = generate_random_string(min_length, max_length)
    user = User.objects.filter(username=random_string)
    while user:
        random_string = generate_random_string(min_length, max_length)
        user = User.objects.filter(username=random_string)
    return random_string


def set_referrer(request, referrer):
    request.session['referrer'] = referrer


def get_referrer(request):
    referrer = request.session.get('referrer', '')
    try:
        del request.session['referrer']
    except KeyError:
        pass
    return referrer
