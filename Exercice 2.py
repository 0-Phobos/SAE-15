print("Nombre jusqu'à 0:")

def Facto(x) :
    if x==1:
        return 1
    return x * Facto(x-1)

print(Facto(2))

print(Facto(3))