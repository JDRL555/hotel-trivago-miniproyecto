from tkinter            import *
from tkinter.messagebox import *

from controllers.ingreso    import  ingreso   as controller 
from controllers.huesped    import  huesped   as controller_huesped 
from controllers.habitacion import habitacion as controller_habitacion

class Ingreso(Toplevel):
  def __init__(self, root, bg_img):

    super().__init__(root)

    self.root   = root
    self.bg_img = bg_img
    self.title("Ingreso")
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

    def on_save(ced_hue, cod_hab, fec_ing, fec_sal, can_per): 
      resultado = controller.insert(ced_hue, cod_hab, fec_ing, fec_sal, can_per)
      if resultado.get("error"):
        showerror("ERROR", resultado.get("msg"))
      else:
        if resultado.get("msg") == 1:
          showinfo("Respuesta", "Registrado exitosamente")
        else:
          showinfo("Respuesta", resultado.get("msg"))

    def on_update(fec_ing, fec_sal, can_per, cod_ing):
      resultado = controller.update(fec_ing, fec_sal, can_per, cod_ing)
      print(resultado)
      if resultado.get("error"):
        showerror("ERROR", resultado.get("msg"))
      else:
        if resultado.get("msg") == 1:
          showinfo("Respuesta", "Editado exitosamente")
        else:
          showwarning("Respuesta", "Debes cambiar al menos una columna")

    def on_before_update(codigo_entry, accept_btn, cod_ing):
      print(cod_ing)
      resultado = controller.select_one(cod_ing)

      print(f"resultado: {resultado}")

      if isinstance(resultado.get("msg"), str):
        showerror("ERROR", "Ingreso no encontrado")
        on_cancel()
      else:
        codigo_entry.destroy()
        accept_btn.destroy()

        fecha_1 = resultado.get("msg")[3]
        fecha_2 = resultado.get("msg")[4]
 
        fecha_1 = str(fecha_1)
        fecha_1 = fecha_1.split(" ")
        fecha_1 = fecha_1[0]
        fecha_1 = fecha_1.split("-")
        fecha_1 = f"{fecha_1[2]}-{fecha_1[1]}-{fecha_1[0]}"

        fecha_2 = str(fecha_2)
        fecha_2 = fecha_2.split(" ")
        fecha_2 = fecha_2[0]
        fecha_2 = fecha_2.split("-")
        fecha_2 = f"{fecha_2[2]}-{fecha_2[1]}-{fecha_2[0]}"

        ingreso = {
          "Fecha de ingreso del huésped": fecha_1,
          "Fecha de salida del huésped": fecha_2,
          "Cantidad de personas que ocupan la habitación": resultado.get("msg")[5],
        }

        print(ingreso)

        main_canvas.delete("codigo_texto")

        fecha_ingreso_variable  = StringVar(main_canvas)
        fecha_salida_variable   = StringVar(main_canvas)
        cantidad_variable       = StringVar(main_canvas)

        fecha_ingreso_variable.set(ingreso["Fecha de ingreso del huésped"])
        fecha_salida_variable.set(ingreso["Fecha de salida del huésped"])
        cantidad_variable.set(ingreso["Cantidad de personas que ocupan la habitación"])

        variables = [
          fecha_ingreso_variable,
          fecha_salida_variable,
          cantidad_variable,
        ]

        x_text = 550
        y_text = 158

        x_entry = 580
        y_entry = 146

        options = list(ingreso.keys())

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
            fecha_ingreso_variable.get(),
            fecha_salida_variable.get(),
            cantidad_variable.get(),
            cod_ing,
          )
        ).place(x=650, y=520)

    def on_delete(cod_ing):
      if askyesno("Seguro?", "Estas seguro que deseas eliminar el ingreso?"):
        ingreso = controller.select_one(cod_ing)
        print(ingreso.get("msg"))
        if isinstance(ingreso.get("msg"), str):
          showerror("ERROR", "Ingreso no encontrado")
        else:
          resultado = controller.delete(cod_ing)
          if resultado.get("error"):
            showerror("ERROR", resultado.get("msg"))
          else:
            if resultado.get("msg") == 1:
              showinfo("Respuesta", "Eliminado exitosamente")

    def on_search(cod_ing):
      resultado = controller.select_one(cod_ing)

      print(resultado)

      if not isinstance(resultado.get("msg"), tuple):
        showerror("ERROR", "Ingreso no encontrado")
        on_cancel()
      else:
        ingreso = {
          "Código de ingreso": resultado.get("msg")[0],
          "Cédula del huésped": resultado.get("msg")[1],
          "Código de habitación": resultado.get("msg")[2],
          "Fecha de ingreso del huésped": resultado.get("msg")[3],
          "Fecha de salida del huésped": resultado.get("msg")[4],
          "Cantidad de personas que ocupan la habitación": resultado.get("msg")[5],
        }

        x_option = 50
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

          x_option += 190

        
        x_value = 90

        for index, value in enumerate(values):
          if index == 3 or index == 4: 
            value = str(value)
            value = value.split(" ")
            value = value[0]
          main_canvas.create_text(
            x_value, y_value, 
            text=value,
            width=360,
            fill="white",
            font=("Roboto", 14),
            justify="center",
            anchor="w"
          )

          if  index == 0: x_value += 170
          if  index == 1: x_value += 200
          if  index == 2: x_value += 170
          if  index == 3: x_value += 170
          if  index == 4: x_value += 250

    def on_click(action):
      select_all_btn.place_forget()
      select_one_btn.place_forget()
      create_btn.place_forget()
      update_btn.place_forget()
      delete_btn.place_forget()
      
      if action=="select_all": 
        resultados    = controller.select_all()
        ingresos      = []
        values        = []

        print(resultados)

        if not len(resultados.get("msg")):
          showinfo("No hay ingresos", "No hay ingresos registrados")
          on_cancel()
        else:
          for resultado in resultados.get("msg"):
            ingresos.append({
              "Código de ingreso": resultado[0],
              "Cédula del huésped": resultado[1],
              "Código de habitación": resultado[2],
              "Fecha de ingreso del huésped": resultado[3],
              "Fecha de salida del huésped": resultado[4],
              "Cantidad de personas que ocupan la habitación": resultado[5],
            })
          
          x_option = 50
          y_option = 170

          y_value = 230

          options = list(ingresos[0].keys())

          for index, option in enumerate(options):
            main_canvas.create_text(
              x_option, y_option, 
              text=option,
              width=200,
              fill="white",
              font=("Roboto", 14),
              justify="center",
              anchor="w"
            )

            x_option += 190
          
          for ingreso in ingresos:
            x_value = 90
            values  = list(ingreso.values())

            for index, value in enumerate(values):
              if index == 3 or index == 4: 
                value = str(value)
                value = value.split(" ")
                value = value[0]
              main_canvas.create_text(
                x_value, y_value, 
                text=value,
                width=360,
                fill="white",
                font=("Roboto", 14),
                justify="center",
                anchor="w"
              )

              if  index == 0: x_value += 170
              if  index == 1: x_value += 210
              if  index == 2: x_value += 180
              if  index == 3: x_value += 180
              if  index == 4: x_value += 260

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
        cod_ing = StringVar()

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
          textvariable=cod_ing
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
          command=lambda: on_search(cod_ing.get())
        )
        search_btn.place(x=650, y=520)
      
      if action=="create":
        cedula_variable             = StringVar()
        codigo_habitacion_variable  = StringVar()
        fecha_ingreso_variable      = StringVar()
        fecha_salida_variable       = StringVar()
        cantidad_variable           = StringVar()

        variables = [
          cedula_variable,
          codigo_habitacion_variable,
          fecha_ingreso_variable,
          fecha_salida_variable,
          cantidad_variable,
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

          if index == 0:
            resultados_huespedes  = controller_huesped.select_all()
            opciones              = []

            if not len(resultados_huespedes.get("msg")):
              showinfo("No hay huespedes", "Se necesita al menos un huesped registrado para pode registrar un ingreso")
              on_cancel()
            else:
              for resultado in resultados_huespedes.get("msg"):
                opciones.append(resultado[0])

              seleccionada  = variables[index]
              seleccionada.set(str(opciones[0]))

              menu = OptionMenu(
                main_canvas,
                seleccionada,
                *opciones,
              )
              menu.configure(
                width=42,
                bg="white",
                borderwidth=0,
                font=("Roboto", 14),  
              )
              menu.place(x=x_entry, y=y_entry)
          

          elif index == 1:
            resultados_habitaciones = controller_habitacion.select_all()
            opciones                = []

            if not len(resultados_habitaciones):
              showinfo("No hay habitaciones", "No hay habitaciones registradas")
              on_cancel()
            else:
              for resultado in resultados_habitaciones:
                opciones.append(resultado[0])

              seleccionada  = variables[index]
              seleccionada.set(opciones[0])

              menu = OptionMenu(
                main_canvas,
                seleccionada,
                *opciones,
              )
              menu.configure(
                width=42,
                bg="white",
                borderwidth=0,
                font=("Roboto", 14),
              )
              menu.place(x=x_entry, y=y_entry)
          else:
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
            codigo_habitacion_variable.get(),
            fecha_ingreso_variable.get(),
            fecha_salida_variable.get(),
            cantidad_variable.get(),
          )
        )
        save_btn.place(x=650, y=520)
      
      if action=="update": 
        cod_ing = StringVar()

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
          font=("Roboto", 14),
          textvariable=cod_ing
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
          command=lambda: on_before_update(codigo_entry, accept_btn, cod_ing.get())
        )
        accept_btn.place(x=650, y=520)
      
      if action=="delete": 
        cod_ing = StringVar()

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
          font=("Roboto", 14),
          textvariable=cod_ing
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
          command=lambda: on_delete(cod_ing.get())
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
      activebackground="#a32828",
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
      activebackground="#745830",
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