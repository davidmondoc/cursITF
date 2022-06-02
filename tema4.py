# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 4 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Flow Control din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 5 despre Functii din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# Iteratiile sunt greute, deoarece necesita putina gandire algoritmica
# Va rog sa imi scrieti pe slack unde intampinati dificultati si va ajut
# Daca stati blocati > 30 min, cereti indiciu
#
# b. Dificultate medie (Faceti cat puteti din ele)


print('----------1----------')
# 1. Avand lista: Folositi un for ca sa iterati prin toata lista si sa afisati ‘Masina mea preferata este x’ /
# Faceti acelasi lucru cu un for each /
# Faceti acelasi lucru cu un while
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

print('-------FOR EACH-------')

for masina_mea in masini:
    print(f'masina mea preferata este {masina_mea}')
print('-------FOR-------')

for masinuta_mea in range(len(masini)):
    print(masinuta_mea)
    print('masina mea preferata este', (masini[masinuta_mea]))

print('------cu WHILE--------')
index_masina=0
while (index_masina<len(masini)):
    print ( f'masina mea preferata este {masini[index_masina]}' )
    index_masina=index_masina+1

print('----------2----------')
#2. Aceeasi lista: Folositi un for else,
# In for Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul,
# In else Printati lista

for i in range(len(masini)):
    if not(i==0 or i==len(masini)-1):
        masini[i] = masini[i].upper()
else:
    print(masini)
# #sau asa:
# index_masina=0
# while (index_masina<len(masini)):
#     print ( f'masina mea preferata este {masini[index_masina]}' )
#     index_masina=index_masina+1

print('----------3----------')
# 3.Aceeasi lista: Vine un cumparator care doreste sa cumpere un Mercedes. Iterati prin ea prin modalitatea aleasa de voi
# Daca masina e mercedes
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
   if masini[x]=='Mercedes':
       print(f'am gasit masina dorita de dvs {masini[x]}')
       break
   else:
        print(f'Am gasit masina {masini[x]}. Mai cautam')

print('----------4----------')
# 4.Aceasi lista: Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun
print(masini)
for cars in masini:
    if cars =='Lastun' or cars=='Trabant':
        continue
    print(f'urmatoarea sugestie este {cars}')

print('----------5----------')
# 5.
# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x
masini_vechi=[]
for cars in range(len(masini)):
    if masini[cars]=='Lastun' or masini[cars]=='Trabant':
        masini_vechi.append(masini[cars])
        masini[cars]='Tesla'
print(f'Modele noi: {masini}')
print(f'Modele vechi: {masini_vechi}')

print('----------6----------')
# 6.
# Avand dict
pret_masini = {'Dacia': 6800, 'Lastun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000 }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
# Iterati prin lista
#
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# (nu trebuie else)
# Printati S-ar putea sa va placa masina x
#
for cars, value in pret_masini.items():
    if cars=='Traband' or cars=='Lastun' or value>15000: #de ce trebuie value>15000? - cred ca stiu...
        continue
    print(f'S-ar putea sa va placa masina {cars},{value}')

print('----------7----------')
# # 7. Avand lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3] # Iterati prin ea: Afisati de cate ori apare 3 (nu aveti voie sa folositi count)

n=0
for i in numere:
    if i==3:
        n+=1
print(f' numarul 3 apare de {n} ori')

print('----------8----------')
# 8. Aceeasi lista: Iterati prin ea, Calculati si afisati suma numerelor (nu aveti voie sa folositi sum)
print(f'numere = {numere}')
total=0
for n in numere:
    total+=n
print(total)

print('----------9----------')
# 9. Aceeasi lista: Iterati prin ea, Afisati cel mai mare numar (nu aveti voie sa folositi max)
print(f'numere = {numere}')
numar_mare=0
for numar in numere:
    if numar>numar_mare:
        numar_mare=numar
print(f'cel mai mare numar este {numar_mare}')

print('----------10----------')
# # 10. Aceeasi lista: Iterati prin ea, Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa(# Ex: daca e 3, sa devina -3). Afisati noua lista
print(f'numere = {numere}')
for nr in range(len(numere)):
    if numere[nr]>0:
        numere[nr]=-numere[nr]
print(f'lista numere finala = {numere}')

# c. Optionale (may need google)

print('----------11----------')
# 11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final

for i in range(len(alte_numere)):
    if alte_numere[i]%2==0:
        numere_pare.append(alte_numere[i])
    else:
        numere_impare.append(alte_numere[i])
    if alte_numere[i]>0:
            numere_pozitive.append(alte_numere[i])
    else:
        numere_negative.append ( (alte_numere[i]) )
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

# print('----------12----------')
# 12.Aceeasi lista: Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici https://www.youtube.com/watch?v=lyZQPjUT5B4

# print('----------13----------')
# 13.
# Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!

# print('----------14----------')
# 14.
# Alegeti un numar de la tastatura
# Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333

# print('----------15----------')
# 15.
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)
