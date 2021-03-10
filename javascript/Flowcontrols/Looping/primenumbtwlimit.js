var low=10;
var up=50;
let flag=0;
for(let i=low;i<=up;i++){
    if (i>1) {
        flag=0
        for(let j=2;j<=i;j++){
            if(i%j==0){
                flag+=1
                break
            }
        }
        if(flag==0){
            console.log(i);
        }
    }
}