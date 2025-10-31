x = 0
if x > 0:
    print(x, "Positive")
else:
    print(x, "Negative")


def test():
    if x > 0:
        print(x, "Positive")
    elif x == 0:
        print(x, "Zero")
    else:
        print(x, "Negative")


test()
print(x == 0)


x=2
y=3
if (x>0) & (y>x):
    print("Both conditions are true")
elif x==0:
    print("x is zero")
else:
    print("At least one condition is false")


def signe(x):
    if x > 0:
        return "le nombre en parametre de signe est : Positive"
    elif x == 0:
        return "le nombre en parametre de signe est : Zero"
    else:
        return "le nombre en parametre de signe est : Negative"


print(signe(5))
print(signe(0))
print(signe(-3))
