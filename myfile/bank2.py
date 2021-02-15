# account,deposit,withdrwa,balance enquiry

from datetime import datetime


class Bank:
    Bank_name = "sbi"

    def __init__(self, ac_no, name, min_bal, bank_name, ):
        self.ac_no = ac_no
        self.name = name
        self.min_bal = min_bal
        self.bank_name = bank_name

    def deposit(self, amount):
        self.min_bal += amount
        print(self.bank_name, "your account", self.ac_no, "has been credited with an amount of", amount, "on",
              datetime.today(), "remaining balance is", self.min_bal)

    def withdraw(self, amount):
        if self.min_bal > amount:
            self.min_bal -= amount
            print("your account", self.ac_no, "has been debited with an amount of", amount, "on", datetime.today(),
                  "remaining balance is", self.min_bal)
        else:
            print("trasaction failed due to insufficinet balance")

    def bal_enq(self):
        print(self.min_bal)


obj = Bank(10010101, "jyo", 3000, "SBI")
obj.withdraw(90000)
obj.deposit(1000)
