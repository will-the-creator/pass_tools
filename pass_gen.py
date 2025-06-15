import random
import string 

def gen_pass(length=12):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    # You can specify the length of the password here
    password_length = 12  # Default length
    print(f"Generated password: {gen_pass(password_length)}")
