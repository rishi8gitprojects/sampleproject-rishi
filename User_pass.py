class User_pass():
    def __init__(self):
        self.passwords = {}
    
    def create_userid(self, user, passkey):
        self.passwords[user] = passkey
    
    def check_user(self, user):
        if user in self.passwords:
            return True
        else:
            return False
    def check_pass(self, user, passkey):
        if passkey == self.passwords[user]:
            return True
        else:
            return False

login = User_pass()
print("(1) Log-in \n(2) Sign-up")
cmd = input("> ")
try:

    if cmd == "2":
        user = input("Create a [username]: ")
        passkey = input("create a [password]: ")
        login.create_userid(user, passkey)
    elif cmd == "1":
        user = input("Create a [username]: ")
        if login.check_user(user):
            passkey = int(input("Enter you [Password]: "))
            if login.check_pass(user,passkey):
                print("You're logged in!")
            else:
                print("Log-in failed!!")
        else:
            print("User not found!!!")
    else:
        print("Enter valid input!!")
finally:
    print("Hope for the good!")
