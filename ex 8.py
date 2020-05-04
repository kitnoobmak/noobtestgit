
username = input("username")
password = input("password")
if username == "customer" and password == "1234":
    print("welcome to voicemail system")
    print("what do you want(type number)")
    print("1.mango  50 THB")
    print("2.cherry 100 THB")
else:
    print("username or password wrong!!!")
x = int(input())
if x == 1 :
    print("how many fruit do you want")
elif x == 2:
    print("how many cherry do you want")
y = int(input())
if x == 1 :
    print("total price of mango is", 50*y, "THB")
elif x == 2:
    print("total price of cherry is", 50*y, "THB")