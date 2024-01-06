def add1(*args):
    sum = 0
    for n in args:
         sum += n
    return sum

print(add1(2,3,4))