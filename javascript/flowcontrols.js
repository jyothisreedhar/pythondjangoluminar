var num=8;
if (num<0){
    console.log("-ve");
}
else if(num>0){
    console.log("+ve");
}
else{
    console.log("zero");
}
//read a number if num is divisible by 3 print fizz
//if num is divisible by 5 print buz
//if divisible by 15 print fizbuz
var num=15;
if (num%15==0) {
    console.log("fiz buzz");
}
if (num%5==0){
    console.log("buzz");
}
else if (num%3==0){
    console.log("finzz");
}