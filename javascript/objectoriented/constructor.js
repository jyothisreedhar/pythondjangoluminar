class Person{
    constructor(age,name){
        this.age=age;
        this.name=name;
    }
    printPerson(){
        console.log(this.age+","+this.name);
    }
}
//object
//referencename=className()
var obj=new Person(25,"ajay");

obj.printPerson()