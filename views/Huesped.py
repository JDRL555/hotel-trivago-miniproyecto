from tkinter            import *
from tkinter.messagebox import *

from controllers.huesped import huesped as controller 

class Huesped(Toplevel):
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
      "Apellidos del huésped",
      "Nombres del huésped",
      "Dirección del huésped",
      "Ciudad del huésped",
      "Email del huésped",
      "Teléfono del huésped",
    ]

    def on_cancel():
      self.destroy()
      Huesped(self.root, self.bg_img)

    def on_save(ced_hue, ape_hue, nom_hue, dir_hue, ciu_hue, email_hue, tel_hue): 
      resultado = controller.insert(ced_hue, ape_hue, nom_hue, dir_hue, ciu_hue, email_hue, tel_hue)
      print(resultado)
      if resultado.get("error"):
        showerror("ERROR", resultado.get("msg"))
      else:
        if resultado.get("msg") == 1:
          showinfo("Respuesta", "Registrado exitosamente")

    def on_update(ced_hue, ape_hue, nom_hue, dir_hue, ciu_hue, email_hue, tel_hue):
      resultado = controller.update(ced_hue, ape_hue, nom_hue, dir_hue, ciu_hue, email_hue, tel_hue)
      print(resultado)
      if resultado.get("error"):
        showerror("ERROR", resultado.get("msg"))
      else:
        if resultado.get("msg") == 1:
          showinfo("Respuesta", "Editado exitosamente")
        else:
          showwarning("Respuesta", "Debes cambiar al menos una columna")

    def on_before_update(codigo_entry, accept_btn, ced_hue):
      print(ced_hue)
      resultado = controller.select_one(ced_hue)

      print(f"resultado: {resultado}")

      if isinstance(resultado.get("msg"), str):
        showerror("ERROR", "Habitación no encontrada")
        on_cancel()
      else:
        codigo_entry.destroy()
        accept_btn.destroy()

        huesped = {
          "Cédula del huésped": resultado.get("msg")[0],
          "Apellidos del huésped": resultado.get("msg")[1],
          "Nombres del huésped": resultado.get("msg")[2],
          "Dirección del huésped": resultado.get("msg")[3],
          "Ciudad del huésped": resultado.get("msg")[4],
          "Email del huésped": resultado.get("msg")[5],
          "Teléfono del huésped": resultado.get("msg")[6],
        }

        print(huesped)

        main_canvas.delete("codigo_texto")

        cedula_variable     = StringVar(main_canvas)
        apellidos_variable  = StringVar(main_canvas)
        nombres_variable    = StringVar(main_canvas)
        direccion_variable  = StringVar(main_canvas)
        ciudad_variable     = StringVar(main_canvas)
        email_variable      = StringVar(main_canvas)
        telefono_variable   = StringVar(main_canvas)

        cedula_variable.set(huesped["Cédula del huésped"])
        apellidos_variable.set(huesped["Apellidos del huésped"])
        nombres_variable.set(huesped["Nombres del huésped"])
        direccion_variable.set(huesped["Dirección del huésped"])
        ciudad_variable.set(huesped["Ciudad del huésped"])
        email_variable.set(huesped["Email del huésped"])
        telefono_variable.set(huesped["Teléfono del huésped"])

        variables = [
          cedula_variable,
          apellidos_variable,
          nombres_variable,
          direccion_variable,
          ciudad_variable,
          email_variable,
          telefono_variable
        ]

        x_text = 550
        y_text = 158

        x_entry = 580
        y_entry = 146

        options = list(huesped.keys())

        for index, option in enumerate(options):
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
            cedula_variable.get(),
            apellidos_variable.get(),
            nombres_variable.get(),
            direccion_variable.get(),
            ciudad_variable.get(),
            email_variable.get(),
            telefono_variable.get()
          )
        ).place(x=650, y=520)

    def on_delete(ced_hue):
      if askyesno("Seguro?", "Estas seguro que deseas eliminar el huesped?"):
        huesped = controller.select_one(ced_hue)
        if not len(huesped.get("msg")):
          showerror("ERROR", "Huesped no encontrado")
        else:
          resultado = controller.delete(ced_hue)
          if resultado.get("error"):
            showerror("ERROR", resultado.get("msg"))
          else:
            if resultado.get("msg") == 1:
              showinfo("Respuesta", "Eliminado exitosamente")

    def on_search(ced_hue):
      resultado = controller.select_one(ced_hue)

      print(resultado)

      if not isinstance(resultado.get("msg"), tuple):
        showerror("ERROR", "Huesped no encontrado")
        on_cancel()
      else:
        huesped = {
          "Cédula del huésped": resultado.get("msg")[0],
          "Apellidos del huésped": resultado.get("msg")[1],
          "Nombres del huésped": resultado.get("msg")[2],
          "Dirección del huésped": resultado.get("msg")[3],
          "Ciudad del huésped": resultado.get("msg")[4],
          "Email del huésped": resultado.get("msg")[5],
          "Teléfono del huésped": resultado.get("msg")[6],
        }

        x_option = 30
        y_option = 250

        y_value = 310

        options = list(huesped.keys())
        values  = list(huesped.values())

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

          x_option += 160

        
        x_value = 35

        for index, value in enumerate(values):
          main_canvas.create_text(
            x_value, y_value, 
            text=value,
            width=360,
            fill="white",
            font=("Roboto", 14),
            justify="center",
            anchor="w"
          )

          if  index == 0: x_value += 160
          if  index == 1: x_value += 160
          if  index == 2: x_value += 180
          if  index == 3: x_value += 130
          if  index == 4: x_value += 180
          if  index == 5: x_value += 180

    def on_click(action):
      select_all_btn.place_forget()
      select_one_btn.place_forget()
      create_btn.place_forget()
      update_btn.place_forget()
      delete_btn.place_forget()
      
      if action=="select_all": 
        resultados     = controller.select_all()
        huespedes     = []
        values        = []

        if not len(resultados.get("msg")):
          showinfo("No hay huespedes", "No hay huespedes registrados")
          on_cancel()
        else:
          for resultado in resultados.get("msg"):
            huespedes.append({
              "Cédula del huésped": resultado[0],
              "Apellidos del huésped": resultado[1],
              "Nombres del huésped": resultado[2],
              "Dirección del huésped": resultado[3],
              "Ciudad del huésped": resultado[4],
              "Email del huésped": resultado[5],
              "Teléfono del huésped": resultado[6],
            })
          
          x_option = 30
          y_option = 170

          y_value = 230

          options = list(huespedes[0].keys())

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

            x_option += 160
          
          for huesped in huespedes:
            x_value = 35
            values  = list(huesped.values())

            for index, value in enumerate(values):
              main_canvas.create_text(
                x_value, y_value, 
                text=value,
                width=360,
                fill="white",
                font=("Roboto", 14),
                justify="center",
                anchor="w"
              )

              if  index == 0: x_value += 160
              if  index == 1: x_value += 160
              if  index == 2: x_value += 180
              if  index == 3: x_value += 130
              if  index == 4: x_value += 180
              if  index == 5: x_value += 180

            y_value += 60

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
          back_btn.place(x=450, y=520)

      if action=="select_one": 
        ced_hue = StringVar()

        main_canvas.create_text(
          480, 172, 
          text="Cédula del huésped",
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
          textvariable=ced_hue
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
        back_btn.place(x=250, y=520)

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
          command=lambda: on_search(ced_hue.get())
        )
        search_btn.place(x=650, y=520)
      
      if action=="create":
        cedula_variable     = StringVar()
        apellidos_variable  = StringVar()
        nombres_variable    = StringVar()
        direccion_variable  = StringVar()
        ciudad_variable     = StringVar()
        email_variable      = StringVar()
        telefono_variable   = StringVar()

        variables = [
          cedula_variable,
          apellidos_variable,
          nombres_variable,
          direccion_variable,
          ciudad_variable,
          email_variable,
          telefono_variable,
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
        back_btn.place(x=250, y=520)

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
            cedula_variable.get(),
            apellidos_variable.get(),
            nombres_variable.get(),
            direccion_variable.get(),
            ciudad_variable.get(),
            email_variable.get(),
            telefono_variable.get(),
          )
        )
        save_btn.place(x=650, y=520)
      
      if action=="update": 
        ced_hue = StringVar()

        main_canvas.create_text(
          480, 172, 
          text="Cédula del huésped",
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
          textvariable=ced_hue
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
        back_btn.place(x=250, y=520)

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
          command=lambda: on_before_update(codigo_entry, accept_btn, ced_hue.get())
        )
        accept_btn.place(x=650, y=520)
      
      if action=="delete": 
        ced_hue = StringVar()

        main_canvas.create_text(
          480, 172, 
          text="Cédula del huésped",
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
          textvariable=ced_hue
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
        back_btn.place(x=250, y=520)

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
          command=lambda: on_delete(ced_hue.get())
        )
        
        search_btn.place(x=650, y=520)

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
      text="Huesped",
      fill="white",
      font=("Roboto", 30),
    )

    select_all_btn = Button(
      main_canvas,
      width=40, 
      text="Ver todos los huespedes",
      bg="#428ef3",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#745830",
      activeforeground="white",
      cursor="hand2",
      command=lambda: on_click("select_all")
    )

    select_one_btn = Button(
      main_canvas,
      width=40, 
      text="Ver un huesped",
      bg="#428ef3",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#745830",
      activeforeground="white",
      command=lambda: on_click("select_one"),
      cursor="hand2"
    )

    create_btn = Button(
      main_canvas,
      width=40, 
      text="Registrar nuevo huesped",
      bg="#428ef3",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#745830",
      activeforeground="white",
      command=lambda: on_click("create"),
      cursor="hand2"
    )

    update_btn = Button(
      main_canvas,
      width=40, 
      text="Editar un huesped",
      bg="#428ef3",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#745830",
      activeforeground="white",
      command=lambda: on_click("update"),
      cursor="hand2"
    )

    delete_btn = Button(
      main_canvas,
      width=40, 
      text="Eliminar un huesped",
      bg="#428ef3",
      fg="white",
      pady=10,
      font=("Roboto", 14),
      borderwidth=0,
      activebackground="#745830",
      activeforeground="white",
      command=lambda: on_click("delete"),
      cursor="hand2"
    )

    select_all_btn.bind("<Enter>", lambda e: select_all_btn.configure(bg="#6aaafd"))
    select_one_btn.bind("<Enter>", lambda e: select_one_btn.configure(bg="#6aaafd"))
    create_btn.bind("<Enter>", lambda e: create_btn.configure(bg="#6aaafd"))
    update_btn.bind("<Enter>", lambda e: update_btn.configure(bg="#6aaafd"))
    delete_btn.bind("<Enter>", lambda e: delete_btn.configure(bg="#6aaafd"))

    select_all_btn.bind("<Leave>", lambda e: select_all_btn.configure(bg="#428ef3"))
    select_one_btn.bind("<Leave>", lambda e: select_one_btn.configure(bg="#428ef3"))
    create_btn.bind("<Leave>", lambda e: create_btn.configure(bg="#428ef3"))
    update_btn.bind("<Leave>", lambda e: update_btn.configure(bg="#428ef3"))
    delete_btn.bind("<Leave>", lambda e: delete_btn.configure(bg="#428ef3"))

    select_all_btn.place(x=100, y=200)
    select_one_btn.place(x=700, y=200)
    create_btn.place(x=100, y=300)
    update_btn.place(x=700, y=300)
    delete_btn.place(x=400, y=400)

    main_canvas.pack(fill="both", expand=True)

    if self:
      self.root.withdraw()