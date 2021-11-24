from tkinter import *

import tkinter.messagebox

from tkinter import Tk

def go():
 root.destroy()
 first()

root=Tk()
root.geometry("800x600")
root.minsize(500, 500)
root.maxsize(800, 600)
root.title("     ")

f1=Frame(root,bg="orange", width=800, height=600)
f1.place(x=0,y=0)
f2=Frame(root, bg="yellow", width=600, height=300)
f2.place(x=100, y=100)
l2=Label(f2, text="Let's Start", bg="black", fg="white", width=55, height=2, font=("bold", 15))
l2.place(x=0,y=0)
b1=Button(f2,text="continue",command=go,width=30,height=5)
b1.place(x=180,y=150)
def first():
    fir=Tk()
    fir.geometry("800x600")
    fir.minsize(500, 500)
    fir.maxsize(800, 600)
    fir.title("     ")


    def page1():
        fir.destroy()
        firstw()
    def stude():
        fir.destroy()
        stud1()


    l1 = Frame(fir, bg="gray",width=800,height=600)
    l1.place(x=0, y=0, anchor=NW)
    l = Label(fir, fg="aqua", bg="gray", text="WELCOME USER", font=('Helvetica bold', 30))
    l.place(anchor=N, relx=0.5, rely=0.1)



    l2 = Button(l1, text="Teacher", bg="white",fg="orange", command=page1,width=30)
    l2.place(y=200,x=170)



    l3 = Button(l1, text="Student",command=stude, bg="white",fg="orange",width=30)
    l3.place(y=200,x=400)


def firstw():
    firstw = Tk()
    firstw.title("login page")
    firstw.geometry("800x600")
    firstw.maxsize(600,800)
    firstw.minsize(800,600)
    def login():
        if user.get() == "1" and user3.get() == "1":
            firstw.destroy()
            second()
        else:
            t = tkinter.messagebox.showinfo("INVALID USERNAME OR PASSWORD ",
                                            "YOU HAVE ENTERED INVALID USERNAME OR PASSWORD  ")
            user.delete(0, END)
            user3.delete(0, END)
    label = Label(text="SCHOOL MANAGEMENT SYSTEM", font=("times new roman", 35), bg="black",
                  fg="white")
    label.pack(side=TOP, fill=X)
    user1 = Label(text="USERNAME", font=("arial", 23))
    user1.place(x=310, y=120)
    user = Entry(width=17, bd=5, font=("arial", 20))
    user.place(x=270, y=200)

    label.pack(side=TOP, fill=X)
    user2 = Label(text="PASSWORD", font=("arial", 23))
    user2.place(x=310, y=280)
    user3 = Entry(width=17, show="*", bd=5, font=("arial", 20))
    user3.place(x=270, y=360)
    b1=Button(firstw,bg="gray",command=login,text="LOGIN",fg="white",font=("arial",19))
    b1.place(x=280,y=430)

