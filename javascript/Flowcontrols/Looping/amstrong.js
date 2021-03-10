var num=153;
let res=0;
let temp=num;
while(num>0){
    digit=num%10;
    res=res+digit**3;
    num=num/10;
}
if(num==res){
    console.log(num,"is an amstrong number");
}
else{
    console.log(num,"is not an amstrong number");
}
console.log(res);