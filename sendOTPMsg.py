from msg import *
code="+91"
number=code+input("enter phone number: ")

send(number)
otp=input("enter otp received: ")
verify(number,otp)