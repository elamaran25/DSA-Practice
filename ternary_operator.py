def ternary(a,b,c):
    return a if (a > b and a > c) else (b if b > c else c)

a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))
print(ternary(a,b,c))