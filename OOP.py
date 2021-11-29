

saraksts  = [1,2,3]

print(type(saraksts))

saraksts.append(20)

print(saraksts)


class Piem():
  pass

a = Piem()

print(type(a))

class Auto():
  def __init__(self, modelis, krasa):   #Inicializācija
    self.modelis = modelis              #Īpašības
    self.krasa = krasa

BMW = Auto(modelis = "X5", krasa = "sarkana")

Opel = Auto(modelis = "Astra", krasa = "melna")

Audi = Auto("A6", "zila")


print(BMW.modelis)

print(Opel.modelis)

print(Audi.modelis)

print(Audi.krasa)


class Auto():
  def __init__(self, modelis, krasa):
    self.modelis = modelis
    self.krasa = krasa

  def dati (self):                        #Metode, strādā ar iekavām()
    return self.modelis + self.krasa
  
  def krasas_maina(self, jauna_krasa):
    print()

BMW = Auto(modelis = "X5", krasa = "sarkana")

Opel = Auto(modelis = "Astra", krasa = "melna")

Audi = Auto("A6", "zila")


# print(BMW.modelis)

# print(Opel.modelis)

# print(Audi.modelis)

# print(Audi.krasa)

print(Audi.dati())
BMW.krasas_maina("sudraba")
Opel.krasas_maina("dzeltena")