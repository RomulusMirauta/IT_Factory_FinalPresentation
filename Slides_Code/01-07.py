# VARIABLES
var1 = 'valoare1'
var2 = 'valoare2'



# DATA TYPES: int, float, bool, str
# instantierea unei variabile de tip integer
putere = 29

# instantierea unei variabile de tip float
pret = 29.99

# instantierea unor variabile de tip boolean
este_vechi = False
este_nou = True

# instantierea unei variabile de tip string
producator = 'Ford'



# BUILT-IN FUNCTIONS: print() and type()
# instantierea unei variabile de tip string
producator = 'Ford'

# afisarea in consola a valorii variabilei producator
print(producator) # output: Ford

# afisarea in consola a tipului de date al variabilei producator
print(type(producator)) # output: <class 'str'>



# DATA STRUCTURES: list, dictionary, set, tuple
# instantierea unei liste
list1 = [29, 29.99, True, 'Ford']

# instantierea unui dictionar
dict1 = {
    'putere': 29,
    'pret': 29.99,
    'este_nou': True,
    'producator': 'Ford'
}

# instantierea unui set
set1 = {'Ford', 'Mazda', 'Volvo', 'Dacia'}

# instantierea unui tuplu
tuple1 = ('apple', 'banana', 'cherry')



# IF-ELSE STATEMENT
numar = int(input("Alege un numar: "))

if numar > 5:
    print("Numarul ales este mai mare decât 5.")  # se executa dacă conditia este True
else:
    print("Numarul ales este mai mic sau egal cu 5.")  # se executa dacă conditia este False
