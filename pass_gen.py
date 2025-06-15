import random
import string 

def gen_pass(length=16):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    
    password_length = 16
    print(f"Generated password: {gen_pass(password_length)}")
