from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import filedialog, messagebox, ttk
import datetime
import time
import csv
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
import matplotlib.animation as graph
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
# import matplotlib.animation as animation
matplotlib.use("TkAgg")
# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf
import plotly
#Data viz
import plotly.graph_objs as go
import tkinter.messagebox as tmsg


class Calculator:

    def __init__(self, master):

        self.master = master

        master.title("Calculator")
        master.wm_iconbitmap("analysis.ico")



        # create screen widget

        self.screen = Text(master, state='disabled', width=30, height=3, background="yellow", foreground="blue")



        # position screen in window

        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.screen.configure(state='normal')



        # initialize empty screen

        self.equation = ''



        # create buttons using createButton

        b1 = self.createButton(7)

        b2 = self.createButton(8)

        b3 = self.createButton(9)

        b4 = self.createButton(u"\u232B", None)

        b5 = self.createButton(4)

        b6 = self.createButton(5)

        b7 = self.createButton(6)

        b8 = self.createButton(u"\u00F7")

        b9 = self.createButton(1)

        b10 = self.createButton(2)

        b11 = self.createButton(3)

        b12 = self.createButton('*')

        b13 = self.createButton('.')

        b14 = self.createButton(0)

        b15 = self.createButton('+')

        b16 = self.createButton('-')

        b17 = self.createButton('=', None, 34)



        # buttons

        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]



        # counter

        count = 0

        # arrange buttons with grid manager

        for row in range(1, 5):

            for column in range(4):

                buttons[count].grid(row=row, column=column)

                count += 1

        # arrange button '=' at the bottom

        buttons[16].grid(row=5, column=0, columnspan=4)



    def createButton(self, val, write=True, width=7):

        # this function creates a button, and takes one compulsory argument, the value that should be on the button



        return Button(self.master, text=val, command=lambda: self.click(val, write), width=width)



    def click(self, text, write):

        if write == None:

            if text == '=' and self.equation:

                self.equation = re.sub(u"\u00F7", '/', self.equation)

                print(self.equation)

                answer = str(eval(self.equation))

                self.clear_screen()

                self.insert_screen(answer, newline=True)

            elif text == u"\u232B":

                self.clear_screen()





        else:

            # add text to screen

            self.insert_screen(text)



    def clear_screen(self):

        # to clear screen

        # set equation to empty before deleting screen

        self.equation = ''

        self.screen.configure(state='normal')

        self.screen.delete('1.0', END)



    def insert_screen(self, value, newline=False):

        self.screen.configure(state='normal')

        self.screen.insert(END, value)

        # record every value inserted in screen

        self.equation += str(value)

        self.screen.configure(state='disabled')





def calculator():
    root8 = Tk()

    my_gui = Calculator(root8)

    root8.mainloop()

