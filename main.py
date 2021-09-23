user_inp = int(input("Enter Value: "))

def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

print(convert(user_inp))