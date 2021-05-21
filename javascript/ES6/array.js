var arr=[10,20,30,40,50,11,12,13,41,42,43,45]
//squares
var squares=arr.map(no=>no**2)
console.log(squares);

//print array elemnt one by one
arr.forEach(num=>console.log(num))

//find cube of array elemnt and print one by one
arr.map((num)=>num**3).forEach(num=>console.log(num))

//extract all the even numbers and print
arr.filter(num=>num%2==0).forEach(num=>console.log(num))

//extract all the odd numbers and print
arr.filter(num=>num%2!=0).forEach(num=>console.log(num))

//sort the given array
//arr.sort((num1,num2)=>num1-num2).forEach(num=>console.log(num))
arr.sort((num1,num2)=>num1>num2?-1:1).forEach(num=>console.log(num))

//find the total of the given array
let num=arr.reduce((num1,num2)=>num1+num2)
console.log(num);

//find the lowest value
//python ternary operator==>num1 if num>num2 else num2
//javascript==num1>num2?num1:num2
let min=arr.reduce((num1,num2)=>num1<num2?num1:num2)
//here we use ternary operator
console.log(min);