# Function command for adding expenses
def enter_data():
    print("Its working ")
    root1 = Tk()
    # Naming the Window
    root1.title("Expense-Tracker💰")

    # Adding icon to the window
    root1.wm_iconbitmap("analysis.ico")
    # Determing the size of window
    root1.geometry("540x600")

    l1 = Label(root1, bg="black", fg="white",
               text="Select Date",
               font="Helvetica 12 bold", borderwidth=8, relief=SUNKEN)
    l1.pack(pady=0, fill=X)
    cal = Calendar(root1, selectmode="day", year=2020, month=12, day=2)
    cal.pack()

    ##function for displaying confirmation of date selected
    def get_date():
        my_label.config(text="Date Entered:-" + cal.get_date())

    # Button for confirming date
    Button(root1, text="Get Date", font="Helvetica 12 bold", command=get_date).pack()
    my_label = Label(root1, text="")
    my_label.pack()
    # Getting date value in string
    date_value = cal.get_date()

    # Adding combobox for Category
    # ttk.Label(root1,text="Select category:-",font ="Helvetica 12 bold" ).pack(fill = X)
    Label(root1, bg="black", fg="white",
          text="Select Category:-",
          font="Helvetica 12 bold", borderwidth=5, relief=SUNKEN).pack(fill=X)
    category_var = StringVar()
    category = ttk.Combobox(root1, width=15, font="Helvetica 12 bold", textvariable=category_var)

    # Adding combobox items:-
    category["values"] = ("Food", "Transportation", "Education", "Rent and Utilities", "Extras")
    category.pack()
    category.current()

    # Adding botton to collect the value

    # Func for selecting the value

    def select():
        date_value = cal.get_date()
        print(date_value)
        category_value = category.get()
        print(category_value)
        amount_value = amt_entry.get()
        print(amount_value)
        description_value = description_entry.get()
        print(description_value)

        expense_data_dict = {"Date": date_value, "Category": category_value, "Amount": amount_value,
                             "Description": description_value}
        # Adding file writing method
        with open("expense_data.csv", "a") as new_file:
            fieldnames = ["Date", "Category", "Amount", "Description"]
            expense_data_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator='\n')
            # expense_data_writer.writeheader()
            expense_data_writer.writerow(expense_data_dict)
        # printing the dicts for tsting purpose
        for key, value in expense_data_dict.items():
            print(f"{key} is the key and {value} is the value")

    # Adding widget for Amount
    Label(root1, bg="black", fg="white",
          text="Enter Amount:-",
          font="Helvetica 12 bold", borderwidth=5, relief=SUNKEN).pack(fill=X)
    amt_entry = Entry(root1, bg="white", font="Helvetica 12 bold", borderwidth=4, relief=SUNKEN)
    amt_entry.pack()

    # Adding label for description
    Label(root1, bg="black", fg="white",
          text="Enter Description:-",
          font="Helvetica 12 bold", borderwidth=5, relief=SUNKEN).pack(fill=X)

    description_entry = Entry(root1, borderwidth=4, font="Helvetica 12 bold", relief=SUNKEN)
    description_entry.pack()
    Button(root1, text="Submit", font="Helvetica 12 bold", command=select).pack()

    root1.mainloop()


# TODO: Linking login and register to other functions.
def login():
    username = uservalue.get()
    passname = passvalue.get()
    userdata = []
    with open("usernames.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            userdata.append(row)
    print(userdata)
    usernames_list = [x["Username"] for x in userdata]
    passwords_list = [x["Password"] for x in userdata]
    print(usernames_list)
    print(passwords_list)
    if username in usernames_list:
        for num in range(0, len(usernames_list)):
            if usernames_list[num] == username and passwords_list[num] == passname:
                print("You are logged in.")
                # Adding Button
                Button(f3, font="Helvetica 16 bold", text="Add Expense", command=enter_data).pack(anchor=CENTER,
                                                                                                  padx=60)

                # Adding button and label and frame for Income.
                # Adding frame
                f4 = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
                f4.pack(fill=X)
                # Adding Button
                Button(f4, font="Helvetica 16 bold", text="Enter Income", command=enter_income).pack()

                # Adding label and button for opening csv files
                f5 = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
                f5.pack(fill=X)
                # Adding Button
                Button(f5, font="Helvetica 16 bold", text="Datasheets of Income/expense", command=get_csv_sheet).pack()

                # Adding Frame for graphical representation
                f6 = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
                f6.pack(fill=X)
                # Adding Button
                Button(f6, font="Helvetica 16 bold", text="Graphical representations", command=graph).pack()

                # Adding Frame for graphical representation
                f7 = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
                f7.pack(fill=X)
                # Adding Button
                Button(f7, font="Helvetica 16 bold", text="Graphical representations-Category wise",
                       command=chart).pack()

                # Adding Frame for graphical representation
                f8 = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
                f8.pack(fill=X)
                # Adding Button
                Button(f8, font="Helvetica 16 bold", text="Loan", command=loan).pack()

                # Adding Frame for graphical representation
                f9 = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
                f9.pack(fill=X)
                # Adding Button
                Button(f9, font="Helvetica 16 bold", text="Stocks", command=extra).pack()
                # Adding Frame for graphical representation
                f10 = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
                f10.pack(fill=X)
                # Adding Button
                Button(f10, font="Helvetica 16 bold", text="Calculator", command=calculator).pack()

    else:
        print("Invalid username\n")


# TODO: Register validation is left.
def register():
    username_value = uservalue.get()
    passname = passvalue.get()
    dicti_username = {"Username": username_value, "Password": passname}

    with open("usernames.csv", "a") as new_file:
        fieldnames = ["Username", "Password"]
        username_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator='\n')
        # username_writer.writeheader()
        username_writer.writerow(dicti_username)
    for key, value in dicti_username.items():
        print(f"{key} is the key and {value} is the pass")


