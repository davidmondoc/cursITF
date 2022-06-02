#LIST:
print('---------------------LIST---------------------------')

nume = 'Mihai'
len(nume)
nume_list=['M', 'i', 'h', 'a', 'i'] #aici am definit o lista cu 5 elemente
print(nume_list[0]) #am accesat primul element din lista
print(len(nume_list)) #printeaza nr total de elemente din lista

#cum se poate aplica slicing pe liste
print(nume_list[0:2]) #returneaza de la primul element pana la penutlimul element definit

print(nume_list) #printeaza toata lista

nume_list.remove('a') # scoatem litera 'a' din lista in funtie de caracter
print(nume_list)

nume_list.pop() # scoatem un caracter in functie de index
print(nume_list)

# elimina_remove=nume_list.remove('a')
# print(elimina_remove)
# elimina_pop=nume_list.pop()
# print(elimina_pop)

'''
diferente intre .pop si .remove:

.remove                                                 .pop
    nu returneaza nimic                                 returneaza o valoare
'''

#suprascriere unei pozitie din lista
nume_list[0]='m'
print(nume_list)

#cum adaugam un element intr-o anumita pozitie
nume_list.insert(0, 'R')
print(nume_list)

#cume se adauga la finalul unei liste
nume_list.append('T')
print(nume_list)

#cum se adauga o lista intr-o alta lista;
lista_in_lista =[
    [1,2,3], [4,5,6],
    ['a','b','c'], ['A','B','C']
]

print(lista_in_lista[2][2], lista_in_lista[0][0])

#SET:
print('---------------------SET---------------------------')

vocale={'A', 'E', 'I', 'O', 'U'}
print(type(nume_list))
print(type(vocale))
#print(vocale[0]) #printam un element in functie de index -
                  #!!! nu se poate printa pozitia 0 pentru ca SET-urile sunt o colectie de date neordonate
print(vocale)
vocale.add('s')
print(vocale)
print(vocale.remove('s'))
print(vocale)

litera=input('va rog introduceti o litera: ').upper()
if litera in vocale:
    print('litera este o vocala')

# TUPLU: = este imputabil, adica ce este definit nu se mai poate schimba
#        = permite valori si este ordonata
print ( '---------------------TUPLU---------------------------' )

camere_hotel=(1, 2, 3, 4, 5, 5, 6, 7)
print(camere_hotel[0])
print(camere_hotel.count(5)) #returneaza de cate ori apare un element din tuplu
print(camere_hotel.index(3)) #returneaza pozitia unui element din tuplu
print(len(camere_hotel)) #afiseaza numarul de elemente din tuplu

#dictionar=structura care stocheaza informatii in formatul cheie:valoare
print ( '---------------------DICTIONARE---------------------------' )
capitale= {
    'Romania': 'Bucuresti',
    'Italia':'Roma',
    'Ukraina':'Kiev'
}

print(capitale['Romania']) #printeaza valoarea in functie de cheie
print(capitale.get('Romania')) #printeaza valoarea in functie de cheie  - alta metoda

#actiualizarea unei informatii
capitale['Romania']='Cluj'
print(capitale['Romania'])

#adaugarea unei noi informatii:
capitale['Rusia']='Moscova'
print(capitale)
print(len(capitale))

#stergerea unei informatii:
capitale.pop('Rusia')
print(capitale)


#extra :D 
def calculeazasuma(a, b):
    return a+b

print(calculeazasuma(5,6))