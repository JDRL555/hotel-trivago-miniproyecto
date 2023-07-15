from tkinter    import Tk, PhotoImage
from views.main import MainView

app = Tk()

app.resizable(width=False, height=False)
app.geometry("800x400")

app.title("Hotel Trivago App")

logo = PhotoImage(file="image/hotel.png")

app.iconphoto(False, logo, logo)

main_view = MainView(app)
main_view.config(bg="#72b6b6", width=800, height=400, pady=20, padx=20)
main_view.pack()

app.mainloop()