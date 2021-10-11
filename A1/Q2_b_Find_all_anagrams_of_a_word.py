from Q2_a_Check_whether_a_string_is_an_English_word import *
from Q1_a_Identify_Anagrams_and_Palindromes import *

def find_all_anagrams(s):
    anagrams_list=[]
    for word in ENGLISH_WORDS:
        if anagrams(s.lower(),word) and s.lower() != word:
            anagrams_list.append(word)
    return sorted(anagrams_list)

# print(is_english_word("suiciding"))
print(find_all_anagrams("Python"))