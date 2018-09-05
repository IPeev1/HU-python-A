import re

def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6 and bool(re.search('\d', 'hello1')):
        return True
    return False

print(new_password('hello1', '1olleh'))
print(new_password('hello1', 'hello1'))
print(new_password('hello1', 'hello12'))
