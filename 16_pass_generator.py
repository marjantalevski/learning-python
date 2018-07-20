import random

def strong_pass_generator(passlength):
    c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = "01234567890"
    s = "!@#$%^&*()?"
    clength = passlength - 4
    nlength = 2
    slength = 2
    char =  "".join(random.sample(c, clength))
    num =  "".join(random.sample(n, nlength))
    sym =  "".join(random.sample(s, slength))
    password = char + num + sym
    print(password)
strong_pass_generator(10)