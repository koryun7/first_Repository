# Write a function that will get a function string and check if the password is strong or not.
# Strong password must contain | One uppercase letter | one special symbol | one number
# Length of the password should be 8 or more
# If your password is Strong you will return True. else return False

def password_checker(password):
    result = False
    number = 0
    uppercase = 0
    symbol = 0
    if len(password) >= 8:
        for i in password:
            if i.isdigit():
                number += 1
            if i.isupper():
                uppercase += 1
            if i in "!@#$%^&*()_+{}|:,./;'[]-=":
                symbol += 1
        if number >= 1 and uppercase >= 1 and symbol >= 1:
            result = True
    return result


print(password_checker(input("Enter your password! ")))

