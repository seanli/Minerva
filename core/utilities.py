def capitalize(text):
    words = text.split(' ')
    capitalized_words = []
    for word in words:
        title_case_word = word[0].upper() + word[1:].lower()
        capitalized_words.append(title_case_word)
    merged = ' '.join(capitalized_words)
    return merged
