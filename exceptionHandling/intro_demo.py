# exception can be handled by using a try statement
# exception means founding an abnormal situation
# try block===>doubtful code
# the critical operation which can raise an exception is placed inside the try clause
# the code that handles the exception is written in the except clause
# the errors are file not found error,zero division error
# the keywords are "try,"except","finally"


num1 = int(input("num1:"))#10
num2 = int(input("num2:"))#2,0
try:
    res = num1 / num2#10/2=5,10/0
    print("res=", res)
except Exception as e:
    print("exception occurred") 99
print("i have one database transaction")
print("i have file operation")
