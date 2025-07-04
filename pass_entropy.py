import math
import string
def calc_ent(pw):
    sets = [
        string.ascii_letters,
        string.digits,
        string.punctuation
    ]
    chars = sum(len(s) for s in sets if any(c in s for c in pw))
    return 0 if chars == 0 else len(pw) * math.log2(chars)
pw = input("enter password: ")
e = calc_ent(pw)
print(f" {e:.2f} bits")
print("\nhell naw" if e < 40 else "\nmid ahh password" if e < 60 else "\nstrong")