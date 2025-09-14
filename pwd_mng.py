import os
import json
import random
import string
from cryptography.fernet import Fernet
from hashlib import sha256

def gen_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    return key

def load_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as f:
            return f.read()
    else:
        return gen_key()

def encrypt_data(data, cipher):
    return cipher.encrypt(data.encode())

def decrypt_data(data, cipher):
    return cipher.decrypt(data).decode()

def gen_pwd():
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))


key = load_key()
cipher = Fernet(key)

password_file = "passwords.enc"

#if it doesnt exist
if not os.path.exists(password_file):
    print("Password file doesnt exist. creating a new one")
    with open(password_file, "wb") as f:
        f.write(b"") #empty
    print("We created it :)")

passwords = []
if os.path.getsize(password_file) > 0:
    with open(password_file, "rb") as f:
        for line in f:
            decrypted = decrypt_data(line.strip(), cipher)
            passwords.append(json.loads(decrypted))
while True:
    print("Options :")
    print("Add new password(1)")
    print("Veiw Stored passwords(2)")
    print("Exit(3)")
    print("Help(4)")
    choice = input(">:")

    if choice == "1":
        website = input("Website/service >:")
        username = input("Username >:")
        pwd_choice = input("Generat random password? (y/n) >:").lower()
        if pwd_choice == "y":
            pwd = gen_pwd()
        else:
            pwd = input("enter pwd >:")

        entry = {"website": website, "username": username, "password": pwd}
        passwords.append(entry)
        
        with open(password_file, "ab") as f:
            f.write(encrypt_data(json.dumps(entry), cipher) + b"\n")
    
    elif choice == "2":
        print("Passwords secret vault:\n")
        for entry in passwords:
            print(f"Website: {entry['website']}, Username: {entry['username']}, Password: {entry['password']}")
    elif choice == "3":
        break
    elif choice == "4":
        print("input pwd or service, input username, then choose generate or manual enter pwd")
        
