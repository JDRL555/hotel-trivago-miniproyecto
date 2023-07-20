from tkinter            import *
from tkinter.messagebox import *

class Ingreso(Toplevel):
  def __init__(self, root, bg_img):

    super().__init__(root)

    self.root   = root
    self.bg_img = bg_img
    self.title("Habitacion")
    self.propagate(False)
    self.resizable(width=False, height=False)
    self.config(
      width=1200, height=600
    )

    logo  = PhotoImage(file="image/hotel.png")
    self.iconphoto(False, logo, logo)

    def on_exit():
      if askokcancel("Seguro?", "Estas seguro que deseas salir del sistema?"):
        self.root.destroy()

    self.protocol("WM_DELETE_WINDOW", on_exit)

    self.options = [
      "Cédula del huésped",
      "Código de habitación",
      "Fecha de ingreso del huésped",
      "Fecha de salida del huésped",
      "Cantidad de personas que ocupan la habitación",
    ]

    def on_cancel():
      self.destroy()
      Ingreso(self.root, self.bg_img)

    def on_save(): 
      showinfo("Exito", "Registrado exitosamente!")

    def on_update(codigo_entry):
      codigo_entry.destroy()
      main_canvas.delete("codigo_texto")

      cedula_variable         = StringVar(main_canvas)
      codigo_variable         = StringVar(main_canvas)
      fecha_ingreso_variable  = StringVar(main_canvas)
      fecha_salida_variable   = StringVar(main_canvas)
      cantidad_variable       = StringVar(main_canvas)

      cedula_variable.set("31386760")
      codigo_variable.set("COD1")
      fecha_ingreso_variable.set("20-06-2023")
      fecha_salida_variable.set("21-06-2023")
      cantidad_variable.set("1")

      variables = [
        cedula_variable,
        codigo_variable,
        fecha_ingreso_variable,
        fecha_salida_variable,
        cantidad_variable
      ]

      x_text = 550
      y_text = 158

      x_entry = 580
      y_entry = 146

      for index, option in enumerate(self.options):
        main_canvas.create_text(
          x_text, y_text, 
          text=option,
          width=1000,
          fill="white",
          font=("Roboto", 16),
          justify="right",
          anchor="e"
        )

        entry = Entry(
          main_canvas,
          width=45,
          font=("Roboto", 14),
          textvariable=variables[index]
        )
        entry.place(x=x_entry, y=y_entry)

        if index == 2:
          y_text += 60
          y_entry += 60
        else:  
          y_text += 50
          y_entry += 50

    def on_delete():
      if askyesno("Seguro?", "Estas seguro que deseas eliminar el ingreso?"):
        showinfo("Exito", "ingreso eliminado exitosamete")

    def on_search():
      ingreso = {
        "Cédula del huésped": "31386760",
        "Código de habitación": "COD1",
        "Fecha de ingreso del huésped": "20-06-2023",
        "Fecha de salida del huésped": "21-06-2023",
        "Cantidad de personas que ocupan la habitación": "1",
      }

      x_option = 140
      y_option = 250

      y_value = 310

      options = list(ingreso.keys())
      values  = list(ingreso.values())

      for index, option in enumerate(options):
        main_canvas.create_text(
          x_option, y_option, 
          text=option,
          width=150,
          fill="white",
          font=("Roboto", 14),
          justify="center",
          anchor="w"
        )

        x_option += 200

      
      x_value = 140

      for index, value in enumerate(values):
        main_canvas.create_text(
          x_value, y_value, 
          text=value,
          width=150,
          fill="white",
          font=("Roboto", 14),
          justify="center",
          anchor="w"
        )

        if  index == 0: x_value += 210 
        if  index == 1: x_value += 220 
        if  index == 2: x_value += 210 
        if  index == 3: x_value += 210

    def on_click(action):
      select_all_btn.place_forget()
      select_one_btn.place_forget()
      create_btn.place_forget()
      update_btn.place_forget()
      delete_btn.place_forget()
      
      if action=="select_all": 
        ingresos = [
          {
            "Código de ingreso": "1",
            "Cédula del huésped": "31386760",
            "Código de habitación": "COD1",
            "Fecha de ingreso del huésped": "20-06-2023",
            "Fecha de salida del huésped": "21-06-2023",
            "Cantidad de personas que ocupan la habitación": "1",
          },
          {
            "Código de ingreso": "2",
            "Cédula del huésped": "30297705",
            "Código de habitación": "COD2",
            "Fecha de ingreso del huésped": "03-02-2022",
            "Fecha de salida del huésped": "03-03-2023",
            "Cantidad de personas que ocupan la habitación": "4",
          },
          {
            "Código de ingreso": "3",
            "Cédula del huésped": "29507396",
            "Código de habitación": "COD1",
            "Fecha de ingreso del huésped": "14-04-2023",
            "Fecha de salida del huésped": "02-07-2023",
            "Cantidad de personas que ocupan la habitación": "2",
          },
        ]

        x_option = 50
        y_option = 170

        y_value = 230

        options = list(ingresos[0].keys())

        for index, option in enumerate(options):
          main_canvas.create_text(
            x_option, y_option, 
            text=option,
            width=150,
            fill="white",
            font=("Roboto", 14),
            justify="center",
            anchor="w"
          )
 
          x_option += 200
        
        for ingreso in ingresos:
          x_value = 90
          values  = list(ingreso.values())

          for index, value in enumerate(values):
            main_canvas.create_text(
              x_value, y_value, 
              text=value,
              width=150,
              fill="white",
              font=("Roboto", 14),
              justify="center",
              anchor="w"
            )

            if  index == 0: x_value += 160 
            if  index == 1: x_value += 220 
            if  index == 2: x_value += 200 
            if  index == 3: x_value += 200
            if  index == 4: x_value += 230

          y_value += 40

        back_btn = Button(
          main_canvas,
          width=30, 
          text="Volver",
          bg="#f53c3c",
          fg="white",
          pady=10,
          font=("Roboto", 14),
          borderwidth=0,
          activebackground="#a32828",
          activeforeground="white",
          cursor="hand2",
          command=on_cancel
        )
        back_btn.place(x=450, y=470)

      if action=="select_one": 
        main_canvas.create_text(
          480, 172, 
          text="Código de ingreso",
          width=500,
          fill="white",
          font=("Roboto", 16),
          justify="right",
          anchor="e"
        )

        Entry(
          main_canvas,
          width=45,
          font=("Roboto", 14)
        ).place(x=550, y=160)

        back_btn = Button(
          main_canvas,
          width=30, 
          text="Volver",
          bg="#f53c3c",
          fg="white",
          pady=10,
          font=("Roboto", 14),
          borderwidth=0,
          activebackground="#a32828",
          activeforeground="white",
          cursor="hand2",
          command=on_cancel
        )
        back_btn.place(x=250, y=470)

        search_btn = Button(
          main_canvas,
          width=30, 
          text="Buscar",
          bg="#6cc950",
          fg="white",
          pady=10,
          font=("Roboto", 14),
          borderwidth=0,
          activebackground="#447e32",
          activeforeground="white",
          cursor="hand2",
          command=on_search
        )
        search_btn.place(x=650, y=470)
      
      if action=="create": 
        x_text = 550
        y_text = 172

        x_entry = 580
        y_entry = 160

        for index, option in enumerate(self.options):
          main_canvas.create_text(
            x_text, y_text, 
            text=option,
            width=1000,
            fill="white",
            font=("Roboto", 16),
            justify="right",
            anchor="e"
          )

          Entry(
            main_canvas,
            width=45,
            font=("Roboto", 14)
          ).place(x=x_entry, y=y_entry)

          if index == 2:
            y_text += 60
            y_entry += 60
          else:  
            y_text += 50
            y_entry += 50

        back_btn = Button(
          main_canvas,
          width=30, 
          text="Volver",
          bg="#f53c3c",
          fg="white",
          pady=10,
          font=("Roboto", 14),
          borderwidth=0,
          activebackground="#a32828",
          activeforeground="white",
          cursor="hand2",
          command=on_cancel
        )
        back_btn.place(x=250, y=470)

        save_btn = Button(
          main_canvas,
          width=30, 
          text="Guardar",
          bg="#6cc950",
          fg="white",
          pady=10,
          font=("Roboto", 14),
          borderwidth=0,
          activebackground="#447e32",
          activeforeground="white",
          cursor="hand2",
          command=on_save
        )
        save_btn.place(x=650, y=470)
      
      if action=="update": 
        main_canvas.create_text(
          480, 172, 
          text="Código de ingreso",
          width=500,
          fill="white",
          font=("Roboto", 16),
          justify="right",
          anchor="e",
          tags="codigo_texto"
        )

        codigo_entry = Entry(
          main_canvas,
          width=45,
          font=("Roboto", 14)
        )
        codigo_entry.place(x=550, y=160)

        back_btn = Button(
          main_canvas,
          width=30, 
          text="Volver",
          bg="#f53c3c",
          fg="white",
          pady=10,
          font=("Roboto", 14),
          borderwidth=0,
          activebackground="#a32828",
          activeforeground="white",
          cursor="hand2",
          command=on_cancel
        )
        back_btn.place(x=250, y=470)

        accept_btn = Button(
          main_canvas,
          width=30, 
          text="Aceptar",
          bg="#6cc950",
          fg="white",
          pady=10,
          font=("Roboto", 14),
          borderwidth=0,
          activebackground="#447e32",
          activeforeground="white",
          cursor="hand2",
          command=lambda: on_update(codigo_entry)
        )
        accept_btn.place(x=650, y=470)
      
      if action=="delete": 
        main_canvas.create_text(
          480, 172, 
          text="Código de ingreso",
          width=500,
          fill="white",
          font=("Roboto", 16),
          justify="right",
          anchor="e"
        )

        Entry(
          main_canvas,
          width=45,
          font=("Roboto", 14)
        ).place(x=550, y=160)

        back_btn = Button(
          main_canvas,
          width=30, 
          text="Volver",
          bg="#f53c3c",
          fg="white",
          pady=10,
          font=("Roboto", 14),
          borderwidth=0,
          activebackground="#a32828",
          activeforeground="white",
          cursor="hand2",
          command=on_cancel
        )
        back_btn.place(x=250, y=470)

        search_btn = Button(
          main_canvas,
          width=30, 
          text="Aceptar",
          bg="#6cc950",
          fg="white",
          pady=10,
          font=("Roboto", 14),
          borderwidth=0,
          activebackground="#447e32",
          activeforeground="white",
          cursor="hand2",
          command=on_delete
        )
        
        search_btn.place(x=650, y=470)

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
      text="Ingreso",
      fill="white",
      font=("Roboto", 30),
    )

    select_all_btn = Button(
      main_canvas,
      width=40, 
      text="Ver todos los ingresos",
      bg="#f53c3c",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#a32828",
      activeforeground="white",
      cursor="hand2",
      command=lambda: on_click("select_all")
    )

    select_one_btn = Button(
      main_canvas,
      width=40, 
      text="Ver un ingreso",
      bg="#f53c3c",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#a32828",
      activeforeground="white",
      command=lambda: on_click("select_one"),
      cursor="hand2"
    )

    create_btn = Button(
      main_canvas,
      width=40, 
      text="Registrar nuevo ingreso",
      bg="#f53c3c",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#a32828",
      activeforeground="white",
      command=lambda: on_click("create"),
      cursor="hand2"
    )

    update_btn = Button(
      main_canvas,
      width=40, 
      text="Editar un ingreso",
      bg="#f53c3c",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#a32828",
      activeforeground="white",
      command=lambda: on_click("update"),
      cursor="hand2"
    )

    delete_btn = Button(
      main_canvas,
      width=40, 
      text="Eliminar un ingreso",
      bg="#f53c3c",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#a32828",
      activeforeground="white",
      command=lambda: on_click("delete"),
      cursor="hand2"
    )

    select_all_btn.bind("<Enter>", lambda e: select_all_btn.configure(bg="#f87474"))
    select_one_btn.bind("<Enter>", lambda e: select_one_btn.configure(bg="#f87474"))
    create_btn.bind("<Enter>", lambda e: create_btn.configure(bg="#f87474"))
    update_btn.bind("<Enter>", lambda e: update_btn.configure(bg="#f87474"))
    delete_btn.bind("<Enter>", lambda e: delete_btn.configure(bg="#f87474"))

    select_all_btn.bind("<Leave>", lambda e: select_all_btn.configure(bg="#f53c3c"))
    select_one_btn.bind("<Leave>", lambda e: select_one_btn.configure(bg="#f53c3c"))
    create_btn.bind("<Leave>", lambda e: create_btn.configure(bg="#f53c3c"))
    update_btn.bind("<Leave>", lambda e: update_btn.configure(bg="#f53c3c"))
    delete_btn.bind("<Leave>", lambda e: delete_btn.configure(bg="#f53c3c"))

    select_all_btn.place(x=100, y=200)
    select_one_btn.place(x=700, y=200)
    create_btn.place(x=100, y=300)
    update_btn.place(x=700, y=300)
    delete_btn.place(x=400, y=400)

    main_canvas.pack(fill="both", expand=True)

    if self:
      self.root.withdraw()