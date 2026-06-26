num1=int(input("enter a number:"))
num2=int(input("enter a number: "))
num3=int(input("enter a number: "))
if(num1>num2 and num1>num3):
    print("First number is greater")
elif(num2>num1 and num2>num3):
    print("second number is largest")
else:
    print("third number is greater")