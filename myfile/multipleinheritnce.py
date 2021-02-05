class Parent:
    #def m1(self):
        #print("inside parent")
        pass

    #def n1(self):
       # print("hai")

    #def n2(self):

       # print("hello")

   # def n3(self):
       # print("hihii")


class Child:
    def m1(self):
        print("inside child")


class SubChild(Parent,Child):
    def m3(self):
        print("inside subchild")


obj = SubChild()
obj.m3()
obj.m1()
#obj.m2()
#obj.n2()
