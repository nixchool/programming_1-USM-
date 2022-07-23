from tkinter import *
from tkinter import messagebox
import os
from login.login_form import login_screen
def register_des():
    window3.destroy()


def reg_screen():
    global window3
    global user_inpt
    global password_inpt
    global password2_inpt
    window3 = Tk()
    window3.geometry('600x300')
    window3.title('Registration Form')
    user_label = Label(window3, text='Username: ').grid(row=0, column=1)
    user_inpt = Entry(window3)
    user_inpt.grid(row=0, column=2, padx=30)
    password_label = Label(window3, text='Password: ').grid(row=1, column=1)
    password_inpt = Entry(window3, show='*')
    password_inpt.grid(row=1, column=2, padx=30)
    password2_label = Label(window3, text='Confirm Password: ').grid(row=2, column=1)
    password2_inpt = Entry(window3, show='*')
    password2_inpt.grid(row=2, column=2, padx=30)
    button = Button(window3, text='Register', command=register)
    button.grid(row=4, column=2)
    window3.mainloop()





#FOR REGISTRATION
def register():
    user = user_inpt.get()
    password = password_inpt.get()
    password2 = password2_inpt.get()
    user_list = os.listdir('employee/users/')
    if user in user_list:
        file = open('employee/users/' + user, "r")
        file.read().splitlines()
        msg = Label(window3, text='Sorry username already exists')
        msg.grid(row=5, column=2)
    elif len(user) == 0:
        msg = Label(window3, text='Username must be filled')
        msg.grid(row=5, column=2)
    elif len(password) == 0:
        msg = Label(window3, text='Password must be filled')
        msg.grid(row=5, column=2)

    elif password == password2:
        file = open('employee/users/'+user, "a+")
        file.write(user + '\n'+ password + "\n\n")
        file.close()
        messagebox.showinfo('Success', 'You have successfully created your account. \n You have to manually login your account.')
        register_des()
        login_screen()

    else:
        msg = Label(window3, text='Confirm Password does not match')
        msg.grid(row=5, column=2)




