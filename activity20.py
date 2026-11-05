from getpass import getpass

u = "tinlemer"
p = "meow1234"

isLoggedIn = False #trigger

while isLoggedIn == False:
    username = input("Username: ")
    password = getpass("Password: ")

    if username == u and password == p:
        print("Login Successful")
        isLoggedIn = True
    else:
        print("Login Failed")