// object is equal to dictionary in python
//its like key value pair
//there is no doble quotes needed for keys
var employe={
    id:1000,name:"ajay",desig:"developer",salary:25000
}
//employee name
console.log(employe["name"]);
console.log(employe.name);
//search gender key in employe
console.log("gender" in employe);//false
//if its found return true else false

//add gender=male key value pair
employe["gender"]="male"
console.log(employe);

//to print all the keys in employe
for(let key in employe){ // in operator returns keys
    console.log(key);
}