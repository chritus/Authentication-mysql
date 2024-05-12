from tkinter import *


# The function to the button when pressed

def convert():
    try:
        value = float(box1.get())
        List1 = from_unit_var.get()
        List2 = to_unit_var.get()

        if List1 == "Metre" and List2 == "Kilometre":
            result = value * 1000
        elif List1 == "Metre" and List2 == "Centimetre":
            result = value * 100
        elif List1 == "Centimetre" and List2 == "Metre":
            result = value / 100
        elif List1 == "Kilometre" and List2 == "Miles":
            result = value * 0.621371
        elif List1 == "Miles" and List2 == "Meter":
            result = value / 1609.34
        elif List1 == "Miles" and List2 == "Centimetre":
            result = value * 160934
        else:
            result = value
        
        result_label.config(text=f"Result: {result:.2f} {List2}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")


# Below is the basic UI for the app

root = Tk()
root.title("Unit Convertor")

# This will hold the first text 
mylabel = Label(root, text="Enter unit here : ")
mylabel.grid(column=0 , row= 0)

# Box to recieve input
box1 = Entry(root , width= 20)
box1.grid(column=1 , row= 0)
box1.get()

#This holds the second text and the "from" labels
mylabel2 = Label(root , text= "From") 
mylabel2.grid(row=1, column=0, padx=5, pady=5)
from_unit_var = StringVar()
List1_label = OptionMenu(root, from_unit_var, "Metre", "Miles", "Centimetre", "Kilometre")
List1_label.grid(row=1, column=1, padx=5, pady=5)

# The "to" labels 
mylabel3 = Label(root , text= " To") 
mylabel3.grid(row=2, column=0, padx=5, pady=5)
to_unit_var = StringVar()
List2_label = OptionMenu(root, to_unit_var, "Metre", "Miles", "Centimetre", "Kilometre")
List2_label.grid(row=2, column=1, padx=5, pady=5)
# Conversions
button1 = Button(root , text="Convert" , command=convert)
button1.grid(row=3, columnspan=2, padx=5, pady=5 )

result_label = Label(root, text="")
result_label.grid(row=4, columnspan=2, padx=5, pady=5)




# Keeps the window open
root.mainloop()

