name = input("What is your name? ")
num1 = int(input('Enter the fist number '))
num2 = int(input('Enter the second number '))
add = (num1 + num2)
subtract = float(num1)-float(num2)
multiplication = float(num1)*float(num2)
division =(num1/num2)

print("Hello",name,"Please find below your calculations")

print('Addition: ',add)
print('Subtraction: ',subtract)
print('Multiplication: ',multiplication)
print("Division ", division)
fact1 = 1
org1 = num1
while num1 > 0:
    fact1 = fact1 * num1
    num1 = num1 - 1
print ("The factorial of ", org1,"is ", fact1)

fact2 = 1
org2 = num2
while num2 > 0:
    fact2 = fact2 * num2
    num2 = num2 - 1
print ("The factorial of ", org2,"is ", fact2)

print("Bye, see you next time")


