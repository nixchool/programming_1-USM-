from tkinter import *
from login.login_form import login_screen
from login.reg_form import reg_screen
def screen():
    window = Tk()
    window.title('Options')
    window.geometry('300x300')
    label = Label(window, text='Choose anyone', bg='blue', height=2, width=45)
    label.grid(row=1, column=1)
    button = Button(text='Login', command=login_screen, height=2, width=15)
    button.grid(row=5, column=1, pady=20)
    button = Button(text='Register', command=reg_screen, height=2, width=15)
    button.grid(row=10, column=1)
    window.mainloop()
screen()











