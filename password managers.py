from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key


def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            if "|" not in line:  # Check if the delimiter is present
                print("Invalid data format in 'password.txt'")
                continue
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "Password:", passw)


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    key = load_key()
    fernet = Fernet(key)  # Renamed variable to avoid confusion

    with open("password.txt", 'a') as f:
        encrypted_pwd = fernet.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_pwd + "\n")


# Main program
master_pwd = input("What is the master password? ")
key = generate_key()
fernet = Fernet(key)

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")