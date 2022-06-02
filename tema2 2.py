'''
a. Usor (recomandat)
1. Revizualizeaza intalnirea 2 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Operatori si Flow Control din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video 3 despre Structuri de date din 'Primii pasi in Programare'
Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
si sigur ti se vor intipari in minte mai bine.
https://www.itfactory.ro/8174437-intro-in-programare/

b. Usor spre Mediu (obligatoriu)
Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
X este un int
'''

#1.Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
    #if impune ce ar trebui sa se intample daca o anume conditie este adevarata
    #else impune ce se intampla daca aceeasi conditie nu este adevarata

#2. Verifica si afiseaza daca x este numar pozitiv sau nu

x=int(input('introdu un numar x: '))

if x>0:
    print(x, 'este numar pozitiv')
else:
    print(x, 'este numar negativ')

print("---------------------------------")

#3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

if x>0:
    print(x, 'este numar pozitiv')
elif x==0:
    print ( x , 'este neutru')
else :
    print(x, 'este numar negativ')

print ( "---------------------------------" )

#4. Verifica si afiseaza daca x este intre -2 si 13

if -2<x<13:
    print(x, 'se incadreaza in intervalul -2:13 ')
else:
    print(x, 'nu se incadreaza in intervalul -2:13')

print ( "---------------------------------" )

#5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

y=int(input('introdu un numar y: '))

if (x-y)<5:
    print(f'{x}-{y}={x-y} deci diferenta scaderii celor doua numere este mai mica decat 5')
else:
    print ( f'{x}-{y} = {x - y} deci diferenta scaderii celor doua numere NU este mai mica decat 5' )

print ( "---------------------------------" )

# #6. Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

if not(5<=x<=27):
     print(x, 'nu se incadreaza in intervalul 5:27')
else:
    print(f'CONDITION ERROR: {x} se incadreaza in intervalul 5:27 ')

print ( "---------------------------------" )

#7. x si y (int) Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare

if x==y:
    print('x si y sunt egale')
elif x>y:
    print('x este mai mare')
else:
    print('y este mai mare')

print ( "---------------------------------" )

#8. x, y, z - laturile unui triunghi. Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.

z=int(input('introdu un numar z: '))
if (x>0 and y>0 and z>0):
    if (x==y and x!=z and y!=z) or (x!=y and x==z and y!=z) or (x!=y and x!=z and y==z): #and (x,y,z>0)-asa nu merge
        print('triunghiul este isoscel')
    elif x==y==z:
        print ('triunghiul este echilateral')
    else :
        print('triunghiul este oarecare')
else:
    print("Latura triunghiului nu poate fi cu valoare negativa!")

#aici am o intrebare: avand in vedere ca folosesc aceleasi numere x,y,z peste tot, cum pot face ca daca unul dintre
#numere este negativ programul sa nu calculeze tipul de triunghi, deoarece nu poti avea triunghi cu latura negativa

print ( "---------------------------------" )

#9.Citeste o litera de la tastatura. Verifica si afiseaza daca este vocala sau nu

litere = input('introduceti o litera: ')

if (litere=='a' or litere=='A' or litere=='ă' or litere=='Ă' or litere=='â' or litere=='Â' or litere=='e'or litere=='E'
    or litere=='i' or litere=='I' or litere=='î' or litere=='Î' or litere=='o' or litere=='O' or litere=='u' or litere =='U'):

#if litere=='a' or 'A' or 'e' or 'E' or 'i' or 'I' or 'o' or 'O' or 'u' or 'U': = asta de ce nu merge? daca il folosesc
# asa spune ca toate literele sunt vocale si daca le pun intre paranteze zice ca toate sunt consoane ???

    print (f'litera introdusa "{litere}" este vocala')
else:
    print(f' litera introdusa "{litere}" nu este vocala: este consoana')

print ( "---------------------------------" )

# 10.Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota=int(input('introduceti nota in obtinuta in Romania pentru a o echivala cu sistemul american de notare: '))
if (nota>9):
    print('A')
elif nota>8:
    print('B')
elif nota>7:
    print('C')
elif nota>6:
    print('D')
elif nota>4:
    print('E')
else:
    print('F')

print ( "---------------------------------" )

#c. Optionale (may need google)
# 11.Verifica daca x are minim 4 cifre // (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

if len(str(x))>=4:
    print(True)
else:
    print(False)

print ( "---------------------------------" )

#12.Verifica daca x are exact 6 cifre

if len(str(x))==6:
    print(True)
else:
    print(False)

print ( "---------------------------------" )

# 13. Verifica daca x este numar par sau impar

assert x%2==0
print('x este numar par')

print ( "---------------------------------" )

# 14. x, y, z (int)
# Afiseaza care este cel mai mare dintre ele?
#
# 15. X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu
#
#
# 16. Pentru exercitiile cu biletele de avion incercati sa aplicati tehnicile de equivalence partitioning si boundary value analysis astfel incat sa eficientizati testarea.
#
# Sa tineti cont de urmatoarea chestie: tehnicile de testare vor fi aplicate nu pe faptul ca o persoana are pasaport sau nu ci pe varsta persoanei
#
# pasaport = input('Are pasaportul valid : DA/NU ')
# ambii_parinti = input('Are ambii parinti? DA/NU ')
# permisiune = input('Are permisiune? DA/NU/NA ' )
#
# if pasaport == 'DA' and (ambii_parinti == 'DA' or permisiune == 'DA') :
#     print('Permite calatoria')
# else :
#     print('Nu permite calatoria')
#
#
# Codul de mai sus va fi actualizat astfel incat sa țină cont și de varsta
#
#
# Age = input(introduceti varsta)
# pasaport = input('Are pasaportul valid : DA/NU ')
# ambii_parinti = input('Are ambii parinti? DA/NU ')
# permisiune = input('Are permisiune? DA/NU/NA ')
#
# If age >=18 and pasaport == “DA”:
# 	print(permite calatoria)
# elif pasaport == 'DA' and (ambii părinți == 'DA' or permisiune == 'DA') :
#     print('Permite calatoria')
# else :
#     print('Nu permite calatoria')
#
#
# Tehnicile de testare discutate vor fi aplicate pe condiția age>=18 și vor consta în crearea unor clase de echivalență din care vom alege cate o singura valoare și respectiv valorile de graniță pentru a le folosi în testare





