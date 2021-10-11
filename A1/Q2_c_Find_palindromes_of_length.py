from Q1_b_Test_whether_a_string_is_a_palindrome import * 
from Q2_a_Check_whether_a_string_is_an_English_word import *

def find_palindromes_of_length(n):
    palindrome_list = []
    for word in ENGLISH_WORDS:
        if len(word) == n and is_palindrome(word):
            palindrome_list.append(word)
    return sorted(palindrome_list)

print(find_palindromes_of_length(3))