# Function for income input
def enter_income():
    print("It's working ")

    root2 = Tk()
    # Naming the Window
    root2.title("Expense-Tracker💰")

    # Adding icon to the window
    root2.wm_iconbitmap("analysis.ico")
    # Determing the size of window
    root2.geometry("540x600")

    # Adding label and frame for getting date
    l1 = Label(root2, bg="black", fg="white",
               text="Select Date:-",
               font="Helvetica 12 bold", borderwidth=8, relief=SUNKEN)
    l1.pack(pady=10, fill=X)

    cal = Calendar(root2, selectmode="day", year=2020, month=12, day=2)
    cal.pack(pady=10)
    ##Displaying selected date
    date_value = ""

    def get_date():
        my_label.config(text="Date Entered:-" + cal.get_date())

    # date_value = cal.get_date()
    # print(date_value)
    # Button for the confirm date func
    Button(root2, text="Get Date", font="Helvetica 12 bold", command=get_date).pack()
    my_label = Label(root2, text="")
    my_label.pack()
    # Storing value of date in a variable
    l2 = Label(root2, bg="black", fg="white",
               text="Enter Your Income:-",
               font="Helvetica 12 bold", borderwidth=8, relief=SUNKEN)
    l2.pack(pady=10, fill=X)

    # Func for executing the button
    def get_income():
        login_value1 = login()
        print(login_value1)
        date_value = cal.get_date()
        print(date_value)
        # print(type(date_value))
        income_amount = int(income_entry.get())
        print(income_amount)
        # print(type(income_amount))
        income_data_dict = {"Date": date_value, "Income": income_amount}
        with open("income_data.csv", "a") as new_file:
            fieldnames = ["Date", "Income"]
            income_data_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator="\n")
            # income_data_writer.writeheader()
            income_data_writer.writerow(income_data_dict)
            # printing the dicts for tsting purpose
        for key, value in income_data_dict.items():
            print(f"{key} is the key and {value} is the value")

    income_entry = Entry(root2, width=15, font="Helvetica 12 bold", bg="white", borderwidth=4, relief=SUNKEN)
    income_entry.pack(pady=10)

    # Adding button for execution
    Button(root2, text="Enter", font="Helvetica 12 bold", command=get_income).pack()

    root2.mainloop()


##Root2 ended here############################################.

# graph
# Function for displaying the csv files dat for income and expense

