import re
password = input("Python@123:")
if re.match(r'^(?=.*[a-z])(?=.*\d)(?=.*[@#$^%+=!&]).{8,}$'
    print("Password is valid.")
else:
    print("Password is invalid.")
