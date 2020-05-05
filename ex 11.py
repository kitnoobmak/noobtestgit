space = " "
number = int(input())
for x in range(number):
    print(space*(number-x),("*"*(x+1)+("*"*x)))
