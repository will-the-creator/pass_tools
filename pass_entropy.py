import math

def calc_ent(password):

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "1234567890"
    special = "!@#$%^&*()_-+=[]{}\;:,.<>?/~`"

    # determine char_set
    char_size = 0
    if any(c in lower for c in password):
        char_size += len(lower)
    if any(c in upper for c in password):
        char_size += len(upper)
    if any(c in nums for c in password):
        char_size += len(nums)
    if any(c in special for c in password):
        char_size += len(special)

    if char_size == 0:
        return 0
    entropy = len(password) * math.log2(char_size)
    return entropy

def main():
    password = input("Never share your password with anyone\n\n enter test password: ")
    entropy = calc_ent(password)
    print(f"\nEntropy: {entropy:.2f} bits")

    if entropy < 40:
        print("\nWeak Password.")
    elif entropy < 60:
        print("\ncould be better, mid ahh password")
    else:
        print("\nStrong password")
if __name__ == "__main__":
    main()
