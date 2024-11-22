# OOP (OBJECT-ORIENTED PROGRAMMING) PRINCIPLES

# INHERITANCE
class Vehicul: # definirea clasei parinte
    def __init__(self, producator):
        self.producator = producator

# definirea clasei copil Masina, care mosteneste clasa Vehicul
# clasa Masina va avea toate atributele si metodele definite in clasa Vehicul
class Masina(Vehicul):
    def descriere(self):
        return f"Acesta este un vehicul produs de {self.producator}."



# POLYMORPHISM
class MasinaElectrica:
    def tip_motor(self):
        return "electric"

class MasinaCombustie:
    def tip_motor(self):
        return "pe benzina"

def afiseaza_tip_motor(masina):
    print(f"Acest vehicul este: {masina.tip_motor()}.")

# crearea obiectelor de tip MasinaElectrica si MasinaCombustie
tesla = MasinaElectrica()
ford = MasinaCombustie()

# apelarea functiei afiseaza_tip_motor cu ambele tipuri de obiecte
afiseaza_tip_motor(tesla)  # output: Acest vehicul este: electric.
afiseaza_tip_motor(ford)   # output: Acest vehicul este: pe benzina.



# ABSTRACTION
# importarea clasei ABC și a abstractmethod din modulul abc (Abstract Base Classes)
from abc import ABC, abstractmethod

# definirea clasei Vehicul care mosteneste de la clasa ABC
# clasa Vehicul este o clasa abstracta
class Vehicul(ABC):
    # decoratorul @abstractmethod marcheaza metoda descriere ca fiind abstracta
    # orice clasa care mosteneste clasa Vehicul trebuie sa implementeze aceasta metoda
    @abstractmethod
    def descriere(self): # metoda abstracta descriere nu are implementare in clasa Vehicul
        pass # instructiune care indica faptul ca blocul de cod este intentionat lasat gol

class Masina(Vehicul): # definirea clasei Masina care mosteneste clasa abstracta Vehicul
    def descriere(self): # implementarea metodei abstracte descriere din clasa parinte Vehicul
        return "Aceasta este o masina."



# ENCAPSULATION
class ContBancar:
    def __init__(self, sold):
        # atribuirea valorii parametrului sold atributului privat __sold al obiectului
        # atributul este privat => este inaccesibil direct din afara clasei
        self.__sold = sold

    # metoda depune primeste un parametru suma si adauga aceasta suma la atributul privat __sold
    def depune(self, suma):
        self.__sold += suma

    # metoda afiseaza_sold returneaza valoarea atributului privat __sold
    def afiseaza_sold(self):
        return self.__sold
