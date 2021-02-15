# create a bank account

from datetime import datetime


class bank:
    def create_acnt(self, acntno, pers_name, min_bal, bank_name):
        self.acntno = acntno
        self.pers_name = pers_name
        self.min_balance = min_bal
        self.bank_name = bank_name

    def deposit(self, amount):
        self.min_bal += amount
        print("your account", self.acntno, "has been credited with amount of", amount, "on", datetime.today(),
              "available balance is", self.min_balance)

    def withdrwal(self, amount):
        if self.min_balance > amount:
            self.min_balance -= amount
            print("your account", self.acntno, "has been debited with amount of", amount, "on", datetime.today(),
                  'available balance is', self.min_balance)
        else:

            print("transaction cancelled with error code")

    def balance(self):
        print(self.min_balance)


obj = bank()
obj.create_acnt(1000989, "siji", 5000, "SBI")
obj.withdrwal(1000)
