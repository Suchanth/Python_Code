#Sum of squares in first n natural numbers
def SumofSquares(n):
    s=0
    for i in range(n+1):
        s = s+i**2
    return s
n=int(input("Enter the Number "))
print("Sum of squares of first {} natural numbers: ".format(n),SumofSquares(n))
