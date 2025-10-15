#Criar um set a vazio
meu_set_vazio = set()
#criar um set com valores
meu_set_com_elementos = {1,2,3,4}

#criar um set atraves da lista
lista = [3,4,5,6,7]
#print(lista)
meu_set_lista = set ( lista )
#print(meu_set_lista)
tupla = (45, 45, 645, 6567, 56, 8, 678)
meu_set_tupla=set (tupla)

set_frases = set ("Hello World !")
set_frases.add('A')
set_frases.discard("3")

#print(type(meu_set_vazio))




#metodo de copia
meu_set = {21,32,13,124,23,4,2343,4,2423,4,2,9}
novo_set = meu_set.copy()
novo_set.add(3)
#print(novo_set)
novissimo_set = meu_set
novissimo_set.add(3)
#print(meu_set)
#print(novissimo_set)
#uniao
a={1,2,3}
b={4,5,6}
union = a.union(b)#{1,2,3,4,5,6}
print(union)