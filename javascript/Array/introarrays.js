//instead of list here we use arrays
//insertion order preserved
//duplicates allowed
//indexing
//homogenious and hetrogenious data
var data=[10,"hello",true,105,10.89]
console.log(data);
var num=[10,20,30,40,50]
console.log(num[2]);

//iterate element in an array
for(let number of num){
    console.log(number);
}

//add element in an arrays
num.push(100);
console.log(num);

//delete element in array
num.pop()
console.log(num);
//pop delete last element in an array