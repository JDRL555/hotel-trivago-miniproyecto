from tkinter            import *  
from views.Huesped      import Huesped
from views.Habitacion   import Habitacion
from views.Ingreso      import Ingreso

def open_huesped(root, bg_img):
  Huesped(root, bg_img)

def open_habitacion(root, bg_img):
  Habitacion(root, bg_img)

def open_ingreso(root, bg_img):
  Ingreso(root, bg_img)

class MainView(Canvas):
  def __init__(self, root, bg_img):
    super().__init__(root)

    self.propagate(False)
    self.root   = root 

    self.create_image(0, 0, image=bg_img, anchor="nw")
    
    self.create_text(
      600, 100, 
      text="Hotel Trivago",
      fill="white",
      font=("Roboto", 30),
    )

    self.create_text(
      600, 150, 
      text="Selecciona lo que deseas controlar:",
      fill="white",
      font=("Roboto", 20),
    )

    huesped_btn = Button(
      self.root,
      width=40, 
      text="Huesped",
      bg="#428ef3",
      fg="white",
      pady=10,
      font=("Roboto", 16),
      borderwidth=0,
      activebackground="#2c5d9e",
      cursor="hand2",
      command=lambda: open_huesped(self.root, bg_img)
    )

    habitacion_btn = Button(
      self.root,
      width=40, 
      text="Habitacion",
      bg="#f3984e",
      fg="white",
      pady=10,
      font=("Roboto", 16),
      borderwidth=0,
      activebackground="#a06535",
      cursor="hand2",
      command=lambda: open_habitacion(self.root, bg_img)
    )

    ingreso_btn = Button(
      self.root,
      width=40, 
      text="Ingreso",
      bg="#f53c3c",
      fg="white",
      pady=10,
      font=("Roboto", 16),
      borderwidth=0,
      activebackground="#a32828",
      cursor="hand2",
      command=lambda: open_ingreso(self.root, bg_img)
    )

    huesped_btn.bind("<Enter>", lambda e: huesped_btn.configure(bg="#6aaafd"))
    huesped_btn.bind("<Leave>", lambda e: huesped_btn.configure(bg="#428ef3"))
    huesped_btn.place(x=350, y=200)

    habitacion_btn.bind("<Enter>", lambda e: habitacion_btn.configure(bg="#f5b47f"))
    habitacion_btn.bind("<Leave>", lambda e: habitacion_btn.configure(bg="#f3984e"))
    habitacion_btn.place(x=350, y=300)

    ingreso_btn.bind("<Enter>", lambda e: ingreso_btn.configure(bg="#f87474"))
    ingreso_btn.bind("<Leave>", lambda e: ingreso_btn.configure(bg="#f53c3c"))
    ingreso_btn.place(x=350, y=400)

    self.pack(fill="both", expand=True)