# import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
import datetime
from tkinter import Listbox
from tkinter import messagebox
import tkinter

import mysql.connector


# User defined Erros
class BaseError(Exception):
    pass


class InputError(BaseError):
    def __init__(self, msg):
        self.msg = msg


class DatabaseError(BaseError):
    def __init__(self, msg):
        self.msg = msg


class LibraryManagementSystem:
    def __init__(self, root):
        # --------------------------------------------Heading Frame---------------------------------------------------------------

        self.root = root

        # For title of the window
        self.root.title("Library Management System")

        # for dimentions of the window like 150x250
        self.root.geometry("1550x850+0+0")

        # -------------------------variables for getting the input value from the text--------------------------------
        self.member_type_var = StringVar()
        self.member_id_var = StringVar()
        self.title_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.mobile_number_var = StringVar()
        self.address_var = StringVar()
        self.book_name_var = StringVar()
        self.book_author_var = StringVar()
        self.book_id_var = StringVar()
        self.issue_date_var = StringVar()
        self.due_date_var = StringVar()
        self.late_fine_var = StringVar()
        self.book_price_var = StringVar()
        self.search_var = StringVar()

        # to style the label
        label_title = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="#000", fg="#ff793f", bd=3,
                            relief=RIDGE, font=("Google Sans", 35,'bold'), padx=2, pady=6)

        # pack method is used to place the label
        # side top means at the top
        # fill X means dilling the X entirely
        label_title.pack(side=TOP, fill=X)

        # --------------------------------------------Detail Frame---------------------------------------------------------------

        # frame is similar to div in HTML like a container
        # bd is border
        # relief is for 3d effect to the box
        frame = Frame(self.root, bd=6, relief=RIDGE, padx=20, bg="#000")

        # width and height to define width and height of the area below the label
        # x and y are the co-ordinates to start with
        frame.place(x=0, y=70, width=1530, height=400)

        # --------------------------------------------DataFrame Left---------------------------------------------------------------

        # to have frame inside frame we use LabelFrame
        # Rest are the features we provide to it.
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="#000", fg="#ff793f", bd=4,
                                   relief=RIDGE, font=("Helvetica", 25,'italic'))
        # for placing the frame with co-ordinates as given
        DataFrameLeft.place(x=0, y=5, width=860, height=350)

        # ---------------Member dropbox--------------------

        # labels for the member details
        label_member = Label(DataFrameLeft, text="Member Type : ", font=("Helvetica", 10,'bold'), padx=5, pady=5,
                             bg='#000',fg='#ff793f')
        label_member.grid(row=0, column=0, sticky=W)

        # A combobox is like a combination of an Entry widget and a Listbox widget. A combobox allows you to select one value in a list of values. In addition, it allows you to enter a custom value.
        comb_member = ttk.Combobox(DataFrameLeft, font=('Google Sans', 10, 'bold'), textvariable=self.member_type_var,
                                   width=27, state="readonly")
        comb_member["value"] = ("Admin", 'Student', 'Teacher')
        comb_member.grid(row=0, column=1)

        # ---------------Id Number--------------------

        # labels for the ID Number details
        label_ID = Label(DataFrameLeft, text="ID Number : ", font=("Helvetica", 10,'bold'), padx=5, pady=5, bg='#000',fg='#ff793f')
        label_ID.grid(row=1, column=0, sticky=W)

        txt_ID = Entry(DataFrameLeft, font=('Google Sans', 10,'bold'), textvariable=self.member_id_var, width=29)
        txt_ID.grid(row=1, column=1)

        # ---------------Title--------------------

        # labels for the title details
        label_tit = Label(DataFrameLeft, text="Book Type : ", font=("Helvetica", 10,'bold'), padx=5, pady=5, bg='#000',fg='#ff793f')
        label_tit.grid(row=2, column=0, sticky=W)

        txt_tit = Entry(DataFrameLeft, font=('Google Sans', 10,'bold'), textvariable=self.title_var, width=29)
        txt_tit.grid(row=2, column=1)

        # ---------------First Name--------------------

        # labels for the first name details
        label_first_name = Label(DataFrameLeft, text="First Name : ", font=("Helvetica", 10,'bold'), padx=5, pady=5,
                                 bg='#000',fg='#ff793f')
        label_first_name.grid(row=3, column=0, sticky=W)

        txt_first_name = Entry(DataFrameLeft, font=('Google Sans', 10,'bold'), textvariable=self.first_name_var, width=29)
        txt_first_name.grid(row=3, column=1)

        # ---------------Last Name--------------------
        # labels for the last name details
        label_last_name = Label(DataFrameLeft, text="Last Name : ", font=("Helvetica", 10,'bold'), padx=5, pady=5,
                                bg='#000',fg='#ff793f')
        label_last_name.grid(row=4, column=0, sticky=W)

        txt_last_name = Entry(DataFrameLeft, font=('Google Sans', 10,'bold'), textvariable=self.last_name_var, width=29)
        txt_last_name.grid(row=4, column=1)

        # ---------------Mobile Number--------------------
        # labels for the Mobile number details
        label_mobile_number = Label(DataFrameLeft, text="Mobile Number : ", font=("Helvetica", 10,'bold'), padx=5, pady=5,
                                    bg='#000',fg='#ff793f')
        label_mobile_number.grid(row=5, column=0, sticky=W)

        txt_mobile_number = Entry(DataFrameLeft, font=('Google Sans', 10,'bold'), textvariable=self.mobile_number_var,
                                  width=29)
        txt_mobile_number.grid(row=5, column=1)

        # ---------------Address Line 1--------------------
        # labels for the address details
        label_address = Label(DataFrameLeft, text="Address : ", font=("Helvetica", 10,'bold'), padx=5, pady=5,
                              bg='#000',fg='#ff793f')
        label_address.grid(row=6, column=0, sticky=W)

        txt_address = Entry(DataFrameLeft, font=('Google Sans', 10,'bold'), textvariable=self.address_var, width=29)
        txt_address.grid(row=6, column=1)

        # ---------------Book Name--------------------
        # labels for the bookName details
        label_bookName = Label(DataFrameLeft, text="Book Name : ", font=("Helvetica", 10,'bold'), padx=5, pady=5,
                               bg='#000',fg='#ff793f')
        label_bookName.grid(row=7, column=0, sticky=W)

        txt_bookName = Entry(DataFrameLeft, font=('Google Sans', 10,'bold'), textvariable=self.book_name_var, width=29)
        txt_bookName.grid(row=7, column=1)

        # ---------------Book Author--------------------
        # labels for the bookID detail
        label_bookID = Label(DataFrameLeft, text="Book Author : ", font=("Helvetica", 10,'bold'), padx=5, pady=5,
                             bg='#000',fg='#ff793f')
        label_bookID.grid(row=8, column=0, sticky=W)

        txt_bookID = Entry(DataFrameLeft, font=('Google Sans', 10,'bold'), textvariable=self.book_author_var, width=29)
        txt_bookID.grid(row=8, column=1)

        # ---------------Book ID--------------------
        # labels for the bookID details
        label_bookID = Label(DataFrameLeft, text="Book ID : ", font=("Helvetica", 10,'bold'), padx=5, pady=5, bg='#000',fg='#ff793f')
        label_bookID.grid(row=9, column=0, sticky=W)

        txt_bookID = Entry(DataFrameLeft, font=('Google Sans', 10,'bold'), textvariable=self.book_id_var, width=29)
        txt_bookID.grid(row=9, column=1)

        # ---------------Issue Date--------------------

        # labels for the issueDate details
        label_issue_date = Label(DataFrameLeft, text="Issue Date : ", font=("Helvetica", 10,'bold'), padx=5, pady=5,
                                 bg='#000',fg='#ff793f')
        label_issue_date.grid(row=0, column=2, sticky=W)
        txt_issue_date = Entry(DataFrameLeft, font=("Helvetica", 10,'bold'), textvariable=self.issue_date_var, width=29)
        txt_issue_date.grid(row=0, column=3)

        # ---------------Due Date--------------------
        # labels for the dueDate details
        label_due_date = Label(DataFrameLeft, text="Due Date : ", font=("Helvetica", 10,'bold'), padx=5, pady=5,
                               bg='#000',fg='#ff793f')
        label_due_date.grid(row=1, column=2, sticky=W)

        txt_due_date = Entry(DataFrameLeft,font=("Helvetica", 10,'bold'), textvariable=self.due_date_var,
                             width=29)
        txt_due_date.grid(row=1, column=3)

        # ---------------Late Return Fine--------------------
        # labels for the late return fine  details
        label_lateReturn = Label(DataFrameLeft, text="Late Return Fine : ", font=("Helvetica", 10,'bold'), padx=5, pady=5,
                                 bg='#000',fg='#ff793f')
        label_lateReturn.grid(row=2, column=2, sticky=W)

        txt_lateReturn = Entry(DataFrameLeft, font=('Google Sans', 10,'bold'), textvariable=self.late_fine_var, width=29)
        txt_lateReturn.grid(row=2, column=3)

        # -----------------------------------
        # labels for the Actual Price of the book details
        label_book_price = Label(DataFrameLeft, text="Book Price : ", font=("Helvetica", 10,'bold'), padx=5, pady=5,
                                 bg='#000',fg='#ff793f')
        label_book_price.grid(row=3, column=2, sticky=W)

        txt_book_price = Entry(DataFrameLeft, font=('Google Sans', 10,'bold'), textvariable=self.book_price_var, width=29)
        txt_book_price.grid(row=3, column=3)

        # --------------------------------------------DataFrame Right--------------------------------------------------------------
        # to have another frame in the right
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="#000", fg="#ff793f", bd=4, relief=RIDGE,
                                    font=("Helvetica", 25, "italic"))
        # for placing the frame with co-ordinates as given
        DataFrameRight.place(x=870, y=5, width=580, height=350)

        self.txtBox = Text(DataFrameRight, font=("Helvetica", 10,'bold'), width=50, height=16, padx=2)
        self.txtBox.grid(row=0, column=2)

        #  This widget provides a slide controller that is used to implement vertical scrolled widgets, such as Listbox, Text and Canvas. Note that you can also create horizontal scrollbars on Entry widgets.
        listScrollbar = Scrollbar(DataFrameRight)
        # ns-> north-south
        listScrollbar.grid(row=0, column=1, sticky="ns")

        # list of books
        listBooks = ['Absalom, Absalom!', "At which point is the night", 'After Many a Summer Dies the Swan',
                     'Ah Wilderness!', 'Alien Corn (play)', "All Passion Spent", "All the King",
                     "Alone on a Wide", "Wide Sea", "An Acceptable Time", "Antic Hay", "An Evil Cradling",
                     "Arms and the Man", "As I Lay Dying", "A Time to Kill", "Behold the Man", "Beneath the Bleeding",
                     "Beyond the Mexique Bay", "Blithe Spirit", "Blood's a Rover", "Blue Remembered Earth",
                     "Bonjour Tristesse", "Brandy of the Damned",
                     "Bury My Heart at Wounded Knee", "Butter In a Lordly Dish",
                     "By Grand Central Station I Sat Down and Wept", "Cabbages and Kings", "Carrion Comfort",
                     "A Catskill Eagle", "The Children of Men"]

        # if we select a book then the details are auto filled.
        def selectbook(event=''):
            value = str(listBox.get(listBox.curselection()))
            x = value
            print("hello : ", value)
            try:
                conn = mysql.connector.connect(host="localhost", username="YOUR USERNAME", password="YOUR PASSWORD",
                                               database="library")

                if (conn == None):
                    raise DatabaseError("Cannot connect to the database")

                my_cursor = conn.cursor()

                my_cursor.execute(f"SELECT * from library.book_data where book_name = \'{x}\'")
                new_cursor = list(my_cursor)
                cursor_list = []
                for i in range(len(new_cursor[0])):
                    cursor_list.append(new_cursor[0][i])

                self.book_id_var.set(cursor_list[0])
                self.book_name_var.set(cursor_list[1])
                self.book_author_var.set(cursor_list[2])
                self.book_price_var.set(cursor_list[3])
                self.title_var.set(cursor_list[4])
                self.late_fine_var.set(cursor_list[5])
                today = datetime.date.today()
                tdelta = today + datetime.timedelta(days=15)
                self.issue_date_var.set(today)
                self.due_date_var.set(tdelta)

            except DatabaseError as e:
                print(e)

            except Exception as e:
                print(e)
            finally:
                print("over")

        # # The Listbox widget is used to display a list of items from which a user can select a number of items.
        listBox = Listbox(DataFrameRight, font=("Helvetica", 10,'bold'), width=20, height=18)
        listBox.bind('<<ListboxSelect>>', selectbook)
        listBox.grid(row=0, column=0, padx=2, pady=2)
        listScrollbar.config(command=listBox.yview)

        # inserting books into the listBox
        for item in listBooks:
            listBox.insert(END, item)

        # --------------------------------------------Button Frame---------------------------------------------------------------
        #
        frameButton = Frame(self.root, bd=4, relief=RIDGE, padx=180, pady=15, bg="#000")
        frameButton.place(x=0, y=470, width=1530, height=70)

        # adding buttons in the frameButton
        btnAddData = Button(frameButton, command=self.add_data, text='Add Data', font=('Google Sans', 10,'bold'), padx=3,
                            pady=3, width=23, bg="#ff793f", fg="#000")
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(frameButton, text='Show Data', command = self.show_data,font=('Google Sans', 10,'bold'), padx=3, pady=3, width=23,
                             bg="#ff793f", fg="#000")
        btnShowData.grid(row=0, column=2)


        btnUpdateData = Button(frameButton, text='Update', command = self.update_func ,font=('Google Sans', 10,'bold'), padx=3, pady=3, width=23,bg="#ff793f", fg="#000")
        btnUpdateData.grid(row=0, column=4)


        btnResetData = Button(frameButton, text='Reset', command = self.reset ,font=('Google Sans', 10,'bold'), padx=3, pady=3, width=23,bg="#ff793f", fg="#000")
        btnResetData.grid(row=0, column=6)


        btnResetData = Button(frameButton, text='Delete', command = self.delete_func ,font=('Google Sans', 10,'bold'), padx=3, pady=3, width=23,bg="#ff793f", fg="#000")
        btnResetData.grid(row=0, column=8)

        btnExit = Button(frameButton, text='Exit', command = self.exit_func,font=('Google Sans', 10, 'bold'), padx=3, pady=3, width=23, bg="#ff793f", fg="#000")
        btnExit.grid(row=0, column=10)





        #  ---------------------------------------------Search------------------------------------------------------
        frameSearch = Frame(self.root, bd=4, relief=RIDGE, padx=180, pady=8, bg="#000")
        frameSearch.place(x=0, y=535, width=1530, height=65)

        label_search = Label(frameSearch, text="Search Books :", font=("Helvetica", 15), padx=5,pady = -3,
                                 bg='#000', fg='#ff793f')
        label_search.grid(row=0, column=0, sticky=W)
        
        txt_search = Entry(frameSearch, font=('Google Sans', 15,'bold'), textvariable=self.search_var, width=50)
        txt_search.grid(row=0, column=1)

        btnExit = Button(frameSearch, text='Search', command = self.search_func,font=('Google Sans', 10, 'bold'), padx=1, pady=1, width=23, bg="#ff793f", fg="#000")
        btnExit.grid(row=0, column=2)


        #  --------------------------------------------Database Frame--------------------------------------------------------------

        # Creating a frame in the lower part
        frameDatabase = Frame(self.root, bd=4, relief=RIDGE, padx=20, pady=5, bg="#000")
        frameDatabase.place(x=0, y=585, width=1530, height=210)

        # Creating a frame inside the above mentioned frame
        table_frame = Frame(frameDatabase, bd=4, relief=RIDGE, padx=20, bg="#000")
        table_frame.place(x=0, y=2, width=1460, height=190)

        # defining the orientattion of the scrollbar
        xscroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # treeview is a widget through which you can add dynamic nodes into your tree ...like insert data , delete data etc
        self.library_table = ttk.Treeview(table_frame, column=(
            'Membertype', 'Member ID', 'Title', 'First Name', 'Last Name', 'Mobile Number', 'Address', 'Book Name',
            'Book Author', 'Book ID', 'Issue Date', 'Due Date', "Late Fine", "Book Price"), xscrollcommand=xscroll.set,
                                          yscrollcommand=yscroll.set)  # setting the scrollbars

        # placing the scrollbars
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        # making it work
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        # this text will appear as a heading of the tables to the users
        self.library_table.heading('Membertype', text='Member Type')
        self.library_table.heading('Member ID', text='Member ID')
        self.library_table.heading('Title', text='Title')
        self.library_table.heading('First Name', text='First Name')
        self.library_table.heading('Last Name', text='Last Name')
        self.library_table.heading('Mobile Number', text='Mobile Number')
        self.library_table.heading('Address', text='Address')
        self.library_table.heading('Book Name', text='Book Name')
        self.library_table.heading('Book Author', text='Book Author')
        self.library_table.heading('Book ID', text='Book ID')
        self.library_table.heading('Issue Date', text='Issue Date')
        self.library_table.heading('Due Date', text='Due Date')
        self.library_table.heading('Late Fine', text='Late Fine')
        self.library_table.heading('Book Price', text='Book Price')

        self.library_table['show'] = 'headings'
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column('Membertype', width=100)
        self.library_table.column('Member ID', width=100)
        self.library_table.column('Title', width=100)
        self.library_table.column('First Name', width=100)
        self.library_table.column('Last Name', width=100)
        self.library_table.column('Mobile Number', width=100)
        self.library_table.column('Address', width=100)
        self.library_table.column('Book Name', width=100)
        self.library_table.column('Book Author', width=100)
        self.library_table.column('Book ID', width=100)
        self.library_table.column('Issue Date', width=100)
        self.library_table.column('Due Date', width=100)
        self.library_table.column('Late Fine', width=100)
        self.library_table.column('Book Price', width=100)

        self.fetch_data()
        self.library_table.bind('<ButtonRelease-1>',self.get_cursor)




    def search_func(self):

        try:
            conn = mysql.connector.connect(host="localhost", username="YOUR USERNAME", password="YOUR PASSWORD",
                                               database="library")
            if conn != "":
                x = self.search_var.get().lower()
                if x=='':
                    raise InputError('Invalid Search')
                my_cursor = conn.cursor()
                my_cursor.execute(f'SELECT * from library.book_data where book_name=\'{x}\'')
                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.library_table.delete(*self.library_table.get_children())
                    for i in rows:
                        self.library_table.insert("", END, values=i)
                    conn.commit()
                    conn.close()
                else:
                    raise InputError('No such book borrowed')


            else:
                raise DatabaseError('Connection Error!')
        except DatabaseError as e:
            print(e)
        except InputError as e:
            messagebox.showerror('Library Management System',e)
        except Exception as e:
            print(e)
        finally:
            self.search_var.set("")
        pass


    def exit_func(self):
        exit_func = messagebox.askyesno('Library Management System','Do you wish to exit the system?')
        if exit_func > 0:
            self.root.destroy()
        else:
            return
        

    def delete_func(self):
        if self.member_id_var.get()=='':
            messagebox.showerror('Error','First Select the Member')
        else:
            conn = mysql.connector.connect(host="localhost", username="YOUR USERNAME", password="YOUR PASSWORD",
                                               database="library")
            my_cursor = conn.cursor()
            query = 'delete from library where member_id=%s'
            value = (self.member_id_var.get(),)
            my_cursor.execute(query, value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo('Success','Member has been deleted')

    def update_func(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='Krish2001@', database='library')
            if conn != "":
                my_cursor = conn.cursor()
                my_cursor.execute('update library set member_type=%s, title=%s, first_name=%s, last_name=%s, mobile_number=%s,address=%s, book_name=%s, book_author=%s, book_id=%s,issue_date=%s,due_date=%s,late_fine=%s,book_price=%s where member_id=%s' ,
                    (
                        self.member_type_var.get(),
                        # self.member_id_var.get(),
                        self.title_var.get(),
                        self.first_name_var.get(),
                        self.last_name_var.get(),
                        self.mobile_number_var.get(),
                        self.address_var.get(),
                        self.book_name_var.get(),
                        self.book_author_var.get(),
                        self.book_id_var.get(),
                        self.issue_date_var.get(),
                        self.due_date_var.get(),
                        self.late_fine_var.get(),
                        self.book_price_var.get(),
                        self.member_id_var.get(),

                    ))

                # rows = my_cursor.fetchall()

                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()
                messagebox.showinfo('Success!', 'Member has been updated.')

            else:
                raise DatabaseError('Connection Error!')
        except DatabaseError as e:
            print(e)


        
    def reset(self):
        self.member_type_var.set("")
        self.member_id_var.set("")
        self.title_var.set("")
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.mobile_number_var.set("")
        self.address_var.set("")
        self.book_name_var.set("")
        self.book_author_var.set("")
        self.book_id_var.set("")
        self.book_price_var.set("")
        self.issue_date_var.set("")
        self.due_date_var.set("")
        self.late_fine_var.set("")
        self.txtBox.delete('1.0', END)




    def show_data(self):
        self.txtBox.insert(END,'Member Type: \t\t' + self.member_type_var.get() + '\n')
        self.txtBox.insert(END,'First Name: \t\t' + self.first_name_var.get() + '\n')
        self.txtBox.insert(END,'Last Name: \t\t' + self.last_name_var.get() + '\n')
        self.txtBox.insert(END,'Book Name: \t\t' + self.book_name_var.get() + '\n')
        self.txtBox.insert(END,'Book Author: \t\t' + self.book_author_var.get() + '\n')
        self.txtBox.insert(END,'Book Type: \t\t' + self.title_var.get() + '\n')
        self.txtBox.insert(END,'Issue Date: \t\t' + self.issue_date_var.get() + '\n')
        self.txtBox.insert(END,'Due Date: \t\t' + self.due_date_var.get() + '\n')
        self.txtBox.insert(END,'Book Price: \t\t' + self.book_price_var.get() + '\n')




    def fetch_data(self):
        
        try:
            conn = mysql.connector.connect(host="localhost", username="YOUR USERNAME", password="YOUR PASSWORD",
                                               database="library")
            if conn!= "":
                my_cursor = conn.cursor()
                my_cursor.execute('SELECT * from library')
                rows = my_cursor.fetchall()
                
                if len(rows)!=0:
                    self.library_table.delete(*self.library_table.get_children())
                    for i in rows:
                        self.library_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
                
            else:
                raise DatabaseError('Connection Error!')
        except DatabaseError as e:
            print(e)




    def get_cursor(self,event=''):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_type_var.set(row[0])
        self.member_id_var.set(row[1])
        self.title_var.set(row[2])
        self.first_name_var.set(row[3])
        self.last_name_var.set(row[4])
        self.mobile_number_var.set(row[5])
        self.address_var.set(row[6])
        self.book_name_var.set(row[7])
        self.book_author_var.set(row[8])
        self.book_id_var.set(row[9])
        self.issue_date_var.set(row[10])
        self.due_date_var.set(row[11])
        self.late_fine_var.set(row[12])
        self.book_price_var.set(row[13])


        
    # connecting with the database
    def add_data(self):
        try:
            # connecting to the mysql database
            conn = mysql.connector.connect(host="localhost", username="YOUR USERNAME", password="YOUR PASSWORD",
                                               database="library")
            # creating a cursor object through which we can execute the SQL query
            my_cursor = conn.cursor()
            # exception handling
            if (
                self.member_type_var.get() == "" or self.member_id_var.get() == "" or self.title_var.get() == "" or self.first_name_var.get() == "" or self.last_name_var.get() == "" or self.address_var.get() == "" or self.book_name_var.get() == "" or self.book_author_var.get() == "" or self.book_id_var.get()== "" or self.book_price_var.get() == "" or self.issue_date_var.get() == "" or self.due_date_var.get() == ""):
                # print(self.member_type_var.get())
                # print(self.member_id_var.get())
                # print(self.title_var.get())
                # print(self.first_name_var.get())
                # print(self.last_name_var.get())
                # print(self.mobile_number_var.get())
                # print(self.book_name_var.get())
                # print(self.book_id_var.get())
                # print(self.book_author_var.get())
                # print(self.issue_date_var.get())
                # print(self.due_date_var.get())
                # print(self.late_fine_var.get())
                # print(self.book_price_var.get())
                raise InputError("Please fill up all the fields properly")
            # elif (len(self.mobile_number_var) <= 9 and len(self.mobile_number_var) > 10):
            #     raise InputError("Please check the entered mobile number")
            my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.member_type_var.get(),
                self.member_id_var.get(),
                self.title_var.get(),
                self.first_name_var.get(),
                self.last_name_var.get(),
                self.mobile_number_var.get(),
                self.address_var.get(),
                self.book_name_var.get(),
                self.book_author_var.get(),
                self.book_id_var.get(),
                self.issue_date_var.get(),
                self.due_date_var.get(),
                self.late_fine_var.get(),
                self.book_price_var.get()
            )
                              )
            # commiting changes into the database
            conn.commit()
            # closing the connection
            conn.close()
            # message box
            messagebox.showinfo('Success', 'Member has been inserted successfully')
        except InputError as e:
            messagebox.showerror('Failure!', e)
        except Exception as e:
            print(e)
        else:
            # print("Database connected successfully")
            self.member_type_var.set("")
            self.member_id_var.set("")
            self.title_var.set("")
            self.first_name_var.set("")
            self.last_name_var.set("")
            self.mobile_number_var.set("")
            self.address_var.set("")
            self.book_name_var.set("")
            self.book_author_var.set("")
            self.book_id_var.set("")
            self.book_price_var.set("")
            self.issue_date_var.set("")
            self.due_date_var.set("")
            self.late_fine_var.set("")

            self.fetch_data()


if __name__ == "__main__":
    root = Tk()

    # instace of the class library
    myobj = LibraryManagementSystem(root)
    # to keep the window open
    root.mainloop()
