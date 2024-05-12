from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

# FUNCTIONALITIES
def clear():
    email_entry.delete(0, END)
    password_entry.delete(0, END)

#To clear
#for text in mail entry to disappear
def on_pressed(event):
    if email_entry.get() == "Email":
        email_entry.delete(0, END)

#for text in password entry to disappear
def on_push(arg):
    if password_entry.get() == "Password":
        password_entry.delete(0, END)



#login functionality
def login_confirm():
    if email_entry.get()=='' or password_entry.get()=='':
        messagebox.showerror("Error", 'All fields are required')
    else:
        try:
           connection = mysql.connector.connect(
               host="localhost",
                user="root",
                password="123prince",
           )
           cursor = connection.cursor()
           cursor.execute("USE qwerty1;")
           query = 'select * from qwerty1 where email= %s and password=%s;'
           cursor.execute(query, (email_entry.get(), password_entry.get()))
           row = cursor.fetchone()
           if row == NONE:
                messagebox.showerror('Error', 'Email or Password does not exists')
           else:
               messagebox.showinfo('Success', 'Login Successful')
               connection.close()
               clear()
               signin_window.destroy()
               import convertor_app
        except:
            messagebox.showerror('Could not connect to database')
           

    

# GUI CODE
signin_window = Tk()
signin_window.geometry('990x660')# Defining the size of the window
signin_window.title("loginPage")

# I used the var bgimage to hold the image
bgImage = ImageTk.PhotoImage(file= "brando-makes-branding-EYGFG3thfAo-unsplash.jpg")


# had to place it in a label
Label1 = Label(signin_window, image=bgImage)


# Positioning the label
Label1.place(x=0 , y=0)

# Label whisch is the User login page 
Header = Label(signin_window, text= "USER LOGIN" ,font=("Microsoft Yahei UI Light",24,"bold") ,bg="#B2BEB5") #fg ="any color" can be used to change the text color
# Positioning the label
Header.place(x=390, y=140)

# Label for the second
email_label= Label(signin_window , text= "Email" , font=("Microsoft Yahei UI Light",14,"bold"), bg="#B2BEB5")
# Positioning the label
email_label.place(x=390, y=200)


# Entry Tab
email_entry = Entry(signin_window, width= 25, font=("Microsoft Yahei UI Light",9,"bold"), bd=0)
email_entry.insert(0,"Email")
email_entry.bind('<FocusIn>', on_pressed)
# Positioning the entry
email_entry.place(x=390, y=230)

# Password label
pasword1= Label(signin_window, text="Password", font=("Microsoft Yahei UI Light",14,"bold"),bg="#B2BEB5")

# Positioning password labe
pasword1.place(x=390, y=260)

# Entry Tab
password_entry = Entry(signin_window, width= 25,font=("Microsoft Yahei UI Light",9,"bold"), bd=0)
password_entry.insert(0,"Password")
password_entry.bind('<FocusIn>', on_push)

# Positioning the entry
password_entry.place(x=390, y=290)

#Sign in button
myButton = Button(signin_window , text="Login" ,font=("Microsoft Yahei UI Light",10,"bold"), bd=0 , bg="#B2BEB5" , command=login_confirm())

# Positioning of button
myButton.place(x=390, y=330)

signin_window.mainloop()
