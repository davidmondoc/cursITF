'''
a. Usor (recomandat)
1. Revizualizeaza intalnirea 1 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video cu Variabile si Tipuri de date din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video cu Operatori si Flow Control din 'Primii pasi in Programare'
Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
si sigur ti se vor intipari in minte mai bine.
https://www.itfactory.ro/8174437-intro-in-programare/

# b. Usor spre Mediu (bligatoriu)

'''
# 1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila

        #o variabila este o parte de memorie care retine date


#2.Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool. Valorile le alegeti voi dupa preferinte

valoare1='tema 1'
valoare2=5
valoare3=7.23
valoare4=True


#3.Utilizat functia type pentru a verifica ca ele au tipul de date asteptat

print('valoare1 este',type(valoare1))
print('valoare2 este',type(valoare2))
print('valoare3 este',type(valoare3))
print('valoare4 este',type(valoare4))


#4.Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere).Verificati tipul acesteia

print(round(valoare3))
valoare3=int(valoare3)
print('valoare3 este mai nou', type(valoare3))


#5.folositi print() si printati in consola 4 propozitii folosind cele 4 variabile. (rezolvati nepotrivirile de tip prin ce modalitate doriti)

print('Aceasta este', valoare1,'pe care ne-a dat-o Andy să o facem')
print(f'Am ajuns la exercitiul, {valoare2} si totul a mers destul de repede')
print(f'{valoare3},...cam atât luam eu la teorie muzicală')
print(f'when people say "word", it means that what they are sayin\' is {valoare4}')

# 6.citeste de la tastatura numele
# citeste de la tastatura prenumele
# afiseaza 'Numele complet are x caractere'

numele=input('Numele: ')
prenumele=input('Prenumele: ')
print(f'Numele complet are {len(numele+prenumele)} caracter')


# 7.citeste de la tastatura lungimea
# citeste de la tastatura latimea
# afiseaza 'Aria dreptunghiului este x'

lungimea=input('Lungimea= ') #sau int(input('Lungimea= '))
lungimea=int(lungimea)
latimea=input('Lățimea= ') #sau int(input('Lățimea= '))
latimea=int(latimea)
print(f'Aria dreptunghiului este {lungimea*latimea}')


# 8.# Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# cititi de la tastatura un int x
# afiseaza stringul fara ultimele x caractere
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

string='Coral is either the stupidest animal or the smartest rock'
x=int(input('introduceti un numar: '))
#x=int(x)
print(string[:-x])


#9.acelasi string: declara un string nou care sa fie format din primele 5 caractere + ultimele 5

string='Coral is either the stupidest animal or the smartest rock'
print(len(string)-5)
print(string[:5]+string[52:])


#10.acelasi string: afisati de cate ori apare cuvantul 'the'

print(string.count('the'))


#11.acelasi string. inlocuieste the cu THE peste tot. printeaza rezultatul

print(string.replace('the', 'THE'))


# 12.acelasi string. salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock (hint: este o functie care te ajuta sa faci asta)
# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '

rock_ind=print('rock_ind =', string.index('rock'))
print(string[:rock_ind])


# 13.
# citeste de la tastatura un string
# verifica daca primul si ultimul caracter sunt la fel
# se va folosi un assert
# atentie: se doreste ca programul sa fie case insensitive
# 'apA' e acceptat

un_string=input('scrie orice:')
assert un_string[0].lower()==un_string[len(un_string)-1].lower()
print('"un_string" are acelasi caracter si la inceput si la sfarsit')


# 14.avand stringul '0123456789': afisati doar numerele pare // acum afisati doar numerele impare (hint: folositi slicing, controlati din pas)

numeric='0123456789'
print('numerele pare din stringul "numeric" :', numeric[::2])
print('numerele impare din stringul "numeric" :',numeric[1::2])


# 15.acelasi string de la 14. folositi un assert ca sa verificati daca acest string contine doar numere
# indiciu: merge cu slicing? probabil ca nu... ce mai stim atunci legat de string?. poate gasim o functie ajutatoare
# Ex: ‘abc123’ => false; ‘abc’ => false, ‘123’ => true

print('contine stringul "numeric" doar cifre? -', numeric.isdigit())
assert numeric.isdigit() == True


# c. Optionale (may need google)
# 16.citeste de la tastatura un string de dimensiune impara
# afiseaza caracterul din mijloc

impar=input('introdu stringul: ')
print(impar[::])



#17. Folosind assert, verificati daca un string este palindrom

cuvant=input('introduceti cuvantul: ')

assert cuvant==cuvant[::-1]
print('Cuvantul este palindrom')

#18. folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
# si salveaza fiecare cuvant intr-o variabila
# acum printeaza ambele variabile pentru verificare

cuvant_1, cuvant_2=input('introduceti cuvantul_1: '), input('introduceti cuvantul_2: ')

print(cuvant_1, cuvant_2)


# 19. citeste un string de la tastatura (eg: alabala portocala)
# salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
# capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# => alAbAlA portocAla

string_mash=input('introdu textul: ')
print(string_mash)
primul_caracter=string_mash[0]
print(primul_caracter)
print(string_mash2=string_mash.replace(primul_caracter, primul_caracter.upper()))


# 20. citeste un user de la tastatura, citeste o parola
# afiseaza: 'Parola pt user x este ***** si are x caractere'
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# eg: parola abc => ***
# parola abcd => ****

import getpass

user=input('introduceri user: ')
parola=input('introduceti parola: ')

print ('Parola pentru userul', user.upper(), 'este:', parola, 'si are', len(parola), 'caractere')