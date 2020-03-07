from tkinter import *
from tkinter import ttk

from tkinter import messagebox

from PIL import Image, ImageTk


class GUIhelper:

    def __init__(self, f, g):

        self._root = Tk()
        self._root.title("OLX Login")
        self._root.minsize(300, 500)
        self._root.iconbitmap("img/index.ico")
        self._root.configure(background="#fd5068")

        label1 = Label(self._root, text="OLX", bg="#fd5068", fg="#fff")
        label1.configure(font=("Constantia", 24, "bold", "italic", "underline"))
        label1.pack(pady=(30, 10))

        self.label2 = Label(self._root, text="Kindly login to proceed", bg="#fd5068", fg="#fff")
        self.label2.configure(font=("Verdana", 12, "bold"))
        self.label2.pack(pady=(5, 10))

        label3 = Label(self._root, text="Email", bg="#fd5068", fg="#fff")
        label3.configure(font=("Verdana", 12, "bold"))
        label3.pack(pady=(10, 5))

        self._emailInput = Entry(self._root)
        self._emailInput.config(border=3, relief=RIDGE)
        self._emailInput.pack(ipadx=50, ipady=7, pady=(1, 10))

        label4 = Label(self._root, text="Password", bg="#fd5068", fg="#fff")
        label4.configure(font=("Verdana", 12, "bold"))
        label4.pack(pady=(10, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.config(border=3, relief=RIDGE)
        self._passwordInput.pack(ipadx=50, ipady=7, pady=(1, 30))

        btn1 = Button(self._root, text="Sign In", fg="#fd5068", bg="#fff", command=lambda: f())
        btn1.configure(width=25, height=2, font=("verdana", 10, "bold"))
        btn1.pack()

        label5 = Label(self._root, text="Not a member? Sign Up now!", bg="#fd5068", fg="#fff")
        label5.configure(font=("Verdana", 10))
        label5.pack(pady=(10, 5))

        btn2 = Button(self._root, text="SignUp Now", fg="#fd5068", bg="#fff", command=lambda: g())
        btn2.pack()

        self._root.mainloop()

    def regWindow(self, f):
        self._root.destroy()

        self._root = Tk()
        self._root.title("Register for OLX")

        self._root.minsize(300, 550)
        self._root.configure(background="#fd5068")

        label1 = Label(self._root, text="OLX", bg="#fd5068", fg="#fff")
        label1.configure(font=("Constantia", 24, "bold", "italic", "underline"))
        label1.pack(pady=(10, 10))

        self.label2 = Label(self._root, text="Fill the form to register", bg="#fd5068", fg="#fff")
        self.label2.configure(font=("Verdana", 12, "bold"))
        self.label2.pack(pady=(5, 10))

        label3 = Label(self._root, text="Name", bg="#fd5068", fg="#fff")
        label3.configure(font=("Verdana", 12, "bold"))
        label3.pack(pady=(5, 5))




        self._nameInput = Entry(self._root)
        self._nameInput.pack(ipadx=50, ipady=7, pady=(1, 5))




        label4 = Label(self._root, text="Email", bg="#fd5068", fg="#fff")
        label4.configure(font=("Verdana", 12, "bold"))
        label4.pack(pady=(5, 5))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label8 = Label(self._root, text="Password", bg="#fd5068", fg="#fff")
        label8.configure(font=("Verdana", 12, "bold"))
        label8.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label5 = Label(self._root, text="Phone", bg="#fd5068", fg="#fff")
        label5.configure(font=("Verdana", 12, "bold"))
        label5.pack(pady=(5, 5))

        self._PhoneInput = Entry(self._root)
        self._PhoneInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label6 = Label(self._root, text="ADDRESS", bg="#fd5068", fg="#fff")
        label6.configure(font=("Verdana", 12, "bold"))
        label6.pack(pady=(5, 5))

        self._addInput = Entry(self._root)
        self._addInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        btn1 = Button(self._root, text="Sign Up", fg="#fd5068", bg="#fff", command=lambda: f())
        btn1.configure(width=25, height=2, font=("verdana", 10, "bold"))
        btn1.pack()

        self._root.mainloop()



    def editWindow(self, other, data):

        self._root.destroy()

        self._root = Tk()
        self._root.title("Update Profile")

        self._root.minsize(300, 550)
        self._root.configure(background="#fd5068")

        label1 = Label(self._root, text="OLX", bg="#fd5068", fg="#fff")
        label1.configure(font=("Constantia", 24, "bold", "italic", "underline"))
        label1.pack(pady=(10, 10))

        label3 = Label(self._root, text="Name :" + data[0][1], bg="#fd5068", fg="#fff")
        label3.configure(font=("Verdana", 12, "bold"))
        label3.pack(pady=(5, 5))

        self._nameInput = Entry(self._root)
        self._nameInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label4 = Label(self._root, text="Email :" + data[0][4], bg="#fd5068", fg="#fff")
        label4.configure(font=("Verdana", 12, "bold"))
        label4.pack(pady=(5, 5))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label8 = Label(self._root, text="Password : " + data[0][2], bg="#fd5068", fg="#fff")
        label8.configure(font=("Verdana", 12, "bold"))
        label8.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label5 = Label(self._root, text="Phone :" + str(data[0][3]), bg="#fd5068", fg="#fff")
        label5.configure(font=("Verdana", 12, "bold"))
        label5.pack(pady=(5, 5))

        self._PhoneInput = Entry(self._root)
        self._PhoneInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label6 = Label(self._root, text="Address :" + str(data[0][5]), bg="#fd5068", fg="#fff")
        label6.configure(font=("Verdana", 12, "bold"))
        label6.pack(pady=(5, 5))

        self._addInput = Entry(self._root)
        self._addInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        btn1 = Button(self._root, text="Update", fg="#fd5068", bg="#fff", command=lambda: other.edit())
        btn1.configure(width=25, height=2, font=("verdana", 10, "bold"))
        btn1.pack()

        self._root.mainloop()

    def mainWindow(self, other, data, mode=0, num=0):
        num1 = num3 = num4 = num
        self.clear()
        self._root.title("My Profile")
        self._root.geometry('350x50')
        self._root.configure(background="#FD5068")

        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile", command=lambda: other.loadProfile())
        filemenu.add_command(label="Edit Profile", command=lambda: other.update())
        filemenu.add_command(label="Logout", command=lambda: self.logout())
        helpmenu = Menu(menu)
        menu.add_cascade(label="Advertisement", menu=helpmenu)
        helpmenu.add_command(label="View Adds", command=lambda: other.viewadds(0))
        helpmenu.add_command(label="Create Adds", command=lambda: other.createadd1())
        helpmenu.add_command(label="My Adds",command=lambda: other.showmyadds(0))
        helpmenu.add_command(label="Show WishList",command=lambda: other.showwishlist(0))


        if mode == 0:
            imageUrl="img/" + data[0][-1]
            load=Image.open(imageUrl)
            load=load.resize((150, 150),Image.ANTIALIAS)

            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image=render
            img.pack()
            name = "Name: " + data[0][1]
            label1 = Label(self._root, text=name, bg="#FD5068", fg="#000")
            label1.configure(font=("Verdana", 10, "bold"))
            label1.pack()

            Email = "Email: " + data[0][4]

            label2 = Label(self._root, text=Email, bg="#FD5068", fg="#000")
            label2.configure(font=("Verdana", 10, "bold"))
            label2.pack()

            Address = "From: " + data[0][5]

            label3 = Label(self._root, text=Address, bg="#FD5068", fg="#000")
            label3.configure(font=("Verdana", 10, "bold"))
            label3.pack()

            Phone = "Phone: " + str(data[0][3])

            label4 = Label(self._root, text=Phone, bg="#FD5068", fg="#000")
            label4.configure(font=("Verdana", 10, "bold"))
            label4.pack()

        if mode == 2:
            imageUrl = "img/" + data[0][-1]
            load = Image.open(imageUrl)
            load = load.resize((150, 150), Image.ANTIALIAS)

            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.pack()
            name = "Item: " + data[0][1]
            label1 = Label(self._root, text=name, bg="#FD5068", fg="#000")
            label1.configure(font=("Verdana", 10, "bold"))
            label1.pack()

            Email = "Description: " + data[0][2]

            label2 = Label(self._root, text=Email, bg="#FD5068", fg="#000")
            label2.configure(font=("Verdana", 10, "bold"))
            label2.pack()

            Address = "Cost: " + str(data[0][3])

            label3 = Label(self._root, text=Address, bg="#FD5068", fg="#000")
            label3.configure(font=("Verdana", 10, "bold"))
            label3.pack()

            Phone = "Owner: " + data[0][4]

            label4 = Label(self._root, text=Phone, bg="#FD5068", fg="#000")
            label4.configure(font=("Verdana", 10, "bold"))
            label4.pack()
            frame = Frame(self._root, bg="#FD5068")
            frame.pack()
            btn1 = Button(frame, text="Previous", bg="#FD5068", fg="#fff", command=lambda: other.viewadds(num4 - 1))
            btn1.config(bg="#FD5068", border=3, relief=RIDGE)
            btn1.pack(side=LEFT, padx=5)
            btn2 = Button(frame, text="Add to Wishlist", bg="#FD5068", fg="#fff", command=lambda: other.addtowishlist(data[0][1]))
            btn2.config(bg="#FD5068", border=3, relief=RIDGE)
            btn2.pack(side=LEFT, padx=5)
            btn3 = Button(frame, text="Show Owner Info", bg="#FD5068", fg="#fff", command=lambda: other.showowner(0,data[0][1]))
            btn3.config(bg="#FD5068", border=3, relief=RIDGE)
            btn3.pack(side=LEFT, padx=5)
            btn3 = Button(frame, text="NEXT", bg="#FD5068", fg="#fff", command=lambda: other.viewadds(num4 + 1))
            btn3.config(bg="#FD5068", border=3, relief=RIDGE)
            btn3.pack(side=LEFT, padx=5)

        if mode == 3:
            self._root.destroy()

            self._root = Tk()
            self._root.title("Create New Advertisement")

            self._root.minsize(300, 550)
            self._root.configure(background="#fd5068")

            label1 = Label(self._root, text="OLX", bg="#fd5068", fg="#fff")
            label1.configure(font=("Constantia", 24, "bold", "italic", "underline"))
            label1.pack(pady=(10, 10))

            self.label2 = Label(self._root, text="Fill the form to advertise", bg="#fd5068", fg="#fff")
            self.label2.configure(font=("Verdana", 12, "bold"))
            self.label2.pack(pady=(5, 10))

            label3 = Label(self._root, text="Item Name", bg="#fd5068", fg="#fff")
            label3.configure(font=("Verdana", 12, "bold"))
            label3.pack(pady=(5, 5))

            self._nameInput = Entry(self._root)
            self._nameInput.pack(ipadx=50, ipady=7, pady=(1, 5))

            label4 = Label(self._root, text="Description", bg="#fd5068", fg="#fff")
            label4.configure(font=("Verdana", 12, "bold"))
            label4.pack(pady=(5, 5))

            self._DescInput = Entry(self._root)
            self._DescInput.pack(ipadx=50, ipady=7, pady=(1, 5))

            label8 = Label(self._root, text="Cost", bg="#fd5068", fg="#fff")
            label8.configure(font=("Verdana", 12, "bold"))
            label8.pack(pady=(5, 5))

            self._CostInput = Entry(self._root)
            self._CostInput.pack(ipadx=50, ipady=7, pady=(1, 5))



            btn1 = Button(self._root, text="Create", fg="#fd5068", bg="#fff", command=lambda: other.createadds(data))
            btn1.configure(width=25, height=2, font=("verdana", 10, "bold"))
            btn1.pack()

            self._root.mainloop()
        if mode == 4:
            imageUrl = "img/" + data[0][-1]
            load = Image.open(imageUrl)
            load = load.resize((150, 150), Image.ANTIALIAS)

            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.pack()
            name = "Item: " + data[0][1]
            label1 = Label(self._root, text=name, bg="#FD5068", fg="#000")
            label1.configure(font=("Verdana", 10, "bold"))
            label1.pack()

            Email = "Description: " + data[0][2]

            label2 = Label(self._root, text=Email, bg="#FD5068", fg="#000")
            label2.configure(font=("Verdana", 10, "bold"))
            label2.pack()

            Address = "Cost: " + str(data[0][3])

            label3 = Label(self._root, text=Address, bg="#FD5068", fg="#000")
            label3.configure(font=("Verdana", 10, "bold"))
            label3.pack()

            Phone = "Owner: " + data[0][4]

            label4 = Label(self._root, text=Phone, bg="#FD5068", fg="#000")
            label4.configure(font=("Verdana", 10, "bold"))
            label4.pack()
            frame = Frame(self._root, bg="#FD5068")
            frame.pack()
            btn1 = Button(frame, text="Previous", bg="#FD5068", fg="#fff", command=lambda: other.showmyadds(num1 - 1))
            btn1.config(bg="#FD5068", border=3, relief=RIDGE)
            btn1.pack(side=LEFT, padx=5)
            btn3 = Button(frame, text="NEXT", bg="#FD5068", fg="#fff", command=lambda: other.showmyadds(num1 + 1))
            btn3.config(bg="#FD5068", border=3, relief=RIDGE)
            btn3.pack(side=LEFT, padx=5)
        if mode == 5:

            imageUrl = "img/" + data[0][-1]
            load = Image.open(imageUrl)
            load = load.resize((150, 150), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.pack()
            name = "Name: " + data[0][1]
            label1 = Label(self._root, text=name, bg="#FD5068", fg="#000")
            label1.configure(font=("Verdana", 10, "bold"))
            label1.pack()

            Email = "Email: " + data[0][4]

            label2 = Label(self._root, text=Email, bg="#FD5068", fg="#000")
            label2.configure(font=("Verdana", 10, "bold"))
            label2.pack()

            Address = "From: " + data[0][5]

            label3 = Label(self._root, text=Address, bg="#FD5068", fg="#000")
            label3.configure(font=("Verdana", 10, "bold"))
            label3.pack()

            Phone = "Phone: " + str(data[0][3])

            label4 = Label(self._root, text=Phone, bg="#FD5068", fg="#000")
            label4.configure(font=("Verdana", 10, "bold"))
            label4.pack()
            btn1 = Button(self._root, text="Back",  bg="#FD5068", fg="#fff", command=lambda: other.viewadds(num))
            btn1.configure(width=25, height=2, font=("verdana", 10, "bold"))
            btn1.pack()
        if mode==1:
            print(data)
            imageUrl = "img/" + data[0][-2]
            load = Image.open(imageUrl)
            load = load.resize((150, 150), Image.ANTIALIAS)

            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.pack()
            name = "Item: " + data[0][1]
            label1 = Label(self._root, text=name, bg="#FD5068", fg="#000")
            label1.configure(font=("Verdana", 10, "bold"))
            label1.pack()

            Email = "Cost: " + str(data[0][2])

            label2 = Label(self._root, text=Email, bg="#FD5068", fg="#000")
            label2.configure(font=("Verdana", 10, "bold"))
            label2.pack()

            Address = "Owner: " + str(data[0][3])

            label3 = Label(self._root, text=Address, bg="#FD5068", fg="#000")
            label3.configure(font=("Verdana", 10, "bold"))
            label3.pack()


            frame = Frame(self._root, bg="#FD5068")
            frame.pack()
            btn1 = Button(frame, text="Previous", bg="#FD5068", fg="#fff", command=lambda: other.showwishlist(num3 - 1))
            btn1.config(bg="#FD5068", border=3, relief=RIDGE)
            btn1.pack(side=LEFT, padx=5)
            btn3 = Button(frame, text="NEXT", bg="#FD5068", fg="#fff", command=lambda: other.showwishlist(num3 + 1))
            btn3.config(bg="#FD5068", border=3, relief=RIDGE)
            btn3.pack(side=LEFT, padx=5)

        self._root.mainloop()

    def logout(self):
        self._root.destroy()
        self.__init__()

    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()

    def message(self, title, text):
        messagebox.showinfo(title, text)
