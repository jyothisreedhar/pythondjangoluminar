class Employe{
    constructor(eid,name,salary,desig){
        this.eid=eid;
        this.name=name;
        this.salary=salary;
        this.desig=desig;   
    }
    printDetails=()=>{
        console.log(this.eid+this.name+this.salary+this.desig);
    }                                                                                          
}
var employe=[]
var obj1=new Employe(100,"varun",25000,"developer")
var obj2=new Employe(101,"arun",22000,"developer")
var obj3=new Employe(102,"tarun",23000,"qa")
var obj4=new Employe(103,"karun",27000,"qa")
employe.push(obj1)
employe.push(obj2)
employe.push(obj3)
employe.push(obj4)
//print all employe designation
employe.forEach(emp =>console.log(emp.desig))

//add bonous 2000 to all employe
employe.map(emp=>emp.salary+2000).forEach(salary=>console.log(salary))

//convert all the employe names in uppercase
employe.map(emp=>emp.name.toUpperCase()).forEach(name=>console.log(name))

//print employe names
names=employe.map(emp=>emp.name)
console.log(names);

//find the details of employes whose designation is developers
employe.filter(emp=>emp.desig=="developer").forEach(emp=>console.log(emp))

//sort employe based on their salary
employe.sort((ob1,ob2)=>ob1.salary>ob2.salary?1:-1).forEach(emp=>console.log(emp))
    
//which employ gaining highest salary
const salary=employe.map(obj=>obj.salary).reduce((salary1,salary2)=>salary1>salary2?salary1:salary2)
console.log(salary);