def get_csv_sheet():


    # Adding the function command defination
    def display_income():
        print("It works")
        label_input["text"] = "Showing Input Data"

        tv1["columns"] = ("Date", "Income")
        # Format the column
        tv1.column('#0', stretch=NO, minwidth=0, width=0)
        tv1.column("Date", anchor=W)
        tv1.column("Income", anchor=W)

        # Creating Heading
        tv1.heading("Date", text="Date", anchor=W)
        tv1.heading("Income", text="Income", anchor=W)
        with open('income_data.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Date = row['Date']
                Income = row['Income']
                # address = row['address']
                tv1.insert("", 0, values=(Date, Income))

    def display_expense():
        print("It works")
        label_input["text"] = "Showing Expense Data"

        tv1["columns"] = ("Date", "Category", "Amount", "Description")
        # Format the column
        tv1.column('#0', stretch=NO, minwidth=0, width=0)
        tv1.column("Date", anchor=W)
        tv1.column("Category", anchor=W)
        tv1.column("Amount", anchor=W)
        tv1.column("Description", anchor=W)

        # Creating Heading
        tv1.heading("Date", text="Date", anchor=W)
        tv1.heading("Category", text="Category", anchor=W)
        tv1.heading("Amount", text="Amount", anchor=W)
        tv1.heading("Description", text="Description", anchor=W)
        with open('expense_data.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Date = row['Date']
                Category = row['Category']
                Amount = row['Amount']
                Description = row['Description']

                # address = row['address']
                tv1.insert("", 0, values=(Date, Category, Amount, Description))


    def display_loan():
        print("It works")
        label_input["text"] = "Showing Loan Data"

        tv1["columns"] = ("Date","Borrower","Amount")
        # Format the column
        tv1.column('#0', stretch=NO, minwidth=0, width=0)
        tv1.column("Date", anchor=W)
        tv1.column("Borrower", anchor=W)
        tv1.column("Amount", anchor=W)


        # Creating Heading
        tv1.heading("Date", text="Date", anchor=W)
        tv1.heading("Borrower", text="Borrower", anchor=W)
        tv1.heading("Amount", text="Amount", anchor=W)

        with open('loans_data.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                Date = row['Date']
                Borrower = row['Borrower']
                Amount = row['Amount']


                # address = row['address']
                tv1.insert("", 0, values=(Date, Borrower, Amount))

    def clear_data():
        print("It works")
        # for i in tv1.get_children():
        #     tv1.delete(i)
        for col in tv1["columns"]:
            tv1.heading(col, text='')
        tv1.delete(*tv1.get_children())

    root3 = Tk()
    # Naming the Window
    root3.title("Expense-Tracker💰")

    # Adding icon to the window
    root3.wm_iconbitmap("analysis.ico")
    # Determing the size of window
    root3.geometry("500x500")

    # Adding frame for the tree view
    f1 = LabelFrame(root3, text="Excel Data")
    f1.place(height=250, width=500)

    # Adding frame for the buttons for the income/expense data
    f2 = LabelFrame(root3, text="Choose File")
    f2.place(height=100, width=400, rely=0.65, relx=0)

    # Adding Buttons for command
    button1 = Button(f2, text="Expense", command=display_expense)
    button1.place(rely=0.65, relx=0.55)

    button2 = Button(f2, text="Income", command=display_income)
    button2.place(rely=0.65, relx=0.40)

    button3 = Button(f2, text="Loan", command=display_loan)
    button3.place(rely=0.65, relx=0.27)

    button2 = Button(f2, text="Clear Data", command=clear_data)
    button2.place(rely=0.65, relx=0.06)

    label_input = Label(f2, text="No Input Given")
    label_input.place(rely=0, relx=0)
    label_input["text"] = "Showing Loan Data"

    # Adding the Treeview widget
    tv1 = ttk.Treeview(f1)
    tv1.place(relheight=1, relwidth=1)

    # Adding the scrollbar
    tree_scrolly = Scrollbar(f1, orient="vertical", command=tv1.yview)
    tree_scrollx = Scrollbar(f1, orient="horizontal", command=tv1.xview)

    tv1.configure(xscrollcommand=tree_scrollx.set, yscrollcommand=tree_scrolly.set)
    tree_scrollx.pack(side=BOTTOM, fill=X)
    tree_scrolly.pack(side=RIGHT, fill=Y)

    root3.mainloop()


###root 3 ends here

###root4 begins here
##Adding function for the graphical representation of csv file
def graph():
    print("It's working.")



    root4 = Tk()
    # Naming the Window
    root4.title("Expense-Tracker💰")

    # Adding icon to the window
    root4.wm_iconbitmap("analysis.ico")
    # Determing the size of window
    root4.geometry("944x534")
    #Adding frame for the date range selection
    f1 = Frame(root4, bg="black", borderwidth=3, relief=SUNKEN)
    f1.pack(fill = X)

    l1 = Label(f1, bg="black", fg="yellow", text="Enter Date range:-(mm/dd/yy)", font="Helvetica 16 bold")
    l1.pack(fill = X)

    date1 = Entry(f1, borderwidth=8, relief=SUNKEN)
    date1.pack(padx = 220,side=LEFT)
    date2 = Entry(f1, borderwidth=8, relief=SUNKEN)
    date2.pack(padx = 0,side=LEFT)

    #Adding func forthe button
    def get_graph():
        print("It is working")
        date_value1 = date1.get()
        date_value2 = date2.get()
        print(date_value1,date_value2)
        date_dict ={"Date":[date_value1,date_value2]}
        date_dict["Date"] = pd.to_datetime(date_dict["Date"])
        print(date_dict["Date"][1])
        start_date = (date_dict["Date"][0]) - datetime.timedelta(days=1)
        end_date = (date_dict["Date"][1]) + datetime.timedelta(days=1)

        #Now finding the total amount of expenses.
        df = pd.read_csv("expense_data.csv")
        df["Date"] = pd.to_datetime(df["Date"])
        #print(df["Date"].dt.year[2])
        df[(df["Date"]>=start_date) & (df["Date"] <= end_date)]
        print(df[(df["Date"]>start_date) & (df["Date"] < end_date)])
        df = df[(df["Date"]>start_date) & (df["Date"] < end_date)]
        print(df)
        print(df["Amount"])
        length = len(df.index)
        Total_expense=0
        y = []
        x = []
        for i in range(0,length):
            Total_expense=Total_expense + df["Amount"][i]
            y.append(df["Amount"][i])
        print(Total_expense)
        # for i in range(0,length):
        #     x.append(df["Date"][i])
        #     print(df["Date"][i])
        # for i in range(length):
        #     x[i] = df["Date"].dt.day
        #     print("Date worked or not")
        #
        #     #print(x[i])
        for i in range(length):
            x.append(df["Date"][i])
        #print(x)
        x_1 = []
        for i in range(length):
            x_1.append(df["Date"].dt.day)
        print(x_1)

        # print(x[0][1])
        print(x[3])
        print("Date worked or not")

        f2 = Frame(root4, bg="black", borderwidth=3, relief=SUNKEN)
        f2.pack(fill=X)

        l2 = Label(f2, bg="black", fg="yellow", text=f"Total Expense for the given period is is: {Total_expense}", font="Helvetica 16 bold")
        l2.pack(fill=X)

        fig = Figure(figsize=(8, 8),
                     dpi=100)

        # list of squares


        # adding the subplot
        plot1 = fig.add_subplot(111)

        # plotting the graph
        plot1.plot(x,y)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                   master=root4)
        canvas.draw()
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                       root4)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()
        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()


        # canvas._tkcanvas.pack(side=TOP)



        #Button to get string date from widget
    Button(f1,text="submit",font="Helvetica 12 bold",command=get_graph).pack()



    root4.mainloop()
##Root4 ended here
##Root4 ended here

##adding function to display th pie chart
#Root 5 will begin here
def chart():
    print("It works")
    root5 = Tk()
    # Naming the Window
    root5.title("Expense-Tracker💰")

    # Adding icon to the window
    root5.wm_iconbitmap("analysis.ico")
    # Determing the size of window
    root5.geometry("944x534")
    # Adding frame for the date range selection
    f1 = Frame(root5, bg="black", borderwidth=3, relief=SUNKEN)
    f1.pack(fill=X)

    l1 = Label(f1, bg="black", fg="yellow", text="Enter Date range:-(mm/dd/yy)", font="Helvetica 16 bold")
    l1.pack(fill=X)

    date1 = Entry(f1, borderwidth=8, relief=SUNKEN)
    date1.pack(padx=220, side=LEFT)
    date2 = Entry(f1, borderwidth=8, relief=SUNKEN)
    date2.pack(padx=0, side=LEFT)

    def draw_graph():
        print("It works")
        date_value1 = date1.get()
        date_value2 = date2.get()
        print(date_value1, date_value2)
        date_dict = {"Date": [date_value1, date_value2]}
        date_dict["Date"] = pd.to_datetime(date_dict["Date"])
        print(date_dict["Date"][1])
        start_date = (date_dict["Date"][0]) - datetime.timedelta(days=1)
        end_date = (date_dict["Date"][1]) + datetime.timedelta(days=1)
        #opening the csv file using df
        df = pd.read_csv("expense_data.csv")
        print(df)
        food_total=0
        transport_total=0
        education_total=0
        rent_total=0
        extras_total=0
        df["Date"] = pd.to_datetime(df["Date"])
        #df[(df["Date"]>=start_date) & (df["Date"]<=end_date)]
        # print(df[(df["Date"]>=start_date) & (df["Date"]<=end_date)])
        df = df[(df["Date"]>start_date) & (df["Date"]<end_date)]
        print(df["Category"][0])

        length = len(df.index)

        #getting food_total from the df
        for i in range(length):
            if(df["Category"][i] == "Food"):
                food_total = food_total + df["Amount"][i]
                print(df["Category"][i])
                print(df["Amount"][i])
        print(food_total)

        #getting transport_total from the df
        for i in range(length):
            if(df["Category"][i] == "Transportation"):
                transport_total = transport_total + df["Amount"][i]
                print(df["Category"][i])
                print(df["Amount"][i])
        print(transport_total)

        # getting transport_total from the df
        for i in range(length):
            if (df["Category"][i] == "Education"):
                education_total = education_total + df["Amount"][i]
                print(df["Category"][i])
                print(df["Amount"][i])
        print(education_total)

        # getting transport_total from the df
        for i in range(length):
            if (df["Category"][i] == "Rent and Utilities"):
                rent_total = rent_total + df["Amount"][i]
                print(df["Category"][i])
                print(df["Amount"][i])
        print(rent_total)

        for i in range(length):
            if (df["Category"][i] == "Extras"):
                extras_total = extras_total + df["Amount"][i]
                print(df["Category"][i])
                print(df["Amount"][i])
        print(extras_total)

        gross_total = food_total+education_total+transport_total+rent_total+extras_total
        print(gross_total)

        #TODO delete it after trying
        labels = ["Food", "Education", "Transportation", "Rent and Utilities", "Extras"]
        values = [food_total,education_total,transport_total,rent_total,extras_total]

        # now to get the total number of failed in each section
        actualFigure = plt.figure(figsize=(8,8))
        actualFigure.suptitle("Category Wise expense data", fontsize=22)

        # explode=(0, 0.05, 0, 0)
        # as explode needs to contain numerical values for each "slice" of the pie chart (i.e. every group needs to have an associated explode value)
        explode = list()
        for k in labels:
            explode.append(0.1)

        pie = plt.pie(values, labels=labels, explode=explode, shadow=True,autopct='%1.1f%%')

        plt.legend(pie[0],labels,loc="lower left")
        canvas = FigureCanvasTkAgg(actualFigure,master = root5)
        canvas.get_tk_widget().pack()
        canvas.draw()

        # def angle(n):
        #     return 360*n/gross_total
        # Label(root5,text="Pie Chart").pack()
        # canvas = Canvas(root5,width=700,height=700)
        # canvas.pack()
        #
        # canvas.create_arc((0,0,300,300),fill="red",outline="red",start=angle(0),extent=angle(food_total))
        # canvas.create_arc((0,0,300,300),fill="blue",outline="blue",start=angle(food_total),extent=angle(transport_total))
        # canvas.create_arc((0,0,300,300),fill="green",outline="green",start=angle(food_total+transport_total),extent=angle(education_total))
        # canvas.create_arc((0,0,300,300),fill="yellow",outline="yellow",start=angle(food_total+transport_total+education_total),extent=angle(rent_total))
        # canvas.create_arc((0,0,300,300),fill="purple",outline="purple",start=angle(food_total+transport_total+education_total+rent_total),extent=angle(extras_total))




    #Button to get string date from widget
    Button(f1,text="submit",font="Helvetica 12 bold",command=draw_graph).pack()
    root5.mainloop()

##root5 ended here

##root6 begins here()
def loan():
    print("It works")
    print("Its working ")
    root6 = Tk()
    # Naming the Window
    root6.title("Expense-Tracker💰")

    # Adding icon to the window
    root6.wm_iconbitmap("analysis.ico")
    # Determing the size of window
    root6.geometry("540x600")

    l1 = Label(root6, bg="black", fg="white",
               text="Select Date",
               font="Helvetica 12 bold", borderwidth=8, relief=SUNKEN)
    l1.pack(pady=0, fill=X)
    cal = Calendar(root6, selectmode="day", year=2020, month=12, day=2)
    cal.pack()

    ##function for displaying confirmation of date selected
    def get_date():
        my_label.config(text="Date Entered:-" + cal.get_date())

    # Button for confirming date
    Button(root6, text="Get Date", font="Helvetica 12 bold", command=get_date).pack()
    my_label = Label(root6, text="")
    my_label.pack()
    # Getting date value in string

    def select():
        print("Just testing")

        date_value = cal.get_date()
        print(date_value)
        borrower_name = borrower_entry.get()
        print(borrower_name)
        amount_value = amt_entry.get()
        print(amount_value)


        loan_data_dict = {"Date": date_value,"Borrower": borrower_name,"Amount": amount_value,
                             }
        # Adding file writing method
        with open("loans_data.csv", "a") as new_file:
            fieldnames = ["Date", "Borrower", "Amount"]
            expense_data_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator='\n')
            # expense_data_writer.writeheader()
            expense_data_writer.writerow(loan_data_dict)
        total_loan = 0
        df = pd.read_csv("loans_data.csv")
        for i in range(len(df.index)):
            total_loan = total_loan + df["Amount"][i]
        loan_label["text"] = f"Total loan given = {total_loan}"

        for key, value in loan_data_dict.items():
            print(f"{key} is the key and {value} is the value")

    # Adding widget for Amount
    Label(root6, bg="black", fg="white",
          text="Enter Amount:-",
          font="Helvetica 12 bold", borderwidth=5, relief=SUNKEN).pack(fill=X)
    amt_entry = Entry(root6, bg="white", font="Helvetica 12 bold", borderwidth=4, relief=SUNKEN)
    amt_entry.pack()

    # Adding label for description
    Label(root6, bg="black", fg="white",
          text="Enter Borrower's name:-",
          font="Helvetica 12 bold", borderwidth=5, relief=SUNKEN).pack(fill=X)

    borrower_entry = Entry(root6, borderwidth=4, font="Helvetica 12 bold", relief=SUNKEN)
    borrower_entry.pack()
    Button(root6, text="Submit", font="Helvetica 12 bold", command=select).pack()

    total_loan = 0

    df = pd.read_csv("loans_data.csv")
    for i in range(len(df.index)):
        total_loan=total_loan+df["Amount"][i]

    loan_label = Label(root6, bg="black", fg="white",
          text=f"Total loan given = {total_loan}",
          font="Helvetica 12 bold", borderwidth=5, relief=SUNKEN)
    loan_label.pack(fill=X)
    root6.mainloop()


