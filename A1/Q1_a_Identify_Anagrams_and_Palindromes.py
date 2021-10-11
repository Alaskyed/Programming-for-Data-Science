def anagrams( s1, s2 ):
    if sorted(s1.lower()) == sorted(s2.lower()) and s1.lower() != s2.lower():
        return True
    else:
        return False  


print(anagrams("this","This"))