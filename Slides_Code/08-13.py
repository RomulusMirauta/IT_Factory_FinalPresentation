# LOOPS: while, for, for each
j = 0

while j < 3:
    print(j)
    j += 1
else:
    print("Ciclul repetitiv s-a incheiat!")

# for
for i in range(3):
    print(i)
else:
    print("Ciclul repetitiv s-a incheiat!")

# for each
masini = ['Ford', 'Mazda', 'Volvo', 'Dacia']

for masina in masini:
    print(f"Masina mea preferata este {masina}.")



# CONTROL FLOWS: break, continue
# programul se va opri dupa 2 iteratii
for i in range(1, 50):
    if i == 3:
        break
    print(i)

# programul va sari peste iteratia 4
for i in range(5):
    if i == 3:
        continue
    print(i)



# FUNCTIONS AND PARAMETERS
# functie fara parametri
def hello1(): # definirea functiei
    print("Hello, user!")

hello1() # apelarea functiei


# functie cu 2 parametri
def hello2(username, tag): # definirea functiei
    print(f"Hello, {username}#{tag}!")

hello2("Andrei", "29") # apelarea functiei



# CLASSES AND OBJECTS
class Masina: # definirea clasei
    producator = 'Ford' # instantierea unui atribut
    pret = 5000

    def facut_plinul(self): # definirea unei metode
        return "Rezervor full!"

masina_mea = Masina() # crearea obiectului masina_mea de tip Masina
print(masina_mea.producator) # afisarea valorii atributului producator al obiectului masina_mea
print(masina_mea.facut_plinul()) # afisarea mesajului in urma apelarii metodei facut_plinul a obiectului masina_mea



# CONSTRUCTORS
class Masina:
    # definirea constructorului pentru clasa Masina
    # metoda __init__ primeste 3 parametri (producator, model, an)
    def __init__(self, producator, model, an):
        self.producator = producator # setarea atributului obiectului la valoarea parametrului
        self.model = model
        self.an = an

    def descriere(self): # definirea unei metode
        return f"{self.producator} {self.model}, fabricata in anul {self.an}."

# crearea obiectului masina_mea de tip Masina, folosind constructorul definit in clasa Masina
# atributelor producator, model si an le sunt atribuite valorile Ford, Focus, respectiv 2019
masina_mea = Masina("Ford", "Focus", 2019)
# afisarea mesajului in urma apelarii metodei descriere a obiectului masina_mea
print(masina_mea.descriere())
