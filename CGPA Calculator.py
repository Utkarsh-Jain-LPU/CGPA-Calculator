from tkinter import messagebox
from tkinter import *
import tkinter
import sqlite3

Home = tkinter.Tk()
Home.title("CGPA Calculator")
Home.geometry("500x600+525+125")


def check():
    data1 = Og.get()
    data2 = Oc.get()
    data3 = Tg.get()
    data4 = Tc.get()
    data5 = Thg.get()
    data6 = Thc.get()
    data7 = Fg.get()
    data8 = Fc.get()
    data9 = Fvg.get()
    data10 = Fvc.get()
    data11 = Sg.get()
    data12 = Sc.get()
    if data1 == "":
        messagebox.showwarning("Warning..!!", "Grade must not be Empty.")
    elif data2 == "":
        messagebox.showwarning("Warning..!!", "Credit must not be Empty.")
    elif data3 == "":
        messagebox.showwarning("Warning..!!", "Grade must not be Empty.")
    elif data4 == "":
        messagebox.showwarning("Warning..!!", "Credit must not be Empty.")
    elif data5 == "":
        messagebox.showwarning("Warning..!!", "Grade must not be Empty.")
    elif data6 == "":
        messagebox.showwarning("Warning..!!", "Credit must not be Empty.")
    elif data7 == "":
        messagebox.showwarning("Warning..!!", "Grade must not be Empty.")
    elif data8 == "":
        messagebox.showwarning("Warning..!!", "Credit must not be Empty.")
    elif data9 == "":
        messagebox.showwarning("Warning..!!", "Grade must not be Empty.")
    elif data10 == "":
        messagebox.showwarning("Warning..!!", "Credit must not be Empty.")
    elif data11 == "":
        messagebox.showwarning("Warning..!!", "Grade must not be Empty.")
    elif data12 == "":
        messagebox.showwarning("Warning..!!", "Credit must not be Empty.")
    else:
        a = int(data1)*int(data2)
        b = int(data3)*int(data4)
        c = int(data5)*int(data6)
        d = int(data7)*int(data8)
        e = int(data9)*int(data10)
        f = int(data11)*int(data12)
        marks = (a+b+c+d+e+f)
        credit = (int(data2)+int(data4)+int(data6)+int(data8)+int(data10)+int(data12))
        avg = marks/credit
        Cgpa.config(text=str(avg))
        con = sqlite3.connect("CGPA.db")
        c = con.cursor()
        c.execute("create table Marks(S1G int, S1C int, S2G int, S2C int, S3G int, S3C int, S4G int, S4C int, S5G int, S5C int, S6G int, S6C int, CGPA int)")
        c.execute("insert into Marks values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(int(data1),int(data2),int(data3),int(data4),int(data5),int(data6),int(data7),int(data8),int(data9),int(data10),int(data11),int(data12),avg))
        c.close()
        con.commit()
        

Label(Home, text="Calculate your CGPA", font="Helvetica 12 bold", height="3", width="500", bg="black", fg="white").pack()

Label(Home, text="Score", font="Helvetica 12 bold").place(x="200", y="120")
Label(Home, text="Credit", font="Helvetica 12 bold").place(x="345", y="120")

Label(Home, text="Subject 1 -", font="Helvetica 12 bold").place(x="65", y="160")
Og = Entry(Home, bd="3")
Og.place(x="165", y="160")
Oc = Entry(Home, bd="3")
Oc.place(x="310", y="160")

Label(Home, text="Subject 2 -", font="Helvetica 12 bold").place(x="65", y="190")
Tg = Entry(Home, bd="3")
Tg.place(x="165", y="190")
Tc = Entry(Home, bd="3")
Tc.place(x="310", y="190")

Label(Home, text="Subject 3 -", font="Helvetica 12 bold").place(x="65", y="220")
Thg = Entry(Home, bd="3")
Thg.place(x="165", y="220")
Thc = Entry(Home, bd="3")
Thc.place(x="310", y="220")

Label(Home, text="Subject 4 -", font="Helvetica 12 bold").place(x="65", y="250")
Fg = Entry(Home, bd="3")
Fg.place(x="165", y="250")
Fc = Entry(Home, bd="3")
Fc.place(x="310", y="250")

Label(Home, text="Subject 5 -", font="Helvetica 12 bold").place(x="65", y="280")
Fvg = Entry(Home, bd="3")
Fvg.place(x="165", y="280")
Fvc = Entry(Home, bd="3")
Fvc.place(x="310", y="280")

Label(Home, text="Subject 6 -", font="Helvetica 12 bold").place(x="65", y="310")
Sg = Entry(Home, bd="3")
Sg.place(x="165", y="310")
Sc = Entry(Home, bd="3")
Sc.place(x="310", y="310")

Label(Home, text="Enter TGPA =", font="Helvetica 12 bold").place(x="125", y="350")
Tgpa = Entry(Home, bd="3")
Tgpa.place(x="250", y="350")

Label(Home, text="Final CGPA  =", font="Helvetica 12 bold").place(x="170", y="400")
Cgpa = Label(Home, text="", font="Helvetica 12 bold", fg="green")
Cgpa.place(x="290", y="400")

Button(Home, text="Calculate CGPA", font="Helvetica 12 bold", bg="black", fg="white", command=check).place(x="190", y="460")

Label(Home, text="All fields are Compulsary...!!", font="Helvetica 12 bold", fg="red").place(x="155", y="500")

Home.mainloop()
