'''a. Usor (recomandat)
1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
si sigur ti se vor intipari in minte mai bine.
https://www.itfactory.ro/8174437-intro-in-programare/

Pentru toate exercitiile
Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
Daca functia are return, printati raspunsul'''

# b. Dificultate: usor spre mediu

print('1. Functie care sa calculeze si sa returneze suma a 2 numere')

def calcul_suma(a,b):
   print(a + b);
   return
# a=int(input('a= '))
# b=int(input(('b= ')))
calcul_suma(3,5)
calcul_suma(7,-1)
print('------------------------------')

print('2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar')
def par_impar(x):
   if x%2==0:
      print(True)
   else:
      print(False)
   return
# nr=int(input('introduceti numarul: '))
# par_impar(nr)
par_impar(2)
par_impar(1)

print('------------------------------')

print('3. Functie care returneaza numarul total de caractere din numele tau complet.')
# (nume, prenume, nume_mijlociu)
# def nr_caractere(nume, prenume, nume_mijlociu):
#    print(nume+prenume+nume_mijlociu)
#    total_caractere=0
#    for i in (nume, prenume, nume_mijlociu):
#       total_caractere+=1
#    return total_caractere
# nume=input('introducerti numele: ')
# prenume=input('introduceri prenumele: ')
# nume_mijlociu=input('introduceti numele mijlociu: ')
# nr_caractere(nume, prenume, nume_mijlociu)

def nr_caractere(nume):
   total_caractere=0
   for i in (nume):
      total_caractere+=1
   return total_caractere
nume=input('introducerti numele: ')
print(f'Numele dumneavoastra are {nr_caractere(nume)} caractere')

print('------------------------------')

print('4. Functie care returneaza aria dreptunghiului')

def ariadreptunghi():
   latimea=int(input('introduceti latimea: '))
   lungimea=int(input('introduceti lungimea: '))
   return f'Pentru un dreptunghi  cu latimea {latimea} si lungimea {lungimea}, aria este {latimea*lungimea})'

print(ariadreptunghi())

print('------------------------------')

print('5. Functie care returneaza aria cercului')

r=float(input("introduceti raza: "))
def ariacercului(r):
   PI = 3.142
   return f'Pentru un cerc cu raza {r}, aria cercului este {PI * (r * r)}'

print(ariacercului(r))

print('------------------------------')

print('6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu')

def checker(element):
   if element in text:
      print(True)
   else:
     print (False)
   return element
text=input('introduceti un text: ')
element=input('ce element doriti sa verificati?: ')

checker(element)

print('------------------------------')

print('7. Functie fara return, primeste un string si printeaza pe ecran: Nr de caractere lower case este x, Nr de caractere upper case este y')

str = ('Introduceti Un Text')

def up_low(str):
    upper = 0
    lower = 0
    for i in range(len(str)):
        if (str[i]>='a' and str[i]<='z'):
            lower+=1
        elif (str[i]>='A' and str[i]<='Z'):
            upper+=1
str=('Acesta Este Un Test')
print('lower case letters=', lower)
print('upper case letter=', upper)


print('------------------------------')

print('8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive')

def pozitive(numere):
   return [n for n in numere if n>0]

numere=([2, 6, -1, 10, -23, 8, -1, -2])

print(pozitive(numere))

print('------------------------------')

print('9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA')
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.

def comparator(x,y):
   if x>y:
      print(f'x={x} este mai mare decat y={y}')
   else:
      print(f'x={x} este mai mic decat y={y}')

x=int(input('introduceti x: '))
y=int(input('introduceri y: '))
print(comparator(x,y))


print('10. Functie care primeste un numar si un set de numere.')
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

def set(lista):
    if e!=() or e!= range(len(lista)):
        lista.append(e)
        print('adaugat noul numar in set', True)
    else:
        print('nu am adaugat numarul in set. Acesta exista deja', False)
    return lista

lista=[1,2,3,4]
e=int(input('introduceti un numar: '))
print(set(lista))

'''
c. Optionale (may need google)

11. Functie care primeste o luna din an si returneaza cate zile are acea luna

12. Functie calculator care sa returneze 4 valori
Suma, diferenta, inmultirea, impartirea a 2 numere

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

13. Functie care primeste o lista de cifre (adica doar 0-9)
Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}

14. Functie care primeste 3 numere
Returneaza valoarea maxima dintre ele

15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
Ex: daca dam nr 3
Suma va fi 6 (0+1+2+3)







BONUS:

16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
‘Numele este de baiat’ sau ‘Numele este de fata’


17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
Returnati numerele comune

Ex:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}

18. Functie care sa aplice o reducere de pret
Daca produsul costa 100 lei si aplicam reducere de 10%
Pretul va fi 90
Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
10% * 100 = 90

19. Functie care sa afiseze data si ora curenta din China

20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
'''

