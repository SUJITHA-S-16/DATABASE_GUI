import tkinter as tk
from tkinter import *
import mysql.connector
import tkinter.messagebox as messagebox

# WINDOW CREATION

window = Tk()

# WINDOW TITLE

window.title("Address Form")
window.geometry("1000x1000")


# CREATING WIDGETS

heading = Label(window, text="FILL THE FORM GIVEN BELOW", font=("bold", 20))
heading.place(x=20, y=10)

first_name = Label(window, text="FIRST NAME", font=("bold", 10))
first_name.place(x=30, y=80)
entry_1 = Entry(width=50)
entry_1.place(x=200, y=80)

last_name = Label(window, text="LAST NAME", font=("bold", 10))
last_name.place(x=30, y=120)
entry_2 = Entry(width=50)
entry_2.place(x=200, y=120)

door_no = Label(window, text="DOOR NO", font=("bold", 10))
door_no.place(x=30, y=160)
entry_3 = Entry(width=50)
entry_3.place(x=200, y=160)

street_name = Label(window, text="STREET NAME", font=("bold", 10))
street_name.place(x=30, y=200)
entry_4 = Entry(width=50)
entry_4.place(x=200, y=200)

city = Label(window, text="CITY", font=("bold", 10))
city.place(x=30, y=240)
entry_5 = Entry(width=50)
entry_5.place(x=200, y=240)

district = Label(window, text="DISTRICT", font=("bold", 10))
district.place(x=30, y=280)
entry_6 = Entry(width=50)
entry_6.place(x=200, y=280)

pincode = Label(window, text="PINCODE", font=("bold", 10))
pincode.place(x=30, y=320)
entry_7 = Entry(width=50)
entry_7.place(x=200, y=320)

email = Label(window, text="EMAIL ID", font=("bold", 10))
email.place(x=30, y=360)
entry_8 = Entry(width=50)
entry_8.place(x=200, y=360)

aadhar_no = Label(window, text="AADHAR NO", font=("bold", 10))
aadhar_no.place(x=30, y=400)
entry_9 = Entry(width=50)
entry_9.place(x=200, y=400)

educational_details = Label(window, text="EDUCATIONAL DETAILS", font=("bold", 10))
educational_details.place(x=30, y=440)
entry_10 = Entry(width=50)
entry_10.place(x=200, y=440)

identification = Label(window, text="IDENTIFICATION", font=("bold", 10))
identification.place(x=30, y=480)
entry_11 = Entry(width=50)
entry_11.place(x=200, y=480)

# FUNCTION TO GET DETAILS


def data():
    first_name1 = entry_1.get()
    last_name1 = entry_2.get()
    door_no1 = entry_3.get()
    street_name1 = entry_4.get()
    city1 = entry_5.get()
    district1 = entry_6.get()
    pincode1 = entry_7.get()
    email1 = entry_8.get()
    aadhar_no1 = entry_9.get()
    educational_details1 = entry_10.get()
    identification1 = entry_11.get()

    # GIVING CONDITIONS TO FULL ALL THE FIELDS

    if(first_name1 == "" or last_name1 == "" or door_no1 == "" or street_name1 == "" or city1 == "" or district1 == ""
            or pincode1 == "" or email1 == "" or aadhar_no1 == "" or educational_details1 == "" or
            identification1 == ""):
        # MESSAGE BOX TO SHOW THE ERROR

        messagebox.showerror("Insert Status", "All fields are Mandatory")

    else:

        # SQL CONNECTION

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password='12345',
            auth_plugin="mysql_native_password"
            )
        my_cursor = mydb.cursor()
        my_cursor.execute("USE hello")

        # TABLE CREATION

        table = "CREATE TABLE if not exists Storage_data2(first_name varchar(250),last_name varchar(250),door_no int," \
                "street_name varchar(250),city varchar(100),district varchar(150),pincode int,email_id varchar(250)," \
                "aadhar_no varchar(12),educational_details varchar(250),identification varchar(350))"
        my_cursor.execute(table)

        # INSERTING DATA INTO THE TABLE

        query = "INSERT INTO hello.Storage_data2(first_name,last_name,door_no,street_name,city,district,pincode," \
                "email_id,aadhar_no,educational_details,identification)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (first_name1, last_name1, door_no1, street_name1, city1, district1, pincode1, email1, aadhar_no1,
                  educational_details1, identification1)
        my_cursor.execute(query, values)

        mydb.commit()

        # DELETING ALL THE INPUTS AFTER INSERTING INTO THE DATABASE

        entry_1.delete(0, "end")
        entry_2.delete(0, "end")
        entry_3.delete(0, "end")
        entry_4.delete(0, "end")
        entry_5.delete(0, "end")
        entry_6.delete(0, "end")
        entry_7.delete(0, "end")
        entry_8.delete(0, "end")
        entry_9.delete(0, "end")
        entry_10.delete(0, "end")
        entry_11.delete(0, "end")

        # MESSAGE BOX TO SHOW THE STATUS

        messagebox.showinfo("Insert Status", "Inserted Successfully")

# BUTTON CREATION TO INSERT DATA INTO SQL


button_insert = tk.Button(window, text="Insert", font=('verdana', 14), command=data)

button_insert.place(x=150, y=550)

window.mainloop()
