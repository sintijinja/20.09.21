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
   self.materials = materials

   self.teksta_gar = len(self.veltijums)
   self.ladites_izm = self.izmers.split(",")

   self.augstums = self.ladites_izm[0]
   self.garums = self.ladites_Izm[1]
   self.platums = self.ladites_izm[3]

 def izdruka (self):
   
   print("\n\n")
   print('\033[1m'+"pasutitaja dati:"+'\033[0m')
   print("-"*50)
   print(f"\x1B[3mpasutitaja vards un uzvards:\x1B[om \033[1;32m{self.klients}\033[1;0m")  
   print(f"\x1B[3mladites izmeri:\x1B[0m \n\x1B[3mplatums:\x1B[0m \033[1;32m{self.platums}\033[1;0m \n\x1B[3mgarums:\x1B[0m \033[1;32m{self.augstums}\033[1;0m")
   print(f"\x1B[3mmateriala cena EUR/m2:\x1B[0m \033[1,32m{self.materials}\033[1;0m")
   print(f"\x1B[3mizmaksas:\x1B[0M \033[1;32M{self.aprekins()}\033[1;0m")

 def aprekins (self):
   darba_samaksa = 15
   PVN = 21
   produkta_cena = (self.teksta_gar) * 1.2 + (self.platums)
    

veltijums = input('uzraksti veltijumu:')
izmeri = input("ievadi laadites izmerus\n garums,platums,augstums (raksti veselus skaitlus, atdalot tos ar komatiem\n")

print(izmeri)
print(type(izmeri))
print(izmeri.split(","))
sadal = izmeri.split(",")
print(sadal[0])
print(sadal[1])
print(sadal[2])


#print(veltijums)
#print(type(veltijums))
#print(len(veltijums))
   