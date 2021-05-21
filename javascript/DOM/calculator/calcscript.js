
function displayBox(num){
    var disp=document.querySelector(".display")
disp.value+=num
}

function result(){
    var disp=document.querySelector(".display").value;
var out=eval(disp)
document.querySelector(".display").value=out  
}

function del(){
    var disp=document.querySelector(".display").value;
    var data=disp.slice(0,-1)
    document.querySelector(".display").value=data  

}