#root6 ended here

#root7 begins here
def extra():
    print("It works")
    root7 = Tk()
    # Naming the Window
    root7.title("Expense-Tracker💰")
    root7.wm_iconbitmap("analysis.ico")
    # Determing the size of window
    root7.geometry("944x534")
    # Adding widget for Amount
    Label(root7, bg="black", fg="white",
          text="Enter Ticker for stocks:-",
          font="Helvetica 12 bold", borderwidth=5, relief=SUNKEN).pack(fill=X)
    stock_entry = Entry(root7, bg="white", font="Helvetica 12 bold", borderwidth=4, relief=SUNKEN)
    stock_entry.pack()
    def get_price():

        stock_name = stock_entry.get()
        # Interval required 1 minute

        data = yf.download(tickers= stock_name, period='1d', interval='1m')

        # declare figure
        fig = go.Figure()

        # Candlestick
        fig.add_trace(go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'], name='market data'))

        # Add titles
        fig.update_layout(
            title=f'{stock_name} live share price evolution',
            yaxis_title='Stock Price (USD per Shares/Indian rupee(for Indian Company)')

        # X-Axes
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m", step="minute", stepmode="backward"),
                    dict(count=45, label="45m", step="minute", stepmode="backward"),
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )

        # Show
        fig.show()
    Button(root7, text="Submit", font="Helvetica 12 bold", command=get_price).pack()


    root7.mainloop()


