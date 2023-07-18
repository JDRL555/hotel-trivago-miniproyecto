from tkinter            import *
from tkinter.messagebox import *



class Habitacion(Toplevel):
  def __init__(self, root, bg_img):

    super().__init__(root)

    self.root = root
    self.title("Habitacion")
    self.propagate(False)
    self.resizable(width=False, height=False)
    self.config(
      width=1200, height=600
    )
    logo  = PhotoImage(file="image/hotel.png")
    self.iconphoto(False, logo, logo)

    def confirm():
      if askokcancel("Seguro?", "Estas seguro que deseas salir del sistema?"):
        self.root.destroy()
    
    self.protocol("WM_DELETE_WINDOW", confirm)
    
    def on_click(action):
      select_all_btn.place_forget()
      select_one_btn.place_forget()
      create_btn.place_forget()
      update_btn.place_forget()
      delete_btn.place_forget()
      
      if action=="select_all": pass
      if action=="select_one": pass
      if action=="create": pass
      if action=="update": pass
      if action=="delete": pass

    def back_to_root(root):
      root.iconify()
      root.deiconify()
      self.destroy()

    main_canvas = Canvas(self)

    main_canvas.create_image(0, 0, image=bg_img, anchor="nw")

    back_root_btn = Button(
      main_canvas,
      width=40, 
      text="Volver a la ventana principal",
      bg="#ac8346",
      fg="white",
      pady=10,
      font=("Roboto", 12),
      borderwidth=0,
      activebackground="#745830",
      activeforeground="white",
      cursor="hand2",
      command=lambda: back_to_root(self.root)
    )

    back_root_btn.bind("<Enter>", lambda e: back_root_btn.configure(bg="#cfac78"))
    back_root_btn.bind("<Leave>", lambda e: back_root_btn.configure(bg="#ac8346"))
    back_root_btn.place(x=1, y=1)

    main_canvas.create_text(
      600, 100, 
      text="Habitacion",
      fill="white",
      font=("Roboto", 30),
    )

    select_all_btn = Button(
      main_canvas,
      width=40, 
      text="Ver todos los habitaciones",
      bg="#f3984e",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#a06535",
      activeforeground="white",
      command=lambda: on_click("select_all"),
      cursor="hand2"
    )

    select_one_btn = Button(
      main_canvas,
      width=40, 
      text="Ver una habitacion",
      bg="#f3984e",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#a06535",
      activeforeground="white",
      command=lambda: on_click("select_one"),
      cursor="hand2"
    )

    create_btn = Button(
      main_canvas,
      width=40, 
      text="Registrar nueva habitacion",
      bg="#f3984e",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#a06535",
      activeforeground="white",
      command=lambda: on_click("create"),
      cursor="hand2"
    )

    update_btn = Button(
      main_canvas,
      width=40, 
      text="Editar una habitacion",
      bg="#f3984e",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#a06535",
      activeforeground="white",
      command=lambda: on_click("update"),
      cursor="hand2"
    )

    delete_btn = Button(
      main_canvas,
      width=40, 
      text="Eliminar una habitacion",
      bg="#f3984e",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#a06535",
      activeforeground="white",
      command=lambda: on_click("delete"),
      cursor="hand2"
    )

    select_all_btn.bind("<Enter>", lambda e: select_all_btn.configure(bg="#f5b47f"))
    select_one_btn.bind("<Enter>", lambda e: select_one_btn.configure(bg="#f5b47f"))
    create_btn.bind("<Enter>", lambda e: create_btn.configure(bg="#f5b47f"))
    update_btn.bind("<Enter>", lambda e: update_btn.configure(bg="#f5b47f"))
    delete_btn.bind("<Enter>", lambda e: delete_btn.configure(bg="#f5b47f"))

    select_all_btn.bind("<Leave>", lambda e: select_all_btn.configure(bg="#f3984e"))
    select_one_btn.bind("<Leave>", lambda e: select_one_btn.configure(bg="#f3984e"))
    create_btn.bind("<Leave>", lambda e: create_btn.configure(bg="#f3984e"))
    update_btn.bind("<Leave>", lambda e: update_btn.configure(bg="#f3984e"))
    delete_btn.bind("<Leave>", lambda e: delete_btn.configure(bg="#f3984e"))

    select_all_btn.place(x=100, y=200)
    select_one_btn.place(x=700, y=200)
    create_btn.place(x=100, y=300)
    update_btn.place(x=700, y=300)
    delete_btn.place(x=400, y=400)

    main_canvas.pack(fill="both", expand=True)

    if self:
      self.root.withdraw()