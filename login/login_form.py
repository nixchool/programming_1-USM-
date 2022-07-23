#https://realpython.com/python-exceptions/
#https://www.tcl.tk/man/tcl8.4/TkCmd/cursors.htm
from tkinter import *
from tkinter import messagebox
import os
def login_screen():
    global window2
    global user_inpt
    global password_inpt
    window2 = Tk()
    window2.geometry('600x300')
    window2.title('Login Form')
    user_label = Label(window2, text='Username')
    user_label.grid(row=0, column=1, padx=30)
    user_inpt = Entry(window2)
    user_inpt.grid(row=0, column=2, padx=30)
    password_label = Label(window2, text='Password')
    password_label.grid(row=1, column=1, padx=30)
    password_inpt = Entry(window2, show='*')
    password_inpt.grid(row=1, column=2, padx=30)
    button = Button(window2, text='Login', command=login)
    button.grid(row=2, column=2, padx=30)
    window2.mainloop()


def login():
    global user
    global password
    user = user_inpt.get()
    password = password_inpt.get()
    user_list = os.listdir('employee/users/')
    if user in user_list:
        file = open('employee/users/'+user, "r")
        verify = file.read().splitlines()
        if password in verify:
            messagebox.showinfo('Success', 'You have successfully logged in')
            log_des()
            emp_screen()
        else:
            msg = Label(window2, text='Username or password does not match')
            msg.grid(row=5, column=2)
    else:
        msg = Label(window2, text='Username does not found')
        msg.grid(row=5, column=2)

    if len(user) == 0:
        msg = Label(window2, text='Please enter username ')
        msg.grid(row=5, column=2)

    elif len(password) == 0:
        msg = Label(window2, text='Please enter password')
        msg.grid(row=5, column=2)




def log_des():
    window2.destroy()











#FOR EMPLOYMENT
#FOR EMPLOYMENT SCREEN
def emp_screen():
    global emp_win
    emp_win = Tk()
    emp_win.title('Employee Management')
    emp_win.geometry('510x550')
    label = Label(emp_win, text='Employee Details', bg='blue', height=3, width=75)
    label.grid(row=1, column=1)
    label = Label(emp_win, text='Welcome '+ user).grid(row=2, column=1, padx=30, pady=10)
    button = Button(emp_win, text='Add Employee Details', command=emp_form, height=2, width=25)
    button.grid(row=3, column=1, pady=20)
    button = Button(emp_win,text='View Employee Details',command= view_emp, height=2, width=25)
    button.grid(row=4, column=1,  pady=20)
    button = Button(emp_win, text='Add Department', command=add_deprt, height=2, width=25)
    button.grid(row=5, column=1,  pady=20)
    button = Button(emp_win, text='View Department', command=view_depart, height=2, width=25)
    button.grid(row=6, column=1,  pady=20)
    emp_win.mainloop()


#EMPLOYMENT FORM
def emp_form():
    global window4
    global id_inpt
    global name_inpt
    global age_inpt
    global addr_inpt
    global email_inpt
    global depart_inpt

    window4 = Tk()
    window4.title('Employee Management Form')
    window4.geometry('600x400')
    id_label = Label(window4, text='ID: ')
    id_label.grid(row=0, column=1, padx=30, pady=10)
    id_inpt = Entry(window4)
    id_inpt.grid(row=0, column=2, padx=30, pady=10)

    name_label = Label(window4, text='Name: ')
    name_label.grid(row=1, column=1, padx=30, pady=10)
    name_inpt = Entry(window4)
    name_inpt.grid(row=1, column=2, padx=30, pady=10)

    age_label = Label(window4, text='Age: ')
    age_label.grid(row=2, column=1, padx=30, pady=10)
    age_inpt = Entry(window4)
    age_inpt.grid(row=2, column=2, padx=30, pady=10)

    addr_label = Label(window4, text='Address: ')
    addr_label.grid(row=3, column=1, padx=30, pady=10)
    addr_inpt = Entry(window4)
    addr_inpt.grid(row=3, column=2, padx=30, pady=10)

    email_label = Label(window4, text='Contact Email: ')
    email_label.grid(row=4, column=1, padx=30, pady=10)
    email_inpt = Entry(window4)
    email_inpt.grid(row=4, column=2, padx=30, pady=10)

    depart_label = Label(window4, text='Department')
    depart_label.grid(row=5, column=1, padx=30, pady=10)
    depart_inpt = Entry(window4)
    depart_inpt.grid(row=5, column=2, padx=30, pady=10)

    button = Button(window4, text='Submit', command=save_emp_data)
    button.grid(row=7, column=2, padx=30, pady=10)
    button = Button(window4, text='Reset', command=reset_emp)
    button.grid(row=7, column=3, padx=30, pady=10)
    window4.mainloop()