#root7 ends here


root = Tk()
# Naming the Window
root.title("Expense-Tracker💰")

# Adding icon to the window
root.wm_iconbitmap("analysis.ico")
# Determing the size of window
root.geometry("944x525")

# Adding Frames

f1 = Frame(root, bg="black", borderwidth=3, relief=SUNKEN)

f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l1 = Label(f1, bg="black", fg="white",
           text="Here is the expense\n tracker.Please login to edit your \nfinancial statements.",
           font="Helvetica 16 bold", borderwidth=3, relief=SUNKEN)
l1.pack(pady=0)

l2 = Label(f2, bg="black", fg="yellow", text="Welcome to Expense Tracker", font="Helvetica 16 bold")
l2.pack()

# Adding login/register button
extralabel = Label(f1, bg="black")
extralabel.pack(pady=30)
user = Label(f1, bg="black", fg="white", font="Helvetica 16 bold", borderwidth=8, text="Username", relief=SUNKEN)
user.pack(fill=X)

# Entry Box
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(f1, textvariable=uservalue, borderwidth=8, relief=SUNKEN)

userentry.pack(fill=X)

password = Label(f1, bg="black", fg="white", font="Helvetica 16 bold", borderwidth=8, text="Password", relief=SUNKEN)
password.pack(fill=X)
passentry = Entry(f1, textvariable=passvalue, borderwidth=8, relief=SUNKEN)
passentry.pack(fill=X)  # TODO: look at it back

