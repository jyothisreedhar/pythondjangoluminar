var num1=20;
var num2=30;
var num3=40;
if((num1 > num2)&(num1 > num3)){
    console.log("num1 is large");
}
else if((num2 > num1)&(num2 > num3)){
    console.log("num2 is large");
}
else if((num3 > num1)&(num3 > num2)){
    console.log("num3 is large");
}

else if((num1 == num2)&(num1 == num3)){
    console.log("3 numbers are equal");
}