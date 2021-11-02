import tkinter as tk

window = tk.Tk()

label = tk.Label(
  text = "Sveiki! Sveiki! Sveiki! Sveiki!",
  foreground = "red",
  background = "#34A2FE"
  )

label1 = tk.Label(
  text = "Uzredzēšanos!",
  fg = "red",
  bg = "#34A2FE",
  width = 10,
  height = 7
  )

label.pack()
label1.pack()

window.mainloop()