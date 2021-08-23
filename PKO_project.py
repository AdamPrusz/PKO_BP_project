from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import attachment_module as attachment
import find_file_module as find_file

root = Tk()
root.title("POTWIERDZENIE MEGA KAM")
root.geometry("340x220")

def popup(send_email):
    response = messagebox.showinfo("Potwierdzenie MEGAKAM", "Gratulacje! Wysłałeś potwierdzenie do księgowej.")
    label_popup = Label(root, text = response)
    label_popup.pack()
    return send_email

def button_zus_click():
    top = Toplevel()
    top.title("ZUS")
    top.geometry("270x200")

    label_first = Label(top, text = f"Czy chcesz wysłać ZUS \n {find_file.filename}?", \
                        font=  ('Helvetica', 10, 'bold'), pady = 30)
    label_password = Label(top, text = "Wpisz hasło do poczty -->")
    entry_password = Entry(top, width = 20)
    button_send = Button(top, text = "WYŚLIJ", font = 'bold', command = lambda: popup(attachment.send_email_zus \
                        (entry_password.get(), find_file.file_path)))
    label_first.grid(row = 0, column = 0, columnspan = 2)
    label_password.grid(row = 1, column = 0)
    entry_password.grid(row = 1, column = 1)
    button_send.grid(row = 2, column = 0, columnspan = 2, padx = 20, pady = 20)


def button_skarbowy_click():
    top = Toplevel()
    top.title("Urząd Skarbowy")
    top.geometry("270x200")

    label_first = Label(top, text="Czy chcesz wysłać Urząd Skarbowy \n pko_trans_details_20210822_094155 ?", \
                        font=('Helvetica', 10, 'bold'), pady=30)
    label_password = Label(top, text="Wpisz hasło do poczty -->")
    entry_password = Entry(top, width=20)
    button_send = Button(top, text="WYŚLIJ", font='bold', command=lambda: popup(attachment.send_email_skarbowy \
                        (entry_password.get(), find_file.file_path)))
    label_first.grid(row=0, column=0, columnspan=2)
    label_password.grid(row=1, column=0)
    entry_password.grid(row=1, column=1)
    button_send.grid(row=2, column=0, columnspan=2, padx=20, pady=20)




zus_img = ImageTk.PhotoImage(Image.open(r'C:\Users\adamp\Downloads\zus.jpg'))
skarbowy_img = ImageTk.PhotoImage(Image.open(r'C:\Users\adamp\Downloads\urzad_skarbowy.jpg'))

label_up = Label(root, text = "Z JAKIEGO URZĘDU WYSYŁASZ POTWIERDZENIE?", pady = 30, font = ('Helvetica', 10, 'bold'))
label_zus = Label(root, image = zus_img)
label_skarbowy = Label(root, image = skarbowy_img)
button_zus = Button(root, text = "Wybierz", height = 3, width = 15, padx = 14, command = button_zus_click)
button_skarbowy = Button(root, text = "Wybierz", height = 3, width = 15, padx = 14, command = button_skarbowy_click)

label_up.grid(row = 0, column = 0, columnspan = 2)
label_zus.grid(row = 1, column = 1)
label_skarbowy.grid(row = 2, column = 1)
button_zus.grid(row = 1, column = 0)
button_skarbowy.grid(row = 2, column = 0)









#otwieranie nowego okna
# def open():
#     top = Toplevel()
#     top.title("POTWIERDZENIE")
#     global my_img
#
#     if clicked.get() == "ZUS":
#         my_img = ImageTk.PhotoImage(Image.open(r'C:\Users\adamp\Downloads\Logo_zus.png'))
#     else:
#         my_img = ImageTk.PhotoImage(Image.open(r'C:\Users\adamp\Downloads\urzad_skarbowy.jpg'))
#
#     myLabel1 = Label(top, image=my_img)
#     myLabel2 = Label(top, text="Wysłano potwierdzenie do Księgowej!")
#     myLabel2.config(font =70)
#
#     myLabel1.grid(row=0, column=0)
#     myLabel2.grid(row=1, column=0)

#wybór urzędu

# clicked = StringVar()
# clicked.set("ZUS")
#
# e = Entry(root, width = 50)
# e.grid(row = 2, column = 1)
# password = e.get()
#
#
# myLabel3 = Label(root, text = f"Twój plik to: {ffm.confirmation}")
# myLabel4 = Label(root, text = "Wybierz Urząd")
# drop = OptionMenu(root, clicked, "ZUS", "Urząd Skarbowy")
# myLabel5 = Label(root, text = "Wpisz hasło poczty")
# myButton = Button(root, text = "Wyślij", padx = 40, command = open)
#
# myLabel3.grid(row = 0, column = 1, columnspan = 2)
# myLabel4.grid(row = 1, column = 0)
# myLabel5.grid(row = 2, column = 0)
#
# drop.grid(row = 1, column = 1)
# myButton.grid(row = 3, column = 1)


#działanie programu
root.mainloop()