import re
def passwordstrength(password):
    len_criteria = len(password) >= 8
    uppercase_criteria=bool(re.search(r'[A-Z]', password))
    lowercase_criteria=bool(re.search(r'[a-z]', password))
    number_criteria=bool(re.search(r'[0-9]', password))
    spechar_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    if len_criteria and uppercase_criteria and lowercase_criteria and number_criteria and spechar_criteria :
        return "Strong password"
    else :
        feedback = "Weak password. Please include: "
        if not len_criteria:
            feedback += "at least 8 characters, "
        if not uppercase_criteria:
            feedback += "at least one uppercase letter, "
        if not lowercase_criteria:
            feedback += "at least one lowercase letter, "
        if not number_criteria:
            feedback += "at least one number, "
        if not spechar_criteria:
            feedback += "at least one special character, "
        return feedback[:-2]
    
    
password = input("Enter your password: ")
strength = passwordstrength(password)
print(strength)