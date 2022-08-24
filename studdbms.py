from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

class StudentDB:

    def __init__(self):
        self.conn = sqlite3.connect("stud.db")
        self.cursor = self.conn.cursor()
        self.tree = None
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
            "STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ROLLNO TEXT, STU_BRANCH TEXT)")
        self.name = None
        self.SEARCH = None
        self.contact = None
        self.email = None
        self.rollno = None
        self.branch = None

    def openDB(self):
        self.conn = sqlite3.connect("stud.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
            "STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ROLLNO TEXT, STU_BRANCH TEXT)")

    def DisplayForm(self):
        display_screen = Tk()
        display_screen.geometry("900x400")
        display_screen.title("krazyprogrammer.com presents")
        # global tree
        # global SEARCH
        # global name, contact, email, rollno, branch
        self.SEARCH = StringVar()
        self.name = StringVar()
        self.contact = StringVar()
        self.email = StringVar()
        self.rollno = StringVar()
        self.branch = StringVar()

        TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
        TopViewForm.pack(side=TOP, fill=X)

        LFrom = Frame(display_screen, width="350")
        LFrom.pack(side=LEFT, fill=Y)

        LeftViewForm = Frame(display_screen, width=500, bg="gray")
        LeftViewForm.pack(side=LEFT, fill=Y)

        MidViewForm = Frame(display_screen, width=600)
        MidViewForm.pack(side=RIGHT)

        lbl_text = Label(TopViewForm, text="Student Management System", font=('verdana', 18), width=600, bg="#1C2833",
                         fg="white")
        lbl_text.pack(fill=X)

        Label(LFrom, text="Name  ", font=("Arial", 12)).pack(side=TOP)
        Entry(LFrom, font=("Arial", 10, "bold"), textvariable=self.name).pack(side=TOP, padx=10, fill=X)
        Label(LFrom, text="Contact ", font=("Arial", 12)).pack(side=TOP)
        Entry(LFrom, font=("Arial", 10, "bold"), textvariable=self.contact).pack(side=TOP, padx=10, fill=X)
        Label(LFrom, text="Email ", font=("Arial", 12)).pack(side=TOP)
        Entry(LFrom, font=("Arial", 10, "bold"), textvariable=self.email).pack(side=TOP, padx=10, fill=X)
        Label(LFrom, text="Rollno ", font=("Arial", 12)).pack(side=TOP)
        Entry(LFrom, font=("Arial", 10, "bold"), textvariable=self.rollno).pack(side=TOP, padx=10, fill=X)
        Label(LFrom, text="Branch ", font=("Arial", 12)).pack(side=TOP)
        Entry(LFrom, font=("Arial", 10, "bold"), textvariable=self.branch).pack(side=TOP, padx=10, fill=X)
        Button(LFrom, text="Submit", font=("Arial", 10, "bold"), command=self.register).pack(side=TOP, padx=10, pady=5,
                                                                                        fill=X)

        # creating search label and entry in second frame
        lbl_txtsearch = Label(LeftViewForm, text="Enter name to Search", font=('verdana', 10), bg="gray")
        lbl_txtsearch.pack()

        search = Entry(LeftViewForm, textvariable=self.SEARCH, font=('verdana', 15), width=10)
        search.pack(side=TOP, padx=10, fill=X)

        btn_search = Button(LeftViewForm, text="Search", command=self.SearchRecord)
        btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

        btn_view = Button(LeftViewForm, text="View All", command=self.DisplayData)
        btn_view.pack(side=TOP, padx=10, pady=10, fill=X)

        btn_reset = Button(LeftViewForm, text="Reset", command=self.Reset)
        btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)

        btn_delete = Button(LeftViewForm, text="Delete", command=self.Delete)
        btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        self.tree = ttk.Treeview(MidViewForm, columns=("Student Id", "Name", "Contact", "Email", "Rollno", "Branch"),
                            selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        self.tree.heading('Student Id', text="Student Id", anchor=W)
        self.tree.heading('Name', text="Name", anchor=W)
        self.tree.heading('Contact', text="Contact", anchor=W)
        self.tree.heading('Email', text="Email", anchor=W)
        self.tree.heading('Rollno', text="Rollno", anchor=W)
        self.tree.heading('Branch', text="Branch", anchor=W)

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)
        self.tree.column('#4', stretch=NO, minwidth=0, width=120)
        self.tree.pack()
        self.DisplayData()

    def register(self):
        self.openDB()
        name1 = self.name.get()
        con1 = self.contact.get()
        email1 = self.email.get()
        rol1 = self.rollno.get()
        branch1 = self.branch.get()

        if name1 == '' or con1 == '' or email1 == '' or rol1 == '' or branch1 == '':
            tkMessageBox.showinfo("Warning", "fill the empty field!!!")
        else:

            self.conn.execute('INSERT INTO STUD_REGISTRATION (STU_NAME,STU_CONTACT,STU_EMAIL,STU_ROLLNO,STU_BRANCH) \
                  VALUES (?,?,?,?,?)', (name1, con1, email1, rol1, branch1));
            self.conn.commit()
            tkMessageBox.showinfo("Message", "Stored successfully")

            self.DisplayData()
            self.conn.close()

    def Reset(self):
        self.openDB()
        self.tree.delete(*self.tree.get_children())
        # refresh table data
        self.DisplayData()

        self.SEARCH.set("")
        self.name.set("")
        self.contact.set("")
        self.email.set("")
        self.rollno.set("")
        self.branch.set("")

    def Delete(self):
        self.openDB()
        if not self.tree.selection():
            tkMessageBox.showwarning("Warning", "Select data to delete")
        else:
            result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                              icon="warning")
            if result == 'yes':
                curItem = self.tree.focus()
                contents = (self.tree.item(curItem))
                selecteditem = contents['values']
                self.tree.delete(curItem)
                cursor = self.conn.execute("DELETE FROM STUD_REGISTRATION WHERE STU_ID = %d" % selecteditem[0])
                self.conn.commit()
                cursor.close()
                self.conn.close()

    def SearchRecord(self):
        self.openDB()
        if self.SEARCH.get() != "":
            self.tree.delete(*self.tree.get_children())

            cursor = self.conn.execute("SELECT * FROM STUD_REGISTRATION WHERE STU_NAME LIKE ?",
                                  ('%' + str(self.SEARCH.get()) + '%',))

            fetch = cursor.fetchall()

            for data in fetch:
                self.tree.insert('', 'end', values=(data))
            cursor.close()
            self.conn.close()

    def DisplayData(self):
        self.openDB()
        self.tree.delete(*self.tree.get_children())

        cursor = self.conn.execute("SELECT * FROM STUD_REGISTRATION")

        fetch = cursor.fetchall()

        for data in fetch:
            self.tree.insert('', 'end', values=(data))
        cursor.close()
        self.conn.close()


studDB = StudentDB()
studDB.DisplayForm()
mainloop()