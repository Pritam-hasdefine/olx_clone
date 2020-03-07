from GUIhelper import GUIhelper
from DBhelper import DBhelper
#from tkinter import filedialog

class OLX(GUIhelper):
    def __init__(self):

        self.db =DBhelper()
        super(OLX, self).__init__(self.loginListner, self.loadRegWindow)  # calling child by parent
    def loginListner(self):
        data = self.db.search('email', self._emailInput.get(), 'password', self._passwordInput.get(), 'userdb1')

        if len(data) == 1:
            self.sessionId=data[0][0]
            self.loadProfile()
        else:
            self.message("OLX","LOGIN FAILED")
    def loadRegWindow(self):
        self.regWindow(self.registrationHandler)
    def registrationHandler(self):
        if self._nameInput.get() == "" or self._emailInput.get() == "" or self._passwordInput.get() == "" or self._PhoneInput.get() == ""  or self._addInput.get() == "" :
            self.label2.configure(text="PLEASE FILL ALL DETAILS", bg="yellow", fg="red")
        else:
           # p = self.fileDialog()
           # print(p)
            regDict = {}
            regDict['user_id'] = "NULL"
            regDict['NAME'] = self._nameInput.get()
            regDict['PASSWORD'] = self._passwordInput.get()
            regDict['PHONE'] = self._PhoneInput.get()
            regDict['EMAIL'] = self._emailInput.get()
            regDict['ADDRESS'] = self._addInput.get()
            #regDict['IMAGE'] = p




            response = self.db.insert(regDict, 'userdb1')

            if response == 1:
                self._root.destroy()
                obj = GUIhelper(self.loginListner, self.loadRegWindow)
                self.label2.configure(text="Registration Successfull ", bg="white", fg="green")
            else:
                self.label2.configure(text="Registration Failed ", bg="red", fg="Yellow")

    def fileDialog(self):
        _filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        return _filename
    def loadProfile(self):
        data=self.db.searchOne('user_id',self.sessionId,'userdb1',"LIKE")
        self.mainWindow(self,data,mode=0)
    def viewadds(self,num):
            #title="Error"
            #text="[+] Can't Load Data"

            nedata = self.db.searchOne('user_id', self.sessionId, 'userdb1', "LIKE")
            data = self.db.search1('item','owner','not like',nedata[0][1])
            new_data=[]

            if num<0 or num>len(data)-1:
                self.message("Error","No More")
            else:
                new_data.append(data[num])
                self.mainWindow(self,new_data,mode=2,num=num)
    def createadd1(self):
        data = self.db.searchOne('user_id', self.sessionId, 'userdb1', "LIKE")
        self.mainWindow(self,data, mode=3)
    def createadds(self,data):
        if self._nameInput.get() == "" or self._DescInput.get() == "" or self._CostInput.get() == "":
            self.label2.configure(text="PLEASE FILL ALL DETAILS", bg="yellow", fg="red")
        else:
            regDict = {}
            regDict['item_id'] = "NULL"
            regDict['Item'] = self._nameInput.get()
            regDict['Description'] = self._DescInput.get()
            regDict['Cost'] = self._CostInput.get()
            regDict['Owner'] = data[0][1]
            response = self.db.insert(regDict, 'item')
            if response == 1:
                self.mainWindow(self,data)
            else:
                self.message("Error","Failed to Create Add")
                self.mainWindow(self,data)
    def showwishlist(self,num):
        data=self.db.searchOne('customer', self.sessionId, 'wishlist', "LIKE")
        print(data)
        new_data = []

        if num < 0 or num > len(data) - 1:
            self.message("Error", "No More")
        else:
            new_data.append(data[num])
            self.mainWindow(self, new_data, mode=1, num=num)
    def showmyadds(self,num):
        nedata = self.db.searchOne('user_id', self.sessionId, 'userdb1', "LIKE")
        data = self.db.search1('item', 'owner', 'like', nedata[0][1])
        new_data = []
        print(data)
        if num < 0 or num > len(data) - 1:
            self.message("Error", "No More")
        else:
            new_data.append(data[num])
            self.mainWindow(self, new_data, mode=4, num=num)
    def showowner(self,num,itm):
        nedata = self.db.searchOne('item', itm, 'item', "LIKE")
        data = self.db.search1('userdb1', 'name', 'like', nedata[0][4])
        print(nedata)
        print(data)
        new_data=self.db.searchOne('name', data[0][1],'userdb1', "LIKE")
        self.mainWindow(self, new_data, mode=5, num=num)
    def addtowishlist(self,itm):
        nedata = self.db.searchOne('item', itm, 'item', "LIKE")
        data = self.db.search1('userdb1', 'name', 'like', nedata[0][4])
        regDict = {}
        regDict['wl_id'] = "NULL"
        regDict['Item'] = nedata[0][1]
        regDict['Cost'] = str(nedata[0][3])
        regDict['Owner'] = nedata[0][4]
        regDict['Image']=(nedata[0][-1])
        regDict['customer']=str(self.sessionId)
        print(regDict)
        response = self.db.insert(regDict, 'wishlist')
        if response !=1:
            self.message("Error","Failed")
    def update(self):
        data = self.db.searchOne('user_id', self.sessionId, 'userdb1', "LIKE")
        self.editWindow(self,data)
        self.edit()
        print("ABCD")
    def edit(self):
        ref= self.db.searchOne('user_id', self.sessionId, 'userdb1', "LIKE")
        ref=list(ref[0])
        regDict = {}
        regDict['user_id'] = "NULL"
        regDict['NAME'] = self._nameInput.get()
        regDict['PASSWORD'] = self._passwordInput.get()
        regDict['PHONE'] = self._PhoneInput.get()
        regDict['EMAIL'] = self._emailInput.get()
        regDict['ADDRESS'] = self._addInput.get()

        for i,j,k in zip(ref,regDict.values(),regDict):
            if j=='':
                regDict[k]=i

        response = self.db.dataupdate(regDict,str(self.sessionId))
        if response == 1:
            self.message("Message", "Updation Successfull")
            self.loadProfile()
        else:
            self.message("Error","Updation Failed")
            self.loadProfile()
    def addimg(self):
        data = self.db.searchOne('user_id', self.sessionId, 'userdb1', "LIKE")
        self.db.insertimg('userdb1',)


obj = OLX()
