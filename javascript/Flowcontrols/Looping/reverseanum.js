var num=321
var res=0
while(num>0){
    digit=num%10; //321%10=1
    res=res*10+digit; //0*10+1=1
    num=Math.floor(num/10);  
}
console.log(res);
