employe = {id: 100,ename:"ajay",exp: 2, salary: 35000}
//employe salary
console.log(employe.salary);
//employe name
console.log(employe["ename"]);

//if employe salary <35000 add 5000rs more
if ((employe["salary"]) <= 35000) {
    ((employe["salary"])+=5000)
}
console.log(employe);

//id of employe
console.log(employe.id);
//check for bonous if not found add it
console.log("bonous" in employe);
employe["bonous"]=5000
console.log(employe);
