x = int(input("ingrese X: "))
y = int(input("ingrese Y: "))


def A(x, y):
    y = y + 5
    if(y<20):
        x = x + 10
        if(x < 20):
            B(x, y)
        else:
            C(x, y)
    else:
        C(x, y)

def B(x, y):
    x = x + y
    if(y<10):
        C(x, y)
    else:
        A(x, y)

def C(x, y):
    y = y + x
    z = x + y
    print(z)
    
if(x < 10):
    B(x, y)
else:
    A(x, y)
