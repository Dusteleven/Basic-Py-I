# WRITE YOUR SOLUTION HERE:

def begin_with_vowel(words: list):
    return [n for n in words if n[0].lower() in ["a","e","i","o","u"]]