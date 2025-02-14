#maximum of three numbers
n1 = int(input("Enter the number1: "))
n2 = int(input("Enter the number2: "))
n3 = int(input("Enter the number3: "))
if n1 > n2 and n1 > n3:
    print(n1,"is the maximum number1")
elif n2 > n1 and n2 > n3:
    print(n2,"is the biggest number2")
elif n3 > n1 and n3 > n2:
    print(n3,"is the biggest number3")
else:
    print(n1,n2,n3,"is the equal numbers")
