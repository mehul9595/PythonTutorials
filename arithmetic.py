import math

def demo_arithmetic(a, b):
    print("\nDemo arithmetic\n")
    print("%s + %s = " % (a, b), a+b)
    print("%s - %s = " % (a, b), a-b)
    print("%s * %s = " % (a, b), a*b)
    print("%s / %s = " % (a, b), a/b)
    print("%s %% %s = " % (a, b), a%b)
    print("%s ** %s = " % (a, b), math.pow(a,b))
    print("%s // %s = " %  (a, b), a//b)
    print("factorial of %s is" % a, math.factorial(a))    


demo_arithmetic(7,2)