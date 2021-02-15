# withdrwal,deposit,balance enquiry,create acconut


from datetime import datetime


class bank:
    bank_name = "SBI"

    def __init__(self, acnt_num, person_name, min_balance):
        self.person_name = person_name
        self.acnt_num = acnt_num
        self.balance = min_balance
        # self.bank_name = bank_name

    def deposit(self, amount):
        self.balance += amount
        print(bank.bank_name, "your account", self.acnt_num, "has been credited with amount", amount, "on",
              datetime.today(),
              "avail bal", self.balance)

    def withdrwal(self, amount):
        if self.balance > amount:  # 30000>10000(f)
            self.balance -= amount
            print("your account", self.acnt_num, "has been debited with amount", amount, "on", datetime.today(),
                  "avail bal", self.balance)
        else:
            print("transaction cancelled with error code")

    def balance(self):
        print(self.balance)


obj = bank("jyothi", 100011010, 3000)
# obj.create_acnt("jyothi",100011010,3000)
# obj.withdrwal(1000)
obj.deposit(5000)
obj1 = bank("vijay", 18932267, 9000)
# obj1.create_acnt("vijay",18932267,9000)
obj1.withdrwal(5000)
obj2 = bank("jay", 189322674, 8000)
# obj2.create_acnt("jay",189322674,8000)
obj2.withdrwal(10000)
# different types of variables are
# instance variable & stataic variable or class variable
