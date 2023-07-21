from tkinter            import *
from tkinter.messagebox import *

from controllers.habitacion import habitacion as controller 

class Habitacion(Toplevel):
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
      "Código de habitación",
      "Número de la habitación",
      "Tipo de habitación \n(N normal, E ejecutiva, S suite)",
      "Capacidad de la habitación \n(I individual, M matrimonial, D doble, T triple)",
      "Precio de la habitación",
    ]
    
    def on_cancel():
      self.destroy()
      Habitacion(self.root, self.bg_img)

    def on_save(cod, num, tip, cap, pre): 
      resultado = controller.insert(cod, num, tip, cap, pre)
      print(resultado)
      if resultado.get("error"):
        showerror("ERROR", resultado.get("msg"))
      else:
        if resultado.get("msg") == 1:
          showinfo("Respuesta", "Registrado exitosamente")

    def on_update(cod_hab, num_hab, tip_hab, cap_hab, pre_hab, sta_hab): 
      resultado = controller.update(cod_hab, num_hab, tip_hab, cap_hab, pre_hab, sta_hab)
      print(resultado)
      if resultado.get("error"):
        showerror("ERROR", resultado.get("msg"))
      else:
        if resultado.get("msg") == 1:
          showinfo("Respuesta", "Editado exitosamente")
        else:
          showwarning("Respuesta", "Debes cambiar al menos una columna")

    def on_before_update(codigo_entry, accept_btn, cod_hab): 
      resultado = controller.select_one(cod_hab)

      if not isinstance(resultado, tuple):
        showerror("ERROR", "Habitación no encontrada")
        on_cancel()
      else:
        codigo_entry.destroy()
        accept_btn.destroy()
        main_canvas.delete("codigo_texto")
        habitacion = {
          "Código de la habitación": resultado[0],
          "Número de la habitación": resultado[1],
          "Tipo de habitación": resultado[2],
          "Capacidad de la habitación": resultado[3],
          "Precio de la habitación": resultado[4],
          "Status de la habitación": resultado[5],
        }

        codigo_variable     = StringVar(main_canvas)
        numero_variable     = StringVar(main_canvas)
        tipo_variable       = StringVar(main_canvas)
        capacidad_variable  = StringVar(main_canvas)
        precio_variable     = StringVar(main_canvas)
        status_variable     = StringVar(main_canvas)

        codigo_variable.set(habitacion["Código de la habitación"])
        numero_variable.set(habitacion["Número de la habitación"])
        tipo_variable.set(habitacion["Tipo de habitación"])
        capacidad_variable.set(habitacion["Capacidad de la habitación"])
        precio_variable.set(habitacion["Precio de la habitación"])
        status_variable.set(habitacion["Status de la habitación"])

        variables = [
          codigo_variable,
          numero_variable,
          tipo_variable,
          capacidad_variable,
          precio_variable,
          status_variable
        ]

        options_update = list(habitacion.keys())

        x_text = 550
        y_text = 158

        x_entry = 580
        y_entry = 146

        for index, option in enumerate(options_update):
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

        Button(
          main_canvas,
          width=30, 
          text="Editar",
          bg="#6cc950",
          fg="white",
          pady=10,
          font=("Roboto", 14),
          borderwidth=0,
          activebackground="#447e32",
          activeforeground="white",
          cursor="hand2",
          command=lambda: on_update(
            codigo_variable.get(),
            numero_variable.get(),
            tipo_variable.get(),
            capacidad_variable.get(),
            precio_variable.get(),
            status_variable.get(),
          )
        ).place(x=650, y=470)

    def on_delete(cod_hab):
      if askyesno("Seguro?", "Estas seguro que deseas eliminar la habitacion?"):
        habitacion = controller.select_one(cod_hab)
        if not isinstance(habitacion, tuple):
          showerror("ERROR", "Habitación no encontrada")
        else:
          resultado = controller.delete(cod_hab)
          if resultado.get("error"):
            showerror("ERROR", resultado.get("msg"))
          else:
            if resultado.get("msg") == 1:
              showinfo("Respuesta", "Eliminado exitosamente")

    def on_search(cod_hab):
      resultado = controller.select_one(cod_hab)

      print(resultado)

      if not isinstance(resultado, tuple):
        showerror("ERROR", "Habitación no encontrada")
        on_cancel()
      else:
        habitacion = {
          "Código de la habitación": resultado[0],
          "Número de la habitación": resultado[1],
          "Tipo de habitación": resultado[2],
          "Capacidad de la habitación": resultado[3],
          "Precio de la habitación": resultado[4],
          "Status de la habitación": resultado[5],
        }

        x_option = 135
        y_option = 230

        y_value = 290

        options = list(habitacion.keys())
        values  = list(habitacion.values())

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

          if index == 2: x_option += 120
          else: x_option += 180
        
        x_value = 145

        for index, value in enumerate(values):
          if index == 4: value = f"{value}$" 
          main_canvas.create_text(
            x_value, y_value, 
            text=value,
            width=150,
            fill="white",
            font=("Roboto", 14),
            justify="center",
            anchor="w"
          )

          if index == 0: x_value += 220 
          elif index == 2: x_value += 150 
          elif index == 3: x_value += 140
          elif index == 4: x_value += 200
          else: x_value += 160

    def on_click(action):
      select_all_btn.place_forget()
      select_one_btn.place_forget()
      create_btn.place_forget()
      update_btn.place_forget()
      delete_btn.place_forget()
      
      if action=="select_all":
        
        resultados    = controller.select_all()
        habitaciones  = []
        values        = []
        
        print(resultados)

        if not len(resultados):
          showinfo("No hay habitaciones", "No hay habitaciones registradas")
          on_cancel()
        else:
          for resultado in resultados:
            habitaciones.append({
              "Código de la habitación": resultado[0],
              "Número de la habitación": resultado[1],
              "Tipo de habitación": resultado[2],
              "Capacidad de la habitación": resultado[3],
              "Precio de la habitación": resultado[4],
              "Status de la habitación": resultado[5],
            })

          x_option = 135
          y_option = 170

          y_value = 230

          options = list(habitaciones[0].keys())

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

            if index == 2: x_option += 120
            else: x_option += 180
          
          for habitacion in habitaciones:
            x_value = 145
            values  = list(habitacion.values())

            for index, value in enumerate(values):
              if index == 4: value = f"{value}$" 

              main_canvas.create_text(
                x_value, y_value, 
                text=value,
                width=150,
                fill="white",
                font=("Roboto", 14),
                justify="center",
                anchor="w"
              )

              if index == 0: x_value += 220 
              elif index == 2: x_value += 150 
              elif index == 3: x_value += 140
              elif index == 4: x_value += 200
              else: x_value += 160

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
        cod_hab = StringVar()

        main_canvas.create_text(
          480, 172, 
          text="Código de habitación",
          width=500,
          fill="white",
          font=("Roboto", 16),
          justify="right",
          anchor="e"
        )

        Entry(
          main_canvas,
          width=45,
          font=("Roboto", 14),
          textvariable=cod_hab
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
          command=lambda: on_search(cod_hab.get())
        )
        search_btn.place(x=650, y=470)
      
      if action=="create": 
        codigo_variable     = StringVar(main_canvas)
        numero_variable     = StringVar(main_canvas)
        tipo_variable       = StringVar(main_canvas)
        capacidad_variable  = StringVar(main_canvas)
        precio_variable     = StringVar(main_canvas)

        variables = [
          codigo_variable,
          numero_variable,
          tipo_variable,
          capacidad_variable,
          precio_variable
        ]

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
            font=("Roboto", 14),
            textvariable=variables[index]
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
          command=lambda: on_save(
            codigo_variable.get(),
            numero_variable.get(),
            tipo_variable.get(),
            capacidad_variable.get(),
            precio_variable.get()
          )
        )
        save_btn.place(x=650, y=470)
      
      if action=="update":
        cod_hab = StringVar()

        main_canvas.create_text(
          480, 172, 
          text="Código de habitación",
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
          font=("Roboto", 14),
          textvariable=cod_hab
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
          command=lambda: on_before_update(codigo_entry, accept_btn, cod_hab.get())
        )
        accept_btn.place(x=650, y=470)
      
      if action=="delete": 
        cod_hab = StringVar()

        main_canvas.create_text(
          480, 172, 
          text="Código de habitación",
          width=500,
          fill="white",
          font=("Roboto", 16),
          justify="right",
          anchor="e"
        )

        Entry(
          main_canvas,
          width=45,
          font=("Roboto", 14),
          textvariable=cod_hab
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
          command=lambda: on_delete(cod_hab.get())
        )
        
        search_btn.place(x=650, y=470)

    def back_to_root(root):
      root.iconify()
      root.deiconify()
      self.destroy()

    main_canvas = Canvas(self)

    main_canvas.create_image(0, 0, image=self.bg_img, anchor="nw")

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