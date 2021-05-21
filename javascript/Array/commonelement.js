//arr1=[10,20,30,40]
//arr2=[21,22,30,31,40]
//find the common elemnts btw two arrays
var arr1=[10,20,30,40]//o(n)
var arr2=[21,22,30,31,40]//o(n)
for(let i of arr1){
    for(let j of arr2){
        if(i==j){
            console.log(i);
        }
    }
}
//search
//var arr1=[10,20,30,40]//10
//        e1
//var arr2=[21,22,30,31,40]//21
//        e2
//e1==e2 ==>common elmnt  20==21 30==21 30==22 30==30 
//e1>e2  ==>10>21         21>21  30>21 pos(e2)+1 30>22 pos(e2)+1
//e1<e2  ==>10<21 =>pos(e1)+1 ,20<21 pos(e1)+1
var arr1=[10,20,30,40];
var arr2=[21,22,30,31,40];
var high1=arr1.length;
//console.log(high);
var high2=arr1.length;
console.log(high1,high2);
//let e1=arr1[];
//console.log(e1);