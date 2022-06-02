# a. Recomandat (usor)
# 1. Revizualizeaza intalnirea 6 si ia notite in caz ca ti-a scapat ceva
#
# b. Obligatorii (mediu)
# Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei


print('1. Clasa Cerc')
class Cerc():
# Atribute: raza, culoare
    raza=0
    culoare=None
    Pi=3.14
# Constructor pt ambele atribute
    def __init__(self , raza_cerc , culoare_cerc):
         self.raza = raza_cerc
         self.culoare = culoare_cerc
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
    def descrie_cerc(self):
        print(self.raza, self.culoare)
# aria() - va RETURNA aria
    def aria(self):
        aria=self.Pi*(self.raza**2)
        return aria
# diametru()
    def diametru(self):
        diametru=2*self.raza
        return diametru
# circumferinta()
    def circumferinta(self):
        circumferinta=2*self.Pi*self.raza
        return circumferinta
cerc=Cerc(10, 'galben') #"cerc" = obiect (o variabila care contine o clasa), instantiat intr-o clasa
#asa
aria=cerc.aria()
print(aria)
#sau
print(cerc.aria())

print(' ')
print('2.Clasa Dreptunghi')
class Dreprunghi():
# Atribute: lungime, latime, culoare
    lungime=0
    latime=0
    culoare=None
#Constructor pt toate atributele
    def __init__(self, lung, lat, shaddow):
        self.lungime=lung
        self.latime=lat
        self.culoare=shaddow
# Metode:
# descrie()
    def descrie(self):
        print(f'Dreptunghiul are lungimea de {self.lungime} cm, latimea de {self.latime} cm si culoarea {self.culoare}')
# aria()
    def aria(self):
        aria=self.lungime*self.latime
        return f'Aria dreptunghiului este de {aria} cm patrati'
# perimetrul()
    def perimetru(self):
        perimetru=2*(self.lungime+self.latime)
        return f'Perimetrul dreptunghiului este de {perimetru} cm patrati'
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().
    def schimba_culoarea(self, noua_culoare):
        self.culoare=noua_culoare

dreptunghi1=Dreprunghi(10,5, 'rosu')
dreptunghi1.descrie()
print(dreptunghi1.aria())
print(dreptunghi1.perimetru())
dreptunghi1.schimba_culoarea('albastru')
dreptunghi1.descrie()

print(' ')
print('3.Clasa Angajat')
class Angajat():
# Atribute: nume, prenume, salariu
    nume=None
    prenume=None
    salariu=0
# Constructor pt toate atributele
    def __init__(self, nume_angajat, prenume_angajat, salariu_angajat):
        self.nume=nume_angajat
        self.prenume=prenume_angajat
        self.salariu=salariu_angajat
# Metode:
# descrie()
    def descrie(self):
        print(f'Nume angajat: {self.nume}, Prenume angajat: {self.prenume}, salariu: {self.salariu}')
# nume_complet()
    def nume_complet(self):
        print(f'Numele complet al angajatului: {self.nume} {prenume}')
# salariu_lunar()
    def salariu_lunar(self):
        print(f'Salariul lunar al angajatiului {self.nume} {self.prenume} este {self.salariu} RON')
# salariu_anual()
    def salariu_anual(self):
        salariu_anual=self.salariu*12
        print(f'Salariul anual al salariatului {self.nume} {self.prenume} este {salariu_anual} RON')
# marire_salariu(procent)
    def marire_salariu(self):
        marire_salariu=self.salariu*0.10
        return marire_salariu

salariat1=Angajat('Mondoc', 'David', 1000)
salariat1.descrie()
salariat1.salariu_lunar()
salariat1.salariu_anual()
print(salariat1.marire_salariu())

from datetime import date
today=date.today()
from tabulate import tabulate

print(' ')
print('4.Clasa Factura')
class Factura():
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie),
# numar, nume_produs, cantitate, pret_buc
    seria='AB'
    numar=0
    nume_produs=None
    cantitate=0
    pret_bucata=0
# Constructor: toate atributele, fara serie
    def __init__(self, nr, prod, cant, pret_buc):
        self.numar=nr
        self.nume_produs=prod
        self.cantitate=cant
        self.pret_bucata=pret_buc
# Metode:
# schimba_cantitatea(cantitate)
    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate=cantitate_noua
# schimba_pretul(pret)
    def schimba_pretul(self, pret_nou):
        self.pret_bucata=pret_nou
# schimba_nume_produs(nume)
    def schimba_nume_produs(self, nume_nou):
        self.nume_produs=nume_nou
# genereaza_factura() - va printa tabelar daca reusiti
    def afiseaza_factura(self):
        total = self.pret_bucata * self.cantitate
        print (tabulate([[self.seria, self.numar, self.nume_produs, self.cantitate, self.pret_bucata, total, date.today()]],
                       headers=['Serie Fact', 'Numar Fact','Produs', 'Cantitate', 'Pret Buc', 'Total', 'Data'], tablefmt='pretty'))
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

factura1=Factura(1,'clatite',1,10)
factura2=Factura(2, 'gogosi',5,5)

