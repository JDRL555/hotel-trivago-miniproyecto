from tkinter            import Tk, PhotoImage, Label, Canvas
from tkinter.messagebox import askokcancel
from views.main         import MainView
from PIL                import Image, ImageTk

def confirm(app):
  if askokcancel("Seguro?", "Estas seguro que deseas salir del sistema?"):
    app.destroy()

app = Tk()
app.resizable(width=False, height=False)
app.geometry("1200x600")
app.title("Hotel Trivago App")
app.protocol("WM_DELETE_WINDOW", lambda: confirm(app))

logo = PhotoImage(file="image/hotel.png")
app.iconphoto(False, logo, logo)
img = Image.open(
  "C:/Users/Joshua/Documents/University_files/Programacion II/hotel-trivago-miniproyecto/image/fondo.png"
).resize((1200,800))   
bg_img  = ImageTk.PhotoImage(image=img)

MainView(root=app, bg_img=bg_img)

app.mainloop()