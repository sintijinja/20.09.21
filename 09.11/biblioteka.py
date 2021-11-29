class robots:
  """klase reprezentā robotu ar specifisko vārdu"""


  def  __init__(self, vards):
    """datu inicializācija"""


    self.vards=vards

    print(f"inicializējam{self.vards}")

  def sasveicinaties(self):
    print(f"Sveiks! Mani sauc {self.vards}")




rob1 = robots("r1")


rob1.sasveicinaties()
rob1.sasveicinaties()


rob2 = robots("r2")

rob2.sasveicinaties()
