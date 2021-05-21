//console.log(localStorage.getItem("acntno"));
class Bank {
    static accountDetails() {
        let userData = {
            1000: { acno: 1000, password: "userone", balance: 9000 },
            1001: { acno: 1001, password: "usertwo", balance: 5000 },
            1002: { acno: 1002, password: "userthree", balance: 5000 }
        }
        return userData
    }
    static authenticate(acno, password) {//1003 userone
        var dataset = Bank.accountDetails()
        if (acno in dataset) {
            if (password == dataset[acno]["password"]) {
                //sucessful authentication
                return 1
            }

            else {
                //invalid password
                return 0
            }

        }
        else {
            //invalid accno
            return -1

        }
    }
    //static setStorage(acno,password){
        //localStorage.setItem("acntno",acntno)
       // localStorage.setItem("password",password)
    //
    static login() {

        var acno = document.querySelector("#acno").value
        var password = document.querySelector("#pwd").value
        let user = Bank.authenticate(acno, password)
        if (user == 0) {
            alert("invalid passsword")
        }
        else if (user == 1) {
            
            //alert("sucessful login")
            window.location.href="home.html"//redirect the homepage
            Bank.setStorage(acno,password)

        }
        else if (user == -1) {
            alert("invalid account numbet")
        }
    }
    static deposit() {
        var dataset=Bank.accountDetails()
        //alert(dataset)
        var acno = document.querySelector("#acno").value
        //alert(acno)
        var password = document.querySelector("#pwd").value
        //alert(password)
        var amount = document.querySelector("#amount").value
        //alert(amount)
        let user=Bank.authenticate(acno,password)
        //alert(user)
        
        if(user==0){
            //alert("invalid password")
        }
        else if(user==1){
            dataset[acno]["balance"]=dataset[acno]["balance"]+amount
            
            alert("amount succesfully added to the account available balance is "+dataset[acno]["balance"])
            
        }
        else if(user==-1){
            alert("invalid accountnumber")
        }


    }
    static withdraw(){
        
        
        var  dataset=Bank.accountDetails()
        //alert(dataset[acno]["balance"])
        var acno=document.querySelector("#acno").value
        //alert(acno)
        var password = document.querySelector("#pwd").value
        //alert(password)
        var amount = document.querySelector("#amount").value
        //alert(amount)
        let user=Bank.authenticate(acno,password)
        //alert(user)
        
        if(user==0){
             alert("invalid password")
        }
         else if(user==1){
             if(amount>dataset[acno]["balance"]){
                 alert("insufficient balance")
            }
            else{
                dataset[acno]["balance"]=dataset[acno]["balance"]-amount
                alert("amount is sucessfully withdrwan and remaining balance: "+dataset[acno]["balance"])
            }
        }
        
         else if(user==-1){
             alert("invalid accountnumber")
        }
       
    }
}