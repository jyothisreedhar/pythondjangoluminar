//method overriding implemented in different class

class Parent{
    phone(){
        console.log("parent phone");
    }
}
class Child extends Parent{
    phone(){
        console.log("child phone");
    }

}
var ch=new Child()
ch.phone()

//class method
//new used for create an object
//this ==>point instance variable
//--init--==constructor
//extends==>used for inheritance
//es6==ECMA standerd
 /* 1.arrow function==lambda function
  2.map()
  3.filter()
  4.reduce()
  5.sort()*/