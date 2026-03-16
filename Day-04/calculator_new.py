
def add(num1, num2, num3):
    add = float(num1 + num2 + num3)
    return add

def sub(num1, num2, num3):
    sub = float(num1 - num2 - num3)
    #print(f"Substraction of {num1},{num2},{num3} is:", sub)
    return sub

def mul(num1, num2, num3):
    mul = float(num1 * num2 * num3)
    #print(f"multiplication of {num1},{num2},{num3} is", mul)
    return mul


print(add(10,3,5))
print(sub(10,45,45))
print(mul(10,34,3))
