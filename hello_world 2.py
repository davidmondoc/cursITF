# command+/ selecteaza/deselecteaza linile selectate

# in cazul in care apare ' sau " in string, se pune \ pentru ca python sa le citeasca parte din cod
# sau se pun " " pentru ca sa interpreteze ' ca find parte din string
# sau ' ' pt ca Py sa citeasca " ca parte din string
print('Mc\' Donalds')
print("Mc' Donalds")

x, y, z = 1, 2, 3
print(z, y, z, x, x, z)

import math

a = 3.7
# sintaxa care limitaza nr de zecimale
print('{:.2f}'.format(a))
print(round(a))
print(math.floor(a)) # fortam rotunjire in jos
print(math.ceil(a)) # fortam rotunjire in sus

# cum aflam tipuri
a = 3
print(type(a))

#type casting=schimbam tipul de date
cifra='2'
cifra2= int(cifra)

print(type(cifra))
print(type(cifra2))

a=1
b=1.2

print(a+b)



# assert - se verifica daca ecuatia este True
# daca e True, mergem mai departe silently
# daca e Talse, cod rosu, eroare, nu mergem mai departe
a = 1
# il intreb pe python: hey, a este egal cu 1?
print(a == 1)
assert a == 1
print('trec pe aici')
print(a == 2)
assert a == 2
print('nu mai ajung aici')

user_pass = input('introdu parola')
parola = 'pass123'
assert parola == user_pass
print('autentificare reusita')