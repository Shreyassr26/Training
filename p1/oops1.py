class Bank:
    Bank_name = "ICICI"
    ROI = 14
    MBL = "Mumbai"

    def __init__(self, Name, Age, Phone, Email, Bal=0):
        self.Name = Name
        self.Age = Age
        self.Phone = Phone
        self.Email = Email
        self.Bal = Bal

    def deposit(self, amt=0):
        if amt == 0:
            amount = self.get_amount()
        self.Bal+=amt
        self.success()

    def withdraw(self, amt=0):
        if amt == 0:
            amt = self.get_amount()
        if amt>self.Bal:
            self.failure()
            print("Insufficient Funds")
            return
        self.Bal = self.sub(self.Bal, amt)
        self.success()

    def display(self):
        print(self.Name, self.Age, self.Phone, self.Email, self.Bal)

    def modify(self, Name="",Age=0,Phno=0,Email=""):
        if Name!="":
            self.Name=Name
        if Age!="":
            self.Age = Age
        if Phno!=0:
            self.Phone=Phno
        if Email!="":
            self.Email=Email
        self.success()

    @classmethod
    def change_BName(cls,new=""):
        if new=="":
            cls.Bank_name=new
        cls.success()

    @classmethod
    def modify_ROI(cls,new=0):
        if new==0:
            new=cls.get_ROI()
        cls.ROI=new
        cls.success()

    @staticmethod
    def get_ROI():
        new=float(input("Enter new ROI"))
        return new

    @staticmethod
    def sub(a,b):
        return a-b

    @staticmethod
    def failure():
        print("Transaction failure")

    @staticmethod
    def success():
        print("Transaction successful")

    @staticmethod
    def get_amount():
        amount = int(input("Enter the amount"))
        return amount

# Reeta = Bank("Reeta",25,9845632644,"reeta@bata.com",10000)
# Reeta.display()
# #Reeta.deposit()
# Reeta.withdraw()
# Reeta.display()

class Bank2(Bank):
    def __init__(self, Name,Age,Phno,Email,Pan,Aadhar,Bal=0):
        super(Bank2,self).__init__(Name,Age,Phno,Email, Bal=0)

        self.Pan=Pan
        self.Aadhar=Aadhar

    def add_aadhar_pan(self,Pan,Aadhar):
        self.Pan=Pan
        self.Aadhar=Aadhar

    def display(self):
        print(super(Bank2.display()))

Reeta1 = Bank("Reeta",25,9989898989,"reeta@bata.com",10000)
Bank2.add_aadhar_pan(Reeta1,"vhjd665",65464646)
print(Reeta1.Aadhar)
print(Reeta1.Pan)
print(Reeta1.display())

