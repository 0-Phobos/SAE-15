L=[1, 2 ,4, 5, 5, 5,]
Li_nb=[]
n = int(input("Entrer le nombre à chercher"))
for i in range(len(L)) :
    if not L[i] in Li_nb:
        Li_nb.append(L[i])
    print(Li_nb)

for i in range(len(Li_nb)) :
    print(L[i],"apparaît",L.count(Li_nb[i]),"fois")
print("fin")

