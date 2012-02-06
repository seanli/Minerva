from django.contrib.auth.models import User

def titlecase(text):
    words = text.split(' ')
    capitalized_words = []
    for word in words:
        title_case_word = word[0].upper() + word[1:].lower()
        capitalized_words.append(title_case_word)
    merged = ' '.join(capitalized_words)
    return merged

def unique_username(first_name, last_name):
    counter = 1
    combined = (first_name.lower()[:1] + last_name.lower())[:30]
    user = User.objects.filter(username=combined)
    while user:
        combined = (first_name.lower()[:1] + unicode(counter) + last_name.lower())[:30]
        user = User.objects.filter(username=combined)
        counter += 1
    return combined

def set_referrer(request, referrer):
    request.session['referrer'] = referrer

def get_referrer(request):
    referrer = request.session.get('referrer', '')
    try:
        del request.session['referrer']
    except KeyError:
        pass
    return referrer