print("sveiks/a!")
print("Si programma izdrukas rekinu koka laditei.\n\n\n")

klients = input("pasutitaja vards, uzvards: ")
print("-"*50)
veltijums = input("vajadzigais veltijums: ")
print("-"*50)
izmers = input("ladites izmers - platums, garums, augstums - milimetros (raksti veselus skait'lus):")
print("-"*50)
materials = input("kokmateriala cena EUR/m2: ")




class Rekins():
 def __init__(self, klients, veltijums, izmers, materials):
   self.klients = klients
   self.veltijums = veltijums
   self.izmers = izmers
   self.materials = int(materials)

   self.teksta_gar = len(self.veltijums)
   self.ladites_izm = self.izmers.split(",")
   #print(self.ladites_izm)

   self.augstums = int(self.ladites_izm[0])
   self.garums = int(self.ladites_izm[1])
   self.platums = int(self.ladites_izm[2])

 def izdruka (self):
   
   print("\n\n")
   print('\033[1m'+"pasutitaja dati:"+'\033[0m')
   print("-"*50)
   print(f"\x1B[3mpasutitaja vards un uzvards:\x1B[0m \033[1;32m{self.klients}\033[1;0m")  
   print(f"\x1B[3mladites izmeri:\x1B[0m \n\x1B[3mplatums:\x1B[0m \033[1;32m{self.platums}\033[1;0m \n\x1B[3mgarums:\x1B[0m \033[1;32m{self.augstums}\033[1;0m")
   print(f"\x1B[3mmateriala cena EUR/m2:\x1B[0m \033[1,32m{self.materials}\033[1;0m")
   print(f"\x1B[3mizmaksas:\x1B[0M \033[1;32M{self.aprekins()}\033[1;0m")

   self.saglabat()
   print(f"klienta dati saglabati faila {self.klients}.csv")

 def aprekins (self):
   darba_samaksa = 15
   PVN = 21
   produkta_cena = (self.teksta_gar) * 1.2 + (self.platums/100 *self.garums/100 * self.augstums/100)/ 3 * self.materials 
   PVN_summa = (produkta_cena + darba_samaksa) *PVN/100
   rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
   return rekina_summa
  
 def saglabat (self):

   import csv

   with open(f"{self.klients}.csv", "w", newline ="") as file:
     writer = csv.writer(file)
     writer.writerow = (["klienta vards","veltijums","izmers","materiala cena"])



Rekins = Rekins(klients,veltijums,izmers,materials)
print(Rekins.izdruka())



# print(izmeri)
# print(type(izmeri))
# print(izmeri.split(","))
# sadal = izmeri.split(",")
# print(sadal[0])
# print(sadal[1])
# print(sadal[2])


#print(veltijums)
#print(type(veltijums))
#print(len(veltijums))
   