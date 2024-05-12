from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

def clear():
    email_entry.delete(0, END)
    password_entry.delete(0, END)

    password1_entry.delete(0, END)


# this is to remove the text hint
def on_pressed(anything):
    if email_entry.get() == "Email":       
        email_entry.delete(0, END)


def on_push(somtihng):
    if password_entry.get() == "Password":
        password_entry.delete(0,END)

def on_pass(somtihng):
    if password1_entry.get() == "Confirm password":
        password1_entry.delete(0,END)


def connect_database():
    if email_entry.get()=='' or password_entry.get()=='' or password1_entry.get()=='':
        messagebox.showerror("Error", 'All fields are required')
    elif password_entry.get()!= password1_entry.get():
        messagebox.showerror("Error", 'Passwords do not match')
    else:
        try:
            # Establish connection to the MySQL database
            Connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123prince",
            )
            

            #creating database 
            try:
                cursor = Connection.cursor()
                cursor.execute("CREATE DATABASE qwerty1;")
            
                #specifing the database
                cursor.execute("USE qwerty1;")
                # Create a users table
                cursor.execute("CREATE TABLE qwerty1 (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), password VARCHAR(255))")

                messagebox.showinfo("Success", "Database and table created successfully!")
            except:
                #specifing the database
                query = 'use qwerty1;'
                cursor.execute(query)

                # Inserting the data into the database
                query= 'insert into qwerty1(email, password) values(%s,%s)'
                cursor.execute(query,(email_entry.get(), password1_entry.get()))
                Connection.commit()
                Connection.close()
                messagebox.showinfo('Success', 'Registration Successful')
                # Clearing the entries
                clear()
                signup_window.destroy()
                # Importing the signin page
            import signin_page
            

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Database operation error: {e}')




# Creating the window

signup_window = Tk()
signup_window.title("SignUp_Page")
signup_window.geometry('990x660')

bgImage = ImageTk.PhotoImage(file= "brando-makes-branding-EYGFG3thfAo-unsplash.jpg")

screen_Image= Label(signup_window, image=bgImage)

screen_Image.place(x=0 , y= 0)

#Label whisch is the User login page 
Header = Label(signup_window, text= "USER SIGNUP" ,font=("Microsoft Yahei UI Light",18,"bold") ,bg="#B2BEB5") #fg ="any color" can be used to change the text color
# Positioning the label
Header.place(x=390, y=140)

# Label for the second
email_label= Label(signup_window , text= "Email" , font=("Microsoft Yahei UI Light",10,"bold"), bg="#B2BEB5")
# Positioning the label
email_label.place(x=390, y=180)

email_entry = Entry(signup_window, width= 25, font=("Microsoft Yahei UI Light",9,"bold"), bd=0)
email_entry.insert(0,"Email")
email_entry.bind('<FocusIn>', on_pressed)
# Positioning the entry
email_entry.place(x=390, y=210)


#label for entring password
password_label= Label(signup_window, text="Password" , font=("Microsoft Yahei UI Light",10,"bold"), bg="#B2BEB5")
# Positioning the label
password_label.place(x=390,y=240)

# password entry label
password_entry = Entry(signup_window, width= 25, font=("Microsoft Yahei UI Light",9,"bold"), bd=0)
password_entry.insert(0,"Password")
password_entry.bind('<FocusIn>', on_push)

# Positioning the entry
password_entry.place(x=390, y=270)

password1_entry = Entry(signup_window, width= 25, font=("Microsoft Yahei UI Light",9,"bold"), bd=0)
password1_entry.insert(0,"Confirm password")
password1_entry.bind('<FocusIn>', on_pass)
# Positioning the entry
password1_entry.place(x=390, y=300)


#Sign up button

signup_button = Button(signup_window, text="SIGNUP" , font=("Microsoft Yahei UI Light",10,"bold"), bg="#B4BEB9" , bd=0, command=connect_database)

signup_button.place(x=390, y=330)

signup_window.mainloop()