def second():
    sec=Tk()
    sec.geometry("800x600")
    sec.maxsize(600,800)
    sec.minsize(800,600)

    def dash():
        root = Tk()
        root.geometry("500x500")
        root.maxsize(500, 500)
        root.minsize(500, 500)
        f1 = Frame(root, bg="gray", width=500, height=500)
        f1.place(x=0, y=0)
        f2 = Frame(f1, bg="white", width=480, height=450)
        f2.place(x=10, y=20)

        global box
        global name
        global radio1
        global radio2
        name = StringVar()
        global sur
        sur = StringVar()
        global gander
        gander = IntVar()
        global var1
        var1 = IntVar()
        global var2
        var2 = IntVar()
        global branch
        branch = StringVar()
        global rollno
        rollno = StringVar()
        global email
        email = StringVar()
        global course
        course = StringVar()
        global python
        python = IntVar()
        global java
        java = IntVar()
        global c
        c = IntVar()
        global gender
        gender = IntVar()
        global d
        d = IntVar()
        global calculate
        calculate = StringVar()
        id = IntVar()
        search = IntVar()

        NAME = name.get()
        SUR = sur.get()
        EMAIL = email.get()
        BRANCH = branch.get()
        GANDER = gander.get()
        var = gender.get()
        PYTHON = python.get()
        JAVA = java.get()
        C = c.get()
        D = d.get()
        CALCULATE = calculate.get()
        calculation2 = 2000

        def submit():

            if entry1.get() == "" or entry2.get() == " " and entry3.get() == " " and gander == 3:
                root.destroy()
                t = tkinter.messagebox.showinfo(" INVALID DETAILS", "ENTER VALID AND EVERY DETAILS")




            else:
                file = open('Student Record.txt', 'a')
                file.write("{")
                file.write("\n")
                file.write('Name :' +entry1.get())
                file.write("\n")
                file.write('Surname :' + entry2.get())
                file.write("\n")
                file.write('Email :' + entry3.get())
                file.write("\n")
                file.write("}")
                file.write("\n")


                file.close()

                t = tkinter.messagebox.showinfo("updated", "updated")

                root.destroy()

        label = Label(root, text="REGISTRATION FORM", font=("arial", 12), bg="black", fg="white")
        label.place(x=140, y=20)

        label1 = Label(root, text="NAME:", font=("arial", 17))
        label1.place(x=10, y=50)

        label2 = Label(root, text="SURNAME:", font=("arial", 17))
        label2.place(x=10, y=90)

        label3 = Label(root, text="EMAIL:", font=("arial", 17))
        label3.place(x=10, y=130)

        label3 = Label(root, text="GENDER:", font=("arial", 17))
        label3.place(x=10, y=170)

        label4 = Label(root, text="CLASS:", font=("arial", 17))
        label4.place(x=10, y=210)

        b1 = Button(f2, text="submit", command=submit, relief=SUNKEN, fg="orange", bg="white")
        b1.place(x=100, y=400)

        # ==============================entryfield========================================

        entry1 = Entry(root, bd=5, width=20, textvar=name, font=("arial", 15))
        entry1.place(x=200, y=50)



        entry2 = Entry(root, bd=5, width=20, textvar=sur, font=("arial", 15))
        entry2.place(x=200, y=90)

        entry3 = Entry(root, bd=5, width=20, textvar=email, font=("arial", 15))
        entry3.place(x=200, y=130)



        radio1 = Radiobutton(root, text="MALE", variable=gander, value=1, font=("arial", 13))
        radio1.place(x=200, y=170)

        radio2 = Radiobutton(root, text="FEMALE", variable=gander, padx=20, value=0, font=("arial", 13))
        radio2.place(x=290, y=170)
        gander.set(3)

        radio1 = Radiobutton(root, text="9th", variable=gender, value=1, font=("arial", 10))
        radio1.place(x=200, y=210)
        radio1 = Radiobutton(root, text="10th", variable=gender, value=2, font=("arial", 10))
        radio1.place(x=240, y=210)
        radio1 = Radiobutton(root, text="11th", variable=gender, value=3, font=("arial", 10))
        radio1.place(x=290, y=210)
        radio1 = Radiobutton(root, text="12th", variable=gender, value=4, font=("arial", 10))
        radio1.place(x=340, y=210)
        gender.set(5)

        python.set(0)
        java.set(0)
        c.set(0)
        d.set(0)

    def set():
        se = Tk()
        se.geometry("700x300")
        se.maxsize(300, 300)
        se.minsize(700, 300)

        def updat():
            t = tkinter.messagebox.showinfo("", "updated....")
            se.destroy()

        f1 = Frame(se, width=700, height=170, bg="gray")
        f1.place(x=0, y=10, anchor="nw")
        l3 = Label(f1, text="Today's timetable", bg="black", fg="white", anchor="n")
        l3.place(x=0, y=0)
        l4 = Label(f1,
                   text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                   bg="gray")
        l4.place(x=0, y=18)
        l5 = Label(f1,
                   text="            Time                    |                        Class                     |",
                   font=("Arial", 13))
        l5.place(x=0, y=30)
        global user
        user=StringVar()

        user = Entry(se, width=7, bd=5, font=("arial", 10))
        user.place(x=0, y=100)
        user2 = Entry(se, width=7, bd=5, font=("arial", 10))
        user2.place(x=100, y=100)
        user3 = Entry(se, width=7, bd=5, font=("arial", 10))
        user3.place(x=200, y=100)
        user4 = Entry(se, width=7, bd=5, font=("arial", 10))
        user4.place(x=300, y=100)
        ll = Label(f1, text="Start time", bg="red", fg="black")
        ll.place(x=5, y=60)
        lll = Label(f1, text="End time", bg="red", fg="black")
        lll.place(x=100, y=60)
        sect = Label(f1, text="STANDARD", bg="red", fg="black")
        sect.place(x=200, y=60)
        secti = Label(f1, text="SECTION", bg="red", fg="black")
        secti.place(x=310, y=60)
        b2 = Button(se, text="Update", command=updat, relief=SUNKEN, bg="orange", fg="black")
        b2.place(x=300, y=150)
        b3 = Button(se, text="NEXT", relief=SUNKEN, bg="orange", fg="black")
        b3.place(x=360, y=150)

    def assign():
        se = Tk()
        se.geometry("700x300")
        se.maxsize(300, 300)
        se.minsize(700, 300)
        def assi():
            t= tkinter.messagebox.showinfo("", "assigned...")
            se.destroy()

        def next():
            t = tkinter.messagebox.showinfo("", "assigned...")




        f1 = Frame(se, width=700, height=170, bg="gray")
        f1.place(x=0, y=10, anchor="nw")
        l3 = Label(f1, text="Assignment", bg="black", fg="white", anchor="n", font=("arial", 12))
        l3.place(x=0, y=0)
        l4 = Label(f1,
                   text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                   bg="gray")
        l4.place(x=0, y=18)
        l5 = Label(f1,
                   text="            class                    |             assign   |    Last Date      |",
                   font=("Arial", 13))
        l5.place(x=0, y=30)

        ll = Label(f1, text="9th", bg="white", fg="black")
        ll.place(x=30, y=60)
        lll = Label(f1, text="10th", bg="white", fg="black")
        lll.place(x=30, y=95)
        llll = Label(f1, text="11th", bg="white", fg="black")
        llll.place(x=30, y=135)

        b2 = Button(se, text="Assign",command=assi, relief=SUNKEN, bg="orange", fg="black")
        b2.place(x=250, y=65)
        b3 = Button(se, text="Assign", relief=SUNKEN,command=assi, bg="orange", fg="black")
        b3.place(x=250, y=100)
        b3 = Button(se, text="Assign", relief=SUNKEN, bg="orange",command=assi, fg="black")
        b3.place(x=250, y=140)
        e1 = Entry(se, width=10, bd=5, font=("arial", 10))
        e1.place(x=350, y=70)
        e2 = Entry(se, width=10, bd=5, font=("arial", 10))
        e2.place(x=350, y=105)
        e3 = Entry(se, width=10, bd=5, font=("arial", 10))
        e3.place(x=350, y=140)

        b4 = Button(se, text="NEXT", command=next, relief=SUNKEN, bg="orange", fg="black")
        b4.place(x=460, y=70)
        b5 = Button(se, text="NEXT", command=next, relief=SUNKEN, bg="orange", fg="black")
        b5.place(x=460, y=100)
        b6 = Button(se, text="NEXT", command=next, relief=SUNKEN, bg="orange", fg="black")
        b6.place(x=460, y=140)

    def mess():
        t = tkinter.messagebox.showinfo("no new messages", "You have no new messages")
    def exi():
        sec.destroy()
        first()

    sec.geometry("800x600")
    sec.maxsize(600, 800)
    sec.minsize(800, 600)
    f1 = Frame(sec, bg="gray", width=800, height=800)
    f1.place(x=0, y=0)
    l1 = Label(f1, text="Hello sir what you wanna do....", fg="white", bg="orange", font=("times new roman", 20))
    l1.place(x=10, y=10)
    button = Button(f1, width=17, font=("arial", 13), text="SET TIMETABLE", command=set, bg="black", fg="white")
    button.place(x=100, y=250)
    enquiry = Button(f1, width=15, font=("arial", 13), text=" MESSAGE", command=mess, bg="black", fg="white")
    enquiry.place(x=270, y=250)
    exit = Button(f1, width=15, command=assign, font=("arial", 13), text="ASSIGNMENTS", bg="black", fg="white")
    exit.place(x=430, y=250)
    assignment = Button(f1, width=15,command=exi, font=("arial", 13), text="EXIT", bg="black", fg="white")
    assignment.place(x=580, y=250)
    Button(f1,text="Register student",command=dash,font=("arial",13),bg="black",fg="white").place(x=100,y=300)


