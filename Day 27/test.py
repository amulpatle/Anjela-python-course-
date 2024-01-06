def add1(*args):
    sum = 0
    for n in args:
         sum += n
    return sum

print(add1(2,3,4))

# kwargs = key value pair 
# it convert argument into dictionary key value

def calculate(n,**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for (key, value) in kwargs.items():
        print(key,value)
    n += kwargs["add"]
    n *= kwargs["mult"]
    print(n)
    
    

calculate(2,add=3,mult = 5)#we can pass agrgument directly or by user defined name
