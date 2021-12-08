
class transportlidzeklis:

  krasa = "melna"

  def __init__ (self, nosaukums, max_atrums, nobraukums):
    self.nosaukums = nosaukums
    self.max_atrums = max_atrums
    self.nobraukums = nobraukums 

  def sedvietu_skaits(self, skaits):
    self.skaits = skaits
    return f"sedvietu skaits {self.nosaukums} ir {self.skaits} vietas."

  def biletes(self):
    return self.skaits * 0.5

#modelis = transportlidzeklis("mercedes" ,150,55)
#print(modelis.nosaukums, modelis.max_atrums, modelis.nobraukums) 


class buss(transportlidzeklis):
  def sedvietu_skaits(self, skaits = 50):
    return super().sedvietu_skaits(skaits = 50)

  def biletes(self):
    return super().biletes()


#modelisx = buss("mercedes", 150,55)
#print(modelisx.nosaukums, modelisx.max_atrums, modelisx.nobraukums)

skolas_buss = buss("mercedes", 140,20)
print(skolas_buss.sedvietu_skaits(100))
print(skolas_buss.krasa, skolas_buss.nosaukums, "atrums:",skolas_buss.max_atrums,"nobraukums:", skolas_buss.nobraukums)
print(skolas_buss.biletes())