extralabel = Label(f1, bg="black")
extralabel.pack()

Button(f1, font="Helvetica 16 bold", text="Login", command=login).pack(anchor=CENTER, padx=60)

extralabel = Label(f1, bg="black", fg="white", font="Helvetica 16 bold", text="OR")
extralabel.pack()

Button(f1, font="Helvetica 16 bold", text="Register", command=register).pack(anchor=CENTER, padx=60)

###Now adding button for data entry of income and expense.

##adding frame for buttons
f3 = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
f3.pack(fill=X)

##adding label for button
# l3 = Label(root,text = "just testing",bg="black",fg="yellow",font="Helvetica 16 bold",borderwidth=8,relief = SUNKEN)
# l3.pack(fill = BOTH)




def rate_us():
    value = tmsg.askquestion("Was your experience Good?", "You used this gui..Ws your experience Good?")
    print(value)
    if value == "yes":
        msg = "Great,Rate us on appstore please."
    else:
        msg = "Tell us what went wrong.We will reach you soon"
    tmsg.showinfo("Experience", msg)
def about():
    tmsg.showinfo("info", "Programmed by Kamal Yogi\nDesigned by Kamal Yogi\n")
def help():
    tmsg.showinfo("Feedback", "For suggestions or feedback contack us at\nkamalyogi0134@gmail.com.\n")
mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="info",command=about)
m1.add_command(label="Rate us",command=rate_us)


root.config(menu=mainmenu)
mainmenu.add_cascade(label="About",menu=m1)


m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="Give Feedback",command=help)


root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m2)
root.mainloop()

#I will move it from her
#root7 is here



