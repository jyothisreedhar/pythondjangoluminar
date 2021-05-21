class Student{
    setStudent(rolno,name,course){
        this.rolno=rolno;
        this.name=name;
        this.course=course;
    }
    printStudent(){
        console.log(this.rolno+","+this.name+","+this.course);
    }
}
//object
//referencename=className()
var obj=new Student();
obj.setStudent(100,"ajay","mca")
obj.printStudent()