factura1.afiseaza_factura()
factura1.schimba_pretul(15)
factura1.schimba_cantitatea(10)
factura1.schimba_nume_produs('crepes')
factura1.afiseaza_factura()

factura2.afiseaza_factura()

print(' ')
print('5.Clasa Cont')
class Cont():
# Atribute: iban, titular_cont, sold
    iban=0
    titular_cont=None
    sold=0
# Constructor pentru toate
    def __init__(self, iban, titular, sold):
        self.iban=iban
        self.titular_cont=titular
        self.sold=sold
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')
# debitare_cont(suma)
    def debitare_cont(self, debitare):
        self.sold=self.sold-debitare
        return f'Am scazut contul cu {debitare} lei'
# creditare_cont(suma)
    def creditare_cont(self, creditare):
        self.sold=self.sold+creditare
        return f'Am crescut contul cu {creditare} lei'


titular1=Cont(12345,'DM',1000)
titular1.afisare_sold()
print(titular1.debitare_cont(int(input('introduceti suma retrasa: '))))
titular1.afisare_sold()
print(titular1.creditare_cont(int(input('introduceti suma depusa: '))))
titular1.afisare_sold()

# BONUS: (daca aveti timp si doriti sa lucrati suplimentar)
print(' ')
print('6.Clasa Masina')
class Masina:
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
    marca=None
    modelul=None
    viteza_max=0
    culoare='Gri' # Culoare = gri - toate masinile cand ies din fabrica sunt gri
    viteza_actuala=0 # Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
    culori_disponibile=('rusu', 'galben', 'verde', 'fuchsia', 'magenta', 'ciclam') # Culori disponibile = alegeti voi 5-7 culori
    inmatriculata=False
# Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
    def __init__(self, marca, model, viteza_maxima):
        self.marca=marca
        self.modelul=model
        self.viteza_max=viteza_maxima
# Metode:
# descrie() (se vor printa toate atributele, inafara de culori_disponibile)
    def descriere(self):
        print(self.marca, self.modelul, self.viteza_max, self.culoare, self.viteza_actuala, self.inmatriculata)
# inmatriculare() - va schimba atributul inmatriculata in True
    def inmatriculare(self):
        self.inmatriculata=True
        print(self.marca, self.modelul, self.viteza_max, self.culoare, self.viteza_actuala, self.inmatriculata)
        return self.inmatriculata
# vopseste(culoare) - se va vopsi masina in noua culoare
# DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
    def vopseste(self, noua_culoare):
        if noua_culoare in self.culori_disponibile:
            self.culoare=noua_culoare
            print ( self.marca , self.modelul , self.viteza_max , self.culoare , self.viteza_actuala ,
                    self.inmatriculata )
            return self.culoare
        else:
            print('Culoarea nu este disponibila pentru aceasca masina')
            return self.culoare
# accelereaza(viteza) - se va accelera la o anumita viteza, daca viteza e negativa-eroare,
# daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
    def accelereaza(self, noua_viteza):
        if noua_viteza<0:
            print('Atentie! Mergeti cu spatele!')
            print ( self.marca , self.modelul , self.viteza_max , self.culoare , self.viteza_actuala ,
                    self.inmatriculata )
        elif noua_viteza>self.viteza_max:
            self.viteza_actuala=self.viteza_max
            print ( self.marca , self.modelul , self.viteza_max , self.culoare , self.viteza_actuala ,
                    self.inmatriculata )
        else:
            self.viteza_actuala=noua_viteza
        print(self.marca, self.modelul, self.viteza_max, self.culoare, self.viteza_actuala, self.inmatriculata)
        return self.viteza_actuala
# franeaza() - masina se va opri si va avea viteza 0
    def franeaza(self, incetinire):
        while self.viteza_actuala>0:
            self.viteza_actuala=self.viteza_actuala-incetinire
            print ( self.marca , self.modelul , self.viteza_max , self.culoare , self.viteza_actuala ,
                    self.inmatriculata )
        if self.viteza_actuala<=0:
            print('am oprit masina')
        return self.viteza_actuala

masina1=Masina('BMW','740Li', 240)
masina1.descriere()
print(masina1.inmatriculare())
print(masina1.vopseste('magenta'))
print(masina1.accelereaza(160))
print(masina1.franeaza(40))
'''
print(' ')
print('7.Clasa TodoList')
class TodoList():
# Atribute: todo ( dict , cheia e numele taskului , valoarea e descrierea)
    todo={None, None} # La inceput nu avem taskuri , dict e gol si nu avem nevoie de constructor
# Metode:
# adauga_task ( nume , descriere )
    def adauga_task(self, nume, descriere):
        self.todo={nume, descriere}
# - se va adauga in dict finalizeaza_task ( nume )
# - se va sterge din dict afiseaza_todo_list ( )
# - doar cheile afiseaza_detalii_suplimentare ( nume_task )
# - in f de numele taskului , printam detalii suplimentare daca taskul nu e in todo list , intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere daca raspunde da - il cerem detalii task si salvam nume + detalii in dict
'''
