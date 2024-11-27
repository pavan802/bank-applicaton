from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class SBI:
    Roi=0.07
    def __init__(self,name,mobno,aadhar,PAN,gender,bal,pin):
        self.name=name
        self.mobno=mobno
        self.aadhar=aadhar
        self.PAN=PAN
        self.gender=gender
        self.bal=bal
        self.pin=pin
    def details(self):
        print(f'''name:{self.name}
              mobno:{self.mobno}
              aadhar:{self.aadhar}
              PAN:{self.PAN}
              gender:{self.gender}
              bal:{self.bal}
              pin:{self.pin}
                            ''')
    def withdraw(self):
        if self.checkpin() ==self.pin:
            amount=int(input("enter the amount to withdraw: "))
            if self.bal >=amount:
                print("amount debited successfully..")
                print(f"available balance {self.bal}")
            else:
                print("insufficent balance...")
        else:
            print('invalid pin')
    def deposite(self):
        amount=int(input("enter the amount to  deposite: "))
        self.bal +=amount
        print("amount credited successfully..")
        print(f"available balance {self.bal}")
    def checkbal(self):
        if self.checkpin ==self.pin:
            print(f"available balance {self.bal}")
        else:
            print('invalid pin')
    @staticmethod
    def checkpin():
        return int(input('enter a 4_digit pin: '))
    @classmethod
    def changeROI(CLS):
        var=float(input('enter the newROI:'))
        SBI.ROI=var
    def changepin(self):
        oldpin=int(input('enter oldpin: '))
        if self.pin==oldpin:
            newpin=int(input('enter new pin: '))
            self.pin=newpin
        else:
            print('oldpin is incorret')

cust1=SBI("pavan",9346305538,"adl94","HJK1234","male",10000,1234)
cust2=SBI("ram",123456789,"12345123","lkjh098","male",8000,5678)
print(cust1.details())
print(cust1.changepin())
print(cust1.details())








