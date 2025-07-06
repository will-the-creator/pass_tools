import os, json, base64, getpass, hashlib
from cryptography.fernet import Fernet, InvalidToken

FILE = "user.enc"

def key(p): return base64.urlsafe_b64encode(hashlib.sha256(p.encode()).digest())
def h(p): return hashlib.sha256(p.encode()).hexdigest()
def encrypt(data, pw): return Fernet(key(pw)).encrypt(json.dumps(data).encode())
def decrypt(blob, pw): return json.loads(Fernet(key(pw)).decrypt(blob).decode())

if os.path.exists(FILE):
    u = input("username >: ")
    p = getpass.getpass("password >: ")
    try:
        data = decrypt(open(FILE, "rb").read(),p)
        if data["user"] == u and data["pass"] == h(p):
            print("logged in")
        while True:
            c = input("[v]eiw [w]rite [q]uit >:").lower()
            if c == "v":
                print(data.get("notes", "[empty]"))
            elif c == "w":
                note = input("Note >:")
                data["notes"] = data.get("notes", "") + "\n" + note
                open(FILE, "wb").write(encrypt(data, p))
            elif c == "q":
                print("\nsic semper tyrannis")
                break
            else: print("pick one of the three first letters")
        else: print("wrong credentials :(")
    except InvalidToken:
        print("decryption falied :( \n wrong password or corrupted file")
    except Exception as e:
        print(f"what the hell: {e}")
else:
    u = input("New Username >: ")
    p = getpass.getpass("new password >: ")
    p2 = getpass.getpass("reenter password >: ")
    if p == p2:
        data = {"user": u, "pass": h(p), "notes": ""}
        open(FILE, "wb").write(encrypt(data, p))
        print("created and encryped")
