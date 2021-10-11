def get_english_words():
    with open( "english_words.txt" ) as f:
         words = f.readlines()
    words = { word.strip() for
             word in words }
    return words

ENGLISH_WORDS = get_english_words()

# func body
def is_english_word(s):
    if s.istitle() or s.islower():
        if s.lower() in ENGLISH_WORDS:
            return True
        else:
            return False
    else:
        return False

# print(is_english_word("suicid"))
