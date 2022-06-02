#functii simple
def say_hi():
    print('hi')

say_hi()
# #functii cu parametri
def say_hi_v1(user, varsta, ocupatie):
    print(f'buna {user}, ai {varsta} ani, si esti {ocupatie}')

nume=input('introdu userul: ')
ocupatie=input('introduceti functia: ')
ani=input('intorduceti anii: ')

say_hi_v1(nume, ani, ocupatie)
say_hi()

def say_hi_v2(user):
    print(f'hi {user}')

nume_input=['alex', 'roxy', 'norbi']
for nume in nume_input:
    say_hi_v2(nume)


def calculeaza_impozit(valoare_salariu):
    if valoare_salariu<4000:
        tax=0
    elif valoare_salariu>=4000 and valoare_salariu<5000:
        tax=0.10
    elif valoare_salariu>=5000 and valoare_salariu<33500:
        tax=0.22
    else:
        tax=0.4
    return tax

valoare_salariu=int(input('introduceti salariul: '))

taxa=calculeaza_impozit(valoare_salariu)
impozit=valoare_salariu*taxa
salariu_impozat=valoare_salariu-valoare_salariu*taxa
print(taxa)
print(calculeaza_impozit(valoare_salariu))

def calculeaza_impozit(valoare_salariu):
    if valoare_salariu<4000:
        tax=0
    elif valoare_salariu>=4000 and valoare_salariu<5000:
        tax=0.10
    elif valoare_salariu>=5000 and valoare_salariu<33500:
        tax=0.22
    else:
        tax=0.4
    return f'taxa aplicata a fost de {tax}, iar salariul dupa impozit este {salariu_impozat}. Impozitul este de {impozit}'

valoare_salariu=int(input('introduceti salariul: '))

print(taxa)
print(calculeaza_impozit(valoare_salariu))

#exercitiu: copiii bilet avion <10 ani=0, 10-18=-50%, 18-65 = 100%, >65=0,

def calcul_pret_bilet(varsta, pret_bilet):
    while varsta<0:
        varsta=int(input('Varsta incorecta. Va rugam incercati din nou'))
    if varsta<10 or varsta>65:
        pret_bilet=0
        print('pret 0')
    elif varsta>=10 and varsta<18:
        pret_bilet=pret_bilet-pret_bilet*0.5
        print ( 'pret 1' )
    elif varsta>=18 and varsta<=65:
        pret_bilet=pret_bilet
        print ( 'pret 2' )
    return f'aveti varsta de {varsta}. pretul biletului este de {pret_bilet} lei'
if __name__=='__main__':
    varsta=10
    pret_bilet=100

    pret_final=calcul_pret_bilet(varsta, pret_bilet)
    print(pret_final)


