class Bank:
    def bal_enq(self):
        print("inside balance enquiry")

    def withdraw(self):
        print("inside withdraw")

    def __deposit(self):  # this keep as private method by providing __,
        print("inside deposit")

class Atm(Bank):
    pass


atm=Atm()
atm.withdraw()
atm.bal_enq()
#atm.__deposit()


obj = Bank()
obj.withdraw()
obj.bal_enq()
#
obj._Bank__deposit()#private msg can be call by using this
