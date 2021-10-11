from Q2_a_Check_whether_a_string_is_an_English_word import *
def password_strength( password ):
    visible_characters = r"~`!@#$%^&*(){}[]|\/:;\";<>.?"

    #ILLEGAL
    if password.lower() in ENGLISH_WORDS:
        return "ILLEGAL"
    else:
        for l in password:
            if l in " \n\r\t":
                return "ILLEGAL"
    # WEAK
    if len(password) < 8:
        return "WEAK"
    else:
        for en_word in ENGLISH_WORDS:
            if password.startswith(en_word):
                last_letter = password.replace(en_word,"")
                if last_letter.isdigit():
                    return "WEAK"

    # STRONG
    if len(password) > 11 and not password.islower() and not password.isupper():
        flag = 0
        for l in password:
            if l.isdigit():
                flag = 1
        for l in password:
            if l in visible_characters and flag == 1:
                return "STRONG"
        
    #MEDIUM
    return "MEDIUM"
            


print(password_strength("brandon123"))
