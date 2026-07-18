a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
d = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", d)