import tkinter as tk
from tkinter import *
import mysql.connector


window = Tk()

# WINDOW TITLE

window.title("Address Form")
window.geometry("1000x2000")

# WIDGET CREATION

text = Label(window, text=" Enter the required field given below and fetch the details of the data", font=("verdana",
                                                                                                           20))
text.place(x=20, y=450)

label_collection = Label(window, text='ENTER YOUR AADHAR NO :', font=('bold', 15))
label_collection.place(x=30, y=550)
entry_12 = Entry(width=50)
entry_12.place(x=350, y=550)

# FUNCTION TO FETCH THE DETAILS


def details():
    mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password='12345',
            auth_plugin="mysql_native_password"
        )
    my_cursor = mydb.cursor()
    my_cursor.execute("USE hello")
    my_cursor.execute("SELECT * FROM Storage_data2 where aadhar_no='"+entry_12.get()+"'")

    i = 0
    for student in my_cursor:
        for j in range(len(student)):
            e = Entry(window, width=20, fg='blue', justify="center", borderwidth=1, relief="solid")
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i+1


# BUTTON TO FETCH THE DETAILS

button_insert = tk.Button(window, text="Fetch", font=('verdana', 14), command=details)

button_insert.place(x=350, y=600)


window.mainloop()

