def login(user, pwd):
    if user.strip() == "" or pwd.strip() == "":
        print("Blank input")
        return

    if user == "admin":
        if pwd == "pass123":
            print("Login Successful")
        else:
            print("Wrong Password")
    else:
        print("Invalid User")

user = "admin"
pwd = "pass123"

login(user, pwd)
