lista=[1,2,3]
nowa_lista = lista # referencja
kopia_listy=lista.copy()
kopia_listy=lista[:]
lista[0] = 'X'
print (nowa_lista)
print (kopia_listy)


