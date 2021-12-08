import tkinter as tk
import random

def akmens(event):
  lbl_lietizv["text"] = "tava izvele:akmens"
  dat_izvele()

def papirits(event):
  lbl_lietizv["text"] = "tava izvele:papirits"
  dat_izvele()

def skeres(event):
  lbl_lietizv["text"] = "tava izvele:skeres"
  dat_izvele()

def dat_izvele():
  izvele = ["akmens", "skeres", "papirits"]
  datizv = random.choice(izvele)
  lbl_datorizv["text"] = f"datora izvele: {datizv}"
  rezultats()

def rezultats():
  dators = lbl_datorizv["text"]
  lietotajs = lbl_lietizv["text"]
  dators = dators.split()

  lietotajs = lietotajs.split()

  if dators[2] == lietotajs[2]:
    lbl_rezultats["text"] = "rezultats:neizskirts"
  else:
    lbl_rezultats["text"] = "vel jamegina"
window = tk.Tk()

lbl_info = tk.Label(text = "sveicinats!\nsi ir spele akmens, skeres, papirits!")

lbl_darit = tk.Label(text = "izvelies kadu no zemak piedavatajiem variantiem:")

lbl_lietizv = tk.Label()
lbl_datorizv = tk.Label()

lbl_rezultats = tk.Label()

btn_akmens = tk.Button(text = "akmens")
btn_skeres = tk.Button(text = "skeres")
btn_papirits = tk.Button(text = "papirits")

btn_akmens.bind("<Button-1>", akmens)
btn_skeres.bind("<Button-1>", skeres)
btn_papirits.bind("<Button-1>", papirits)

lbl_info.pack(fill = tk.X)
lbl_darit.pack()
btn_akmens.pack()
btn_papirits.pack()
btn_skeres.pack()
lbl_lietizv.pack()
lbl_datorizv.pack()
lbl_rezultats.pack()

window.mainloop()