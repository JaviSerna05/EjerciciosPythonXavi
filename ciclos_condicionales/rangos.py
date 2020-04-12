#range(1,10)---> Se usa cuando quiero darle un orden cronologico


#for indice, valor in enumerate(lista, 10):
    #print("indice:", indice, "valor:", valor)
lista = [1,2,3,4,5,6]
for indice in range( len(lista) ):
    print("indice:", indice, "valor:", lista[indice])