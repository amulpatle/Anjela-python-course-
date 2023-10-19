from art import logo

print(logo)

while True:
    num1 = int(input("what is the first number"))
    print(""" 
            +
            -
            *
            /""")
    op = input("Pick an oprator")
    num2 = int(input("Enter second number"))
    if op == '+':
        print(num1 + num2)
    elif op =='-':
        print(num1-num2)
    elif op == '*':
        print(num1*num2)
    elif op == '/':
        print(num1/num2)
    else :
        print("invalid oprator")
    choice = input("type 'Y' if you want to start again else type 'N' ")
    if choice == 'N':
        break
