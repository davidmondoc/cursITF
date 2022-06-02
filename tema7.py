from abc import ABC, abstractmethod
# 2. Faceti exercitiul dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna) - DONE
#
# ABSTRACTION
# Clasa abstracta FormaGeometrica
# Contine un field PI=3.14
# Contine o metoda abstracta aria
# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
#
class FormaGeometrica(ABC):
    PI=3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie_cu_colturi(self):
        return 'Cel mai probabil am colturi'

    def descriere_fara_colturi(self):
        return 'Eu  nu am colturi'

# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
# constructor pt latura
# ENCAPSULATION
# latura este proprietate privata
# Implementati getter, setter, deleter p t latura
# Implementati metoda ceruta de interfata
# POLYMORPHISM
# Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
# Creati un obiect de tip Patrat si jucati-va cu metodele lui
# Creati un obiect de tip Cerc si jucati-va cu metodele lui
class Patrat(FormaGeometrica):

    def __init__(self,latura):
        self.__latura=latura

    def aria(self):
        area = self.__latura** 2
        return area

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, latura):
        if latura>0:
            self.__latura=latura
        else:
            print('Valoarea laturii trebuie sa fie mai mare ca 0')

    @latura.deleter
    def latura(self):
        self.__latura=0

patrat1=Patrat(0)
patrat1.latura=7
print(patrat1.aria())
print(patrat1.descrie_cu_colturi())

# Clasa Cerc - mosteneste FormaGeometrica
# constructor pt raza
# raza este proprietate privata
# Implementati getter, setter, deleter pt raza
# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte
class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza=raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza):
        if raza>0:
            self.__raza=raza
        else:
            print('Valoarea razei trebuie sa fie mai mare ca 0')

    @raza.deleter
    def raza(self):
        self.__raza = 0

    def aria(self):
        area=self.PI*self.__raza**2
        return area

cerc1=Cerc(1)
cerc1.raza=2
print(cerc1.aria())
print(cerc1.descriere_fara_colturi())

# 3. Actualizati proiectul pe github facand un push la noul cod
# In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public
