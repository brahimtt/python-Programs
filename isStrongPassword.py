import re
strongPswRegex=re.compile(r'''(
    ([a-zA-Z]{2,7})     #  uppercase and lowercase  
    (\d{1,6})             # at least one digit   
                         
    )''',re.VERBOSE)
def isStrongPassword(text):
    if len(text)!=8:
        return False
    elif strongPswRegex.search(text)==None:
        return False
    else:
        return True
print('enter your password:')
text=input()

if isStrongPassword(text):
    print('your password is strong ')
else:
    print('your password must contain uppercase and lower case and at least one digit')