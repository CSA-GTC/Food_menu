'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
""" 
    This is a travel program where you can log your travels and add notes to each log.
"""

# Gregory Clarke
# Advanced Computer Programming
# 12/17/2018


from tkinter import *
from tkinter import ttk


class App:
    def __init__(self):
        self.content = Frame(root)

        self.countries = Label(self.content, text="Entrees")
        self.items = Listbox(self.content, height=6, width=21, selectmode="SINGLE",
                             exportselection=FALSE)  # listbox for items on sale
        self.items.bind("<<ListboxSelect>>")
        for b in ["Sandwich $3", "Pizza $4", "Chicken Nuggets $3.75", "Chicken $4", "Tofu $15", "Clam Chowder $20"]:
            self.items.insert(END, b)  # Adds values to listbox

        self.textshow = Label(self.content, text="Drink")  # label for Radiobutton
        self.y = StringVar()
        self.y.set(0)
        self.car = Radiobutton(self.content, text="Soda $1", variable=self.y, value="soda")
        self.car.deselect()
        self.house = Radiobutton(self.content, text="Tea #1", variable=self.y, value="tea")
        self.personal = Radiobutton(self.content, text="Milk $0.75", variable=self.y, value="milk")
        self.fourth = Radiobutton(self.content, text="Juice $1.25", variabl=self.y, value="juice")
        self.fifth = Radiobutton(self.content, text="Bottled Water $1", variabl=self.y, value="water")

        self.spinvallabel = Label(self.content, text="Day")
        self.otherlabel = Label(self.content, text="Employee Id")
        self.spinval = StringVar()
        self.s = Spinbox(self.content, values=(
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"), textvariable=self.spinval, wrap=True, width=22, state="readonly")

        self.show = Label(self.content, text="Payment Type")  # label for combobox
        self.choosevalue = StringVar()  # value for combobox
        self.choosevalue.set("")
        self.box = ttk.Combobox(self.content, state="readonly", textvariable=self.choosevalue)
        self.box["values"] = ["Credit", "Check", "Cash"]  # Types of transportation
        self.box.bind("<<ComboboxSelected>>")  # applies selected value

        self.entry = Entry(self.content)

        self.submitbutton = Button(self.content, text="Checkout", command=self.submit)  # buttons to submit and clear
        self.calculate = Button(self.content, text="Calculate", command=self.calc)
        self.clear = Button(self.content, text="Clear", command=self.clear)

        self.menubar = Menu(root)  # menubar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)  # creates option in menubar
        self.filemenu.add_command(label="Exit", command=root.quit)

        self.error = Label(self.content)  # label for errors

        self.menubar2 = Menu(root)  # second menu for "help"
        self.helpmenu = Menu(self.menubar2, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)  # creates option in menubar
        self.helpmenu.add_command(label="About", command=self.new)  # option in help
        self.helpmenu.add_command(label="Help", command=self.other)  # option in help
        root.config(menu=self.menubar)

        self.grip_frame = Frame(root)

        self.size = ttk.Sizegrip(self.grip_frame)

        self.content.grid(column=0, row=0)  # grids widgets
        self.error.grid(column=1, row=5)
        self.countries.grid(column=0, row=0)
        self.items.grid(column=0, row=1, padx=(0, 15))
        self.box.grid(column=1, row=1, sticky=N)  # grid for items/combobox
        self.textshow.grid(column=0, row=2)     #label
        self.car.grid(column=0, row=3, sticky=N)     #radiobuttons
        self.house.grid(column=0, row=4, sticky=N)
        self.personal.grid(column=0, row=5, sticky=N)
        self.fourth.grid(column=0, row=6, sticky=N)
        self.fifth.grid(column=0, row=7, sticky=N)
        self.spinvallabel.grid(column=2, row=1)
        self.otherlabel.grid(column=2, row=1, sticky=S, pady=(0, 10))
        self.s.grid(column=1, row=1)
        self.show.grid(column=1, row=0)
        self.entry.grid(column=1, row=1, sticky=S, pady=(0, 10))
        self.calculate.grid(column=1, row=2, sticky=N)
        self.submitbutton.grid(column=1, row=3)
        self.clear.grid(column=1, row=4)
        self.size.grid(column=999, row=999)
        self.grip_frame.grid(column=999, row=999)

        root.columnconfigure(0, weight=1)  # weight for rows and columns
        root.rowconfigure(0, weight=1)
        root.minsize(450, 250)
        self.grip_frame.columnconfigure(999, weight=1)
        self.grip_frame.rowconfigure(999, weight=1)

    def clear(self):  # clears all widgets
        self.entry.delete(0, END)
        self.y.set(0)
        self.spinval.set("Monday")
        self.choosevalue.set("")
        self.items.bind(self.items.selection_clear(0, END))
        self.error.config(text="")

    def calc(self):
        values = [self.items.get(idx) for idx in self.items.curselection()]  # gets all values
        if values == "":
            self.error.config(text="Please fill out all fields")
        elif values == "Sandwich $3":
            self.x +=3

        elif values == "Pizza $4":
            self.x += 4

        elif values == "Chicken Nuggets $3.75":
            self.x += 3.75


        elif values == "Chicken $4":
            self.x += 4

        elif values == "Tofu $15":
            self.x += 15

        elif values == "Clam Chowder $20":
            self.x += 20


        if self.y == "soda":
            self.x += 1
        elif self.y == "tea":
            self.x += 1
        elif self.y == "milk":
            self.x += .75
        elif self.y == "juice":
            self.x += 1.25
        elif self.y == "water":
            self.x += 1

        else:
            self.error.config(text="Please fill out all fields")

        self.x = ""
        self.t = eval(str(self.x))
        self.error.config(text=self.t)



    def submit(self):  # submits values to file
        for y in self.x:  # runs through all values
            if y == "" or y == 0 or y == []:  # checks for empty inputs
                self.error.config(text="Error")

        str1 = ' '.join(str(e) for e in self.x)  # turns values into string
        file = open("travel_log.txt", "a")
        file.write(str1)  # writes values to file
        file.write("\n")
        file.close()

        self.spinval.set("January")
        self.choosevalue.set("")
        self.items.bind(self.items.selection_clear(0, END))
        self.error.config(text="Submitted")


    def new(self):  # makes new top level for about
        top = Toplevel(root, padx=15, pady=15)
        top.title("About")
        msg = Message(top, text="Quick Lunch\nVersion 1.0\nGregory Clarke", width=100)
        msg.pack()
        button = Button(top, text="Close", command=top.destroy)
        button.pack()
        top.resizable(width=False, height=False)

    def other(self):  # makes new top level for about
        top = Toplevel(root, padx=15, pady=15)
        top.title("Help")
        msg = Message(top, text="This program allows for the quick ordering of a meal. Fill out the page to enter complete transaction ", width=100)
        msg.pack()
        button = Button(top, text="Close", command=top.destroy)
        button.pack()
        top.resizable(width=False, height=False)


root = Tk()
app = App()
root.title("Quick Lunch")
root.mainloop()
root.destroy()
