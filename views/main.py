from tkinter import *  

class MainView(Frame):
  def __init__(self, root):
    super().__init__(root)
    
    self.root = root
    self.pack_propagate(False)

    Label(
      self, 
      text="Hotel Trivago",
      bg="#72b6b6",
      font=("Roboto", 20)
    ).pack(anchor=CENTER)

    Label(
      self, 
      text="Seleccione una opcion para llevar el control de la misma:",
      bg="#72b6b6",
      padx=20,
      font=("Roboto", 16)
    ).pack(anchor=CENTER)

    Button(
      self,
      width=40, 
      text="Huesped",
      bg="#428ef3",
      fg="white",
      pady=10,
      font=("Roboto", 16),
      borderwidth=0
    ).pack(anchor=CENTER, pady=10)

    Button(
      self,
      width=40, 
      text="Habitacion",
      bg="#f3984e",
      fg="white",
      pady=10,
      font=("Roboto", 16),
      borderwidth=0
    ).pack(anchor=CENTER, pady=10)

    Button(
      self,
      width=40, 
      text="Ingreso",
      bg="#f53c3c",
      fg="white",
      pady=10,
      font=("Roboto", 16),
      borderwidth=0
    ).pack(anchor=CENTER, pady=10)