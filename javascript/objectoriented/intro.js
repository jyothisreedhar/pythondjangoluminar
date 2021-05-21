//class-->blue print,design pattern
//object--.real world entity
//reference--

class Person{
    setPerson(age,name){//in python we use def keyword,but here no nead for function
        this.age=age;//use this instead of self
        this.name=name;
    }
    printPerson(){
        console.log(this.age+","+this.name);
    }
}
//object
//referencename=className()
var obj=new Person();//new is a keyword//we can use var,let to create refernce
obj.setPerson(25,"ajay")
obj.printPerson()
//instance variable this.age,this.name