def reset_emp():
    id_inpt.delete(0, END)
    name_inpt.delete(0, END)
    age_inpt.delete(0, END)
    addr_inpt.delete(0, END)
    email_inpt.delete(0, END)
    depart_inpt.delete(0, END)

#TO SAVE DATA
def save_emp_data():
    global id
    global name
    global age
    global address
    global email
    global department
    id = id_inpt.get()
    name = name_inpt.get()
    age = age_inpt.get()
    address = addr_inpt.get()
    email = email_inpt.get()
    department = depart_inpt.get()
    if len(id) == 0:
        msg = Label(window4, text='Sorry, ID field is empty')
        msg.grid(row=0, column=3, padx=30, )
    elif len(name) == 0:
        msg = Label(window4, text='Sorry, name is empty')
        msg.grid(row=1, column=3, padx=30, )
    elif len(age) == 0:
        msg = Label(window4, text='Sorry, age is empty')
        msg.grid(row=2, column=3, padx=30, )
    elif len(address) == 0:
        msg = Label(window4, text='Sorry, address is empty')
        msg.grid(row=3, column=3, padx=30, )
    elif len(email) == 0:
        msg = Label(window4,text='Sorry, email is empty')
        msg.grid(row=4, column=3, padx=30, )
    elif len(department) == 0:
        msg = Label(window4, text='Sorry, department is empty')
        msg.grid(row=5, column=3, padx=30, )
    else:
        with open('employee/users/'+user+'_employee', 'w+') as empsave:
            empsave.write('name: ' + name + '\nage: ' + age + '\naddress: ' + address + '\ncontact: ' + email + '\ndepartment: ' + department + '\n\n')
            messagebox.showinfo('Success', 'Successfully added')


#FOR VIEW EMPLOYMENT
def view_emp():
    window5 = Tk()
    window5.title('Employee Detail')
    window5.geometry('300x300')
    try:
        with open('employee/users/'+user+'_employee', 'r') as f:
            Label(window5, text=f.read()).grid(row=0, column=0)
    except FileNotFoundError:
        Label(window5, text='Sorry, Employee form is not filled up').grid(row=6, column='3')
    window5.mainloop()


#FOR DEPARTMENT
def add_deprt():
    global depart_code
    global depart_name
    global window6
    window6 = Tk()
    window6.title('Department Form')
    window6.geometry('700x500')
    depart_code = Label(window6, text='Code: ')
    depart_code.grid(row=1, column=1, padx=30, pady=10)
    depart_code = Entry(window6)
    depart_code.grid(row=1, column=2, padx=30, pady=10)

    depart_name = Label(window6, text='Name: ')
    depart_name.grid(row=2, column=1, padx=30, pady=10)
    depart_name = Entry(window6)
    depart_name.grid(row=2, column=2, padx=30, pady=10)

    button = Button(window6, text='Submit', command=save_depart_data)
    button.grid(row=3, column=2, padx=30, pady=10)
    button = Button(window6, text='Reset', command=reset_depart)
    button.grid(row=3, column=3, padx=30, pady=10)
    window6.mainloop()


def save_depart_data():
    global depart_code
    global depart_name
    depart_code = depart_code.get()
    depart_name = depart_name.get()
    if len(depart_code) == 0:
        msg = Label(window6, text='Sorry, ID field is empty')
        msg.grid(row=0, column=3, padx=30, )
    elif len(depart_name) == 0:
        msg = Label(window6, text='Sorry, name is empty')
        msg.grid(row=1, column=3, padx=30, )
    else:
        with open('employee/users/'+user+'_depart', 'w') as save_depart:
            save_depart.write('Department Code:' + depart_code + '\nDepartment Name: ' + depart_name)
            messagebox.showinfo('Success', 'Department have been added')


def reset_depart():
        depart_code.delete(0, END)
        depart_name.delete(0, END)




#FOR VIEW DEPARTMENT
def view_depart():
    window6 = Tk()
    window6.title('Department Detail')
    window6.geometry('300x300')
    try:
        with open('employee/users/' + user + '_depart', 'r') as f:
            Label(window6, text=f.read()).grid(row=0, column=0)
    except FileNotFoundError:
        Label(window6, text='Sorry, departmant form is not filled up').grid(row=3, column=6)

    window6.mainloop()


