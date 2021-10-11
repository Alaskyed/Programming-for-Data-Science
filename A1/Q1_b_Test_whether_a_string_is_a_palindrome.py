def is_palindrome(s):
    for l in s:
        if not l.isalnum():
            s = s.replace(l,"")
    length = int(len(s)/2)
    s = s.replace(" ","")
    return s[:length].lower() == s[::-1][:length].lower()

print(is_palindrome("Ab cba!"))