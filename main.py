class user:
    login = ''
    pswd = 0

    def __init__(self, u, p):
        self.login = u
        self.pswd = p

accs = []

accs.append(user("tim",1212))

while True:
    command = input("Comand list:\n   (1)-Sign in\n   (2)-Log in\n   (3)-Break while\n")

    match command:
        case "1":
            login = input("Your login:\n")
            pswd = int(input("Your PIN:\n"))
            cfpswd = int(input("Confirm PIN:\n"))

            if pswd == cfpswd:
                accs.append(user(login, pswd))
                print("Your account is crreated!")

            else:
                print("PINs do not much")

        case "2":
            resp=input("user name\n")

            for i in range(len(accs)):
                if resp == accs[i].login:
                    password = int(input("Input PIN: \n"))
                    if password == accs[i].pswd:
                        print(f"Hello {accs[i].login}")

        case _:
            break