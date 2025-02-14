#Calculator using arithmetic operation
class Arithmetic:
    def __init__(self,num1,num2):
        sum = num1+ num2
        print("Addition of two numbers is",sum)
    def subtract(num1,num2):
        sub = num1 - num2
        print("Difference of two numbers is",sub)
    def multiply(num1,num2):
        mul = num1 * num2
        print("Multiply of two numbers is",mul)
    def divide(num1,num2):
        divide = num1 / num2
        print("Division of two numbers is",divide)
    def power_fun(self,num1,num2):
        power = num1 ** num2
        print("Power of two numbers is",power)
c1 = Arithmetic.subtract(23,34)
c2 = Arithmetic(23,34)
c3= Arithmetic.multiply(12,2)
c4 = Arithmetic.divide(12,3)
