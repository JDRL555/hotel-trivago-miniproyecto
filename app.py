from tkinter            import Tk, PhotoImage, Label, Canvas
from tkinter.messagebox import askokcancel
from views.main         import MainView
from PIL                import Image, ImageTk

def on_exit(app):
  if askokcancel("Seguro?", "Estas seguro que deseas salir del sistema?"):
    app.destroy()

app = Tk()
app.resizable(width=False, height=False)
app.geometry("1200x600")
app.title("Hotel Trivago App")
app.protocol("WM_DELETE_WINDOW", lambda: on_exit(app))

logo = PhotoImage(file="image/hotel.png")
app.iconphoto(False, logo, logo)

pathname = "C:/Users/Joshua/Documents/University_files/Programacion II/hotel-trivago-miniproyecto/image/"

img = Image.open(
  pathname + "fondo.png"
).resize((1200,800))   
bg_img  = ImageTk.PhotoImage(image=img)

img = Image.open(
  pathname + "huesped.png"
).resize((1200,800))   
huesped_img  = ImageTk.PhotoImage(image=img)

img = Image.open(
  pathname + "habitacion.png"
).resize((1200,800))   
habitacion_img  = ImageTk.PhotoImage(image=img)

img = Image.open(
  pathname + "ingreso.png"
).resize((1200,800))   
ingreso_img  = ImageTk.PhotoImage(image=img)

MainView(
  root=app, bg_img=bg_img,
  huesped_img=huesped_img,
  habitacion_img=habitacion_img,
  ingreso_img=ingreso_img
)

app.mainloop()