def stud1():
    stu = Tk()
    stu.geometry("800x600")
    stu.maxsize(600, 800)
    stu.minsize(800, 600)

    def login():
        if entr.get() == "1" and ent.get() == "1":

            stu.destroy()
            stu2()

        else:
            t = tkinter.messagebox.showinfo("INVALID USERNAME OR PASSWORD ",
                                            "YOU HAVE ENTERED INVALID USERNAME OR PASSWORD  ")
            entr.delete(0, END)
            ent.delete(0, END)

    stu.title("Login Page")
    label = Label(text="SCHOOL MANAGEMENT SYSTEM", font=("times new roman", 35), bg="black",
                  fg="white")
    label.pack(side=TOP, fill=X)
    l1 = Label(text="USERNAME", font=("arial", 23))
    l1.place(x=310, y=120)
    entr = Entry(width=17, bd=5, font=("arial", 20))
    entr.place(x=270, y=200)
    label.pack(side=TOP, fill=X)
    l2 = Label(text="PASSWORD", font=("arial", 23))
    l2.place(x=310, y=280)
    ent = Entry(width=17, show="*", bd=5, font=("arial", 20))
    ent.place(x=270, y=360)
    bul1 = Button(stu, bg="gray", command=login, text="LOGIN", fg="white", font=("arial", 19))
    bul1.place(x=280, y=430)

def stu2():
    stud = Tk()
    stud.geometry("800x600")
    stud.maxsize(600, 800)
    stud.minsize(800, 600)

    def mess():
        t = tkinter.messagebox.showinfo("no new messages", "You have no new messages")
    def assi():
        t = tkinter.messagebox.showinfo("oops", "something goes wrong")

    def exi():
        stud.destroy()
        t=tkinter.messagebox.showinfo(" ", "Thanks for visiting.....")
        first()
    def feee():
        main = Tk()
        main.geometry("1600x1000+0+0")
        main.title("Enquiry")

        def check():
            z = IntVar()
            y = IntVar()
            u = IntVar()
            z = 20000

            if entry29.get() == " ":
                t = tkinter.messagebox.showinfo("OOPS ", "You haven't added money.....")
            elif entry29.get() > "20000":
                t = tkinter.messagebox.showinfo(" ","Enter the valid amount of fees")
            else:
                u = entry29.get()
                entry26.insert(0, z)
                entry27.insert(0, u)
                y = int(((entry26.get()))) - int(((entry27.get())))
                entry28.insert(0, y)

        def res():
            entry26.delete(0, END)
            entry27.delete(0, END)
            entry28.delete(0, END)
            entry29.delete(0, END)

        def distroy3():
            main.destroy()

        button = Button(main, text="BACK", width=30, bg="red", fg="black", command=distroy3)
        button.place(x=0, y=0)

        label3 = Label(main, text="ENTER AMOUNT", font=("arial", 17))
        label3.place(x=550, y=100)

        button23 = Button(main, command=check, text="ADD FEE", width=26, font=("arial", 10), bg="black", fg="white")
        button23.place(x=550, y=310)
        entry29 = Entry(main, bd=5, width=20, font=("arial", 15))
        entry29.place(x=550, y=200)
        button28 = Button(main, command=res, text="RESET", width=26, font=("arial", 10), bg="red", fg="black")
        button28.place(x=1150, y=0)

        label31 = Label(main, text="TOTEL FEE", font=("arial", 17))
        label31.place(x=900, y=550)
        label32 = Label(main, text="PAID FEE", font=("arial", 17))
        label32.place(x=600, y=550)
        label33 = Label(main, text="REMAIN FEE", font=("arial", 17))
        label33.place(x=300, y=550)

        entry26 = Entry(main, bd=5, width=20, font=("arial", 15))
        entry26.place(x=900, y=600)
        entry27 = Entry(main, bd=5, width=20, font=("arial", 15))
        entry27.place(x=600, y=600)
        entry28 = Entry(main, bd=5, width=20, font=("arial", 15))
        entry28.place(x=300, y=600)

    def syllabus():
        syl = Tk()
        syl.geometry("500x500")
        syl.maxsize(500, 500)
        syl.minsize(500, 500)

        def p():
            top = Tk()
            top.title("Physics Syllabus")
            top.geometry("300x300")
            top.maxsize(300, 300)
            top.minsize(300, 300)

            def pre():
                top.destroy()
                syllabus()

            mb = Menubutton(top, text="CHAPTER 1", relief=SUNKEN)
            mb.place(x=10, y=20)
            mb.menu = Menu(mb)
            mb["menu"] = mb.menu
            mb.menu.add_checkbutton(label="chapter name:measurment")
            mb.menu.add_checkbutton(label="topic:SI,CGS UNIT")
            mb2 = Menubutton(top, text="CHAPTER 2", relief=SUNKEN)
            mb2.place(x=90, y=20)
            mb2.menu = Menu(mb2)
            mb2["menu"] = mb2.menu
            mb2.menu.add_checkbutton(label="chapter name:Light")
            mb2.menu.add_checkbutton(label="topic:Reflection\nRefraction")
            mb3 = Menubutton(top, text="CHAPTER 3", relief=SUNKEN)
            mb3.place(x=170, y=20)
            mb3.menu = Menu(mb3)
            mb3["menu"] = mb3.menu
            mb3.menu.add_checkbutton(label="chapter name:Motion")
            mb3.menu.add_checkbutton(label="topic:Distance\nDisplacement")
            mb4 = Menubutton(top, text="CHAPTER 4", relief=SUNKEN)
            mb4.place(x=40, y=50)
            mb4.menu = Menu(mb4)
            mb4["menu"] = mb4.menu
            mb4.menu.add_checkbutton(label="chapter name:Force")
            mb4.menu.add_checkbutton(label="topic:Newton's law of motion ")
            mb5 = Menubutton(top, text="CHAPTER 5", relief=SUNKEN)
            mb5.place(x=130, y=50)
            mb5.menu = Menu(mb5)
            mb5["menu"] = mb5.menu
            mb5.menu.add_checkbutton(label="chapter name:Gravitation")
            mb5.menu.add_checkbutton(label="topic:Universal law of attraction ")
            mb6 = Menubutton(top, text="CHAPTER 6", relief=SUNKEN)
            mb6.place(x=10, y=90)
            mb6.menu = Menu(mb6)
            mb6["menu"] = mb6.menu
            mb6.menu.add_checkbutton(label="chapter name:Sound")
            mb6.menu.add_checkbutton(label="topic:structure of ear")
            b1 = Button(top, text="PREVIOUS", command=pre, relief=SUNKEN, bg="brown", fg="white")
            b1.place(x=100, y=170)

        def c():
            top = Tk()
            top.title("Chemistry Syllabus")
            top.geometry("300x300")
            top.maxsize(300, 300)
            top.minsize(300, 300)

            def pre():
                top.destroy()
            mb = Menubutton(top, text="CHAPTER 1", relief=SUNKEN)
            mb.place(x=10, y=20)
            mb.menu = Menu(mb)
            mb["menu"] = mb.menu
            mb.menu.add_checkbutton(label="chapter name:Atom and molecules")
            mb.menu.add_checkbutton(label="topic:Basic of")
            mb2 = Menubutton(top, text="CHAPTER 2", relief=SUNKEN)
            mb2.place(x=90, y=20)
            mb2.menu = Menu(mb2)
            mb2["menu"] = mb2.menu
            mb2.menu.add_checkbutton(label="chapter name:Chemical Equation")
            mb2.menu.add_checkbutton(label="topic:Exothermic,Endothermic")
            mb3 = Menubutton(top, text="CHAPTER 3", relief=SUNKEN)
            mb3.place(x=170, y=20)
            mb3.menu = Menu(mb3)
            mb3["menu"] = mb3.menu
            mb3.menu.add_checkbutton(label="chapter name:Motion")
            mb3.menu.add_checkbutton(label="topic:Distance\nDisplacement")
            mb4 = Menubutton(top, text="CHAPTER 4", relief=SUNKEN)
            mb4.place(x=40, y=50)
            mb4.menu = Menu(mb4)
            mb4["menu"] = mb4.menu
            mb4.menu.add_checkbutton(label="chapter name:Force")
            mb4.menu.add_checkbutton(label="topic:Newton's law of motion ")
            mb5 = Menubutton(top, text="CHAPTER 5", relief=SUNKEN)
            mb5.place(x=130, y=50)
            mb5.menu = Menu(mb5)
            mb5["menu"] = mb5.menu
            mb5.menu.add_checkbutton(label="chapter name:Gravitation")
            mb5.menu.add_checkbutton(label="topic:Universal law of attraction ")
            mb6 = Menubutton(top, text="CHAPTER 6", relief=SUNKEN)
            mb6.place(x=10, y=90)
            mb6.menu = Menu(mb6)
            mb6["menu"] = mb6.menu
            mb6.menu.add_checkbutton(label="chapter name:Sound")
            mb6.menu.add_checkbutton(label="topic:structure of ear")
            b1 = Button(top, text="PREVIOUS", command=pre, relief=SUNKEN, bg="brown", fg="white")
            b1.place(x=100, y=170)
        def m():
            top = Tk()
            top.title("Math Syllabus")
            top.geometry("300x300")
            top.maxsize(300, 300)
            top.minsize(300, 300)

            def pre():
                top.destroy()


            mb = Menubutton(top, text="CHAPTER 1", relief=SUNKEN)
            mb.place(x=10, y=20)
            mb.menu = Menu(mb)
            mb["menu"] = mb.menu
            mb.menu.add_checkbutton(label="chapter name:Real numbers")
            mb.menu.add_checkbutton(label="topic:Rational,Irrational")
            mb2 = Menubutton(top, text="CHAPTER 2", relief=SUNKEN)
            mb2.place(x=90, y=20)
            mb2.menu = Menu(mb2)
            mb2["menu"] = mb2.menu
            mb2.menu.add_checkbutton(label="chapter name:Polynomial")
            mb2.menu.add_checkbutton(label="topic:Factorial")
            mb3 = Menubutton(top, text="CHAPTER 3", relief=SUNKEN)
            mb3.place(x=170, y=20)
            mb3.menu = Menu(mb3)
            mb3["menu"] = mb3.menu
            mb3.menu.add_checkbutton(label="chapter name:Trignometry")
            mb3.menu.add_checkbutton(label="topic:Basic of trignometry")
            mb4 = Menubutton(top, text="CHAPTER 4", relief=SUNKEN)
            mb4.place(x=40, y=50)
            mb4.menu = Menu(mb4)
            mb4["menu"] = mb4.menu
            mb4.menu.add_checkbutton(label="chapter name:Triangle")
            mb4.menu.add_checkbutton(label="topic:Types of triangle,Law of triangle")
            mb5 = Menubutton(top, text="CHAPTER 5", relief=SUNKEN)
            mb5.place(x=130, y=50)
            mb5.menu = Menu(mb5)
            mb5["menu"] = mb5.menu
            mb5.menu.add_checkbutton(label="chapter name:Measurment")
            mb5.menu.add_checkbutton(label="topic:Area,Perimeter")
            mb6 = Menubutton(top, text="CHAPTER 6", relief=SUNKEN)
            mb6.place(x=10, y=90)
            mb6.menu = Menu(mb6)
            mb6["menu"] = mb6.menu
            mb6.menu.add_checkbutton(label="chapter name:Sound")
            mb6.menu.add_checkbutton(label="topic:structure of ear")
            b1 = Button(top, text="PREVIOUS", command=pre, relief=SUNKEN, bg="brown", fg="white")
            b1.place(x=100, y=170)
        def b():
            top = Tk()
            top.title("Biology Syllabus")
            top.geometry("300x300")
            top.maxsize(300, 300)
            top.minsize(300, 300)

            def pre():
                top.destroy()

            mb = Menubutton(top, text="CHAPTER 1", relief=SUNKEN)
            mb.place(x=10, y=20)
            mb.menu = Menu(mb)
            mb["menu"] = mb.menu
            mb.menu.add_checkbutton(label="chapter name:Real numbers")
            mb.menu.add_checkbutton(label="topic:Rational,Irrational")
            mb2 = Menubutton(top, text="CHAPTER 2", relief=SUNKEN)
            mb2.place(x=90, y=20)
            mb2.menu = Menu(mb2)
            mb2["menu"] = mb2.menu
            mb2.menu.add_checkbutton(label="chapter name:Polynomial")
            mb2.menu.add_checkbutton(label="topic:Factorial")
            mb3 = Menubutton(top, text="CHAPTER 3", relief=SUNKEN)
            mb3.place(x=170, y=20)
            mb3.menu = Menu(mb3)
            mb3["menu"] = mb3.menu
            mb3.menu.add_checkbutton(label="chapter name:Trignometry")
            mb3.menu.add_checkbutton(label="topic:Basic of trignometry")
            mb4 = Menubutton(top, text="CHAPTER 4", relief=SUNKEN)
            mb4.place(x=40, y=50)
            mb4.menu = Menu(mb4)
            mb4["menu"] = mb4.menu
            mb4.menu.add_checkbutton(label="chapter name:Triangle")
            mb4.menu.add_checkbutton(label="topic:Types of triangle,Law of triangle")
            mb5 = Menubutton(top, text="CHAPTER 5", relief=SUNKEN)
            mb5.place(x=130, y=50)
            mb5.menu = Menu(mb5)
            mb5["menu"] = mb5.menu
            mb5.menu.add_checkbutton(label="chapter name:Measurment")
            mb5.menu.add_checkbutton(label="topic:Area,Perimeter")
            mb6 = Menubutton(top, text="CHAPTER 6", relief=SUNKEN)
            mb6.place(x=10, y=90)
            mb6.menu = Menu(mb6)
            mb6["menu"] = mb6.menu
            mb6.menu.add_checkbutton(label="chapter name:Sound")
            mb6.menu.add_checkbutton(label="topic:structure of ear")
            b1 = Button(top, text="PREVIOUS", command=pre, relief=SUNKEN, bg="brown", fg="white")
            b1.place(x=100, y=170)
        def e():
            top = Tk()
            top.title("English Syllabus")
            top.geometry("300x300")
            top.maxsize(300, 300)
            top.minsize(300, 300)

            def pre():
                top.destroy()
                syllabus()

            mb = Menubutton(top, text="CHAPTER 1", relief=SUNKEN)
            mb.place(x=10, y=20)
            mb.menu = Menu(mb)
            mb["menu"] = mb.menu
            mb.menu.add_checkbutton(label="chapter name:Real numbers")
            mb.menu.add_checkbutton(label="topic:Rational,Irrational")
            mb2 = Menubutton(top, text="CHAPTER 2", relief=SUNKEN)
            mb2.place(x=90, y=20)
            mb2.menu = Menu(mb2)
            mb2["menu"] = mb2.menu
            mb2.menu.add_checkbutton(label="chapter name:Polynomial")
            mb2.menu.add_checkbutton(label="topic:Factorial")
            mb3 = Menubutton(top, text="CHAPTER 3", relief=SUNKEN)
            mb3.place(x=170, y=20)
            mb3.menu = Menu(mb3)
            mb3["menu"] = mb3.menu
            mb3.menu.add_checkbutton(label="chapter name:Trignometry")
            mb3.menu.add_checkbutton(label="topic:Basic of trignometry")
            mb4 = Menubutton(top, text="CHAPTER 4", relief=SUNKEN)
            mb4.place(x=40, y=50)
            mb4.menu = Menu(mb4)
            mb4["menu"] = mb4.menu
            mb4.menu.add_checkbutton(label="chapter name:Triangle")
            mb4.menu.add_checkbutton(label="topic:Types of triangle,Law of triangle")
            mb5 = Menubutton(top, text="CHAPTER 5", relief=SUNKEN)
            mb5.place(x=130, y=50)
            mb5.menu = Menu(mb5)
            mb5["menu"] = mb5.menu
            mb5.menu.add_checkbutton(label="chapter name:Measurment")
            mb5.menu.add_checkbutton(label="topic:Area,Perimeter")
            mb6 = Menubutton(top, text="CHAPTER 6", relief=SUNKEN)
            mb6.place(x=10, y=90)
            mb6.menu = Menu(mb6)
            mb6["menu"] = mb6.menu
            mb6.menu.add_checkbutton(label="chapter name:Sound")
            mb6.menu.add_checkbutton(label="topic:structure of ear")
            b1 = Button(top, text="PREVIOUS", command=pre, relief=SUNKEN, bg="brown", fg="white")
            b1.place(x=100, y=170)
        def h():
            t=tkinter.messagebox.showinfo("OOPS ", "something goes wrong.....")



        f1 = Frame(syl, bg="gray", width=500, height=500)
        f1.place(x=0, y=0)
        l1 = Label(f1, text="CHOOSE THE SUBJECT", fg="white", bg="black", font=("helvetica Bold", 17))
        l1.place(x=100, y=20)

        phy = Button(f1, width=10, font=("arial", 13), command=p, text="PHYSICS", bg="black",
                     fg="white")
        phy.place(x=20, y=150)
        chem = Button(f1, width=10, font=("arial", 13), command=c, text="CHEMISTRY", bg="black", fg="white")
        chem.place(x=140, y=150)
        bio = Button(f1, width=10, font=("arial", 13),command=b, text="BIOLOGY", bg="black", fg="white")
        bio.place(x=250, y=150)
        ma = Button(f1, width=10, font=("arial", 13),command=m, text="MATH", bg="black", fg="white")
        ma.place(x=360, y=150)
        eng = Button(f1, width=10, font=("arial", 13),command=e, text="ENGLISH", bg="black", fg="white")
        eng.place(x=70, y=200)
        hin = Button(f1, width=10, font=("arial", 13),command=h,text="HINDI", bg="black", fg="white")
        hin.place(x=190, y=200)
        soc = Button(f1, width=15, font=("arial", 13),command=h, text="SOCIAL SCIENCE", bg="black", fg="white")
        soc.place(x=310, y=200)








    f1 = Frame(stud, bg="gray", width=800, height=800)
    f1.place(x=0, y=0)
    l1 = Label(f1, text="Hello user what you wanna see....", fg="white", bg="orange", font=("times new roman", 20))
    l1.place(x=10, y=10)

    enquiry = Button(f1, width=15, font=("arial", 13),command=mess, text=" MESSAGE", bg="black", fg="white")
    enquiry.place(x=270, y=250)
    assign = Button(f1, width=15,command=assi, font=("arial", 13), text="ASSIGNMENTS", bg="black", fg="white")
    assign.place(x=430, y=250)
    fee = Button(f1, width=15,command=feee, font=("arial", 13), text="Fee Enquiry", bg="black", fg="white")
    fee.place(x=580, y=250)
    sylabus = Button(f1, width=15, font=("arial", 13),command=syllabus, text="Syllabus", bg="black", fg="white")
    sylabus.place(x=100, y=300)
    exit = Button(f1, width=15, font=("arial", 13),command=exi, text="Exit", bg="black", fg="white")
    exit.place(x=270, y=300)



root.mainloop()
