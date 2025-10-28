secret = "python123"

def check_password(password):
    if password == secret:
        return True
    else:
        return False

for i in range (1, 6):
    password = input("please enter the password: ")
    result = check_password(password)
    if result == True:
        print("correct password")
        break
    else:
        print("incorrect password")