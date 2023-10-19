from mail import *
import secrets
email=input("enter the receiver's email address: ")
# Generate a random OTP
def generate_otp():
    # Generate a random 6-digit OTP
    return ''.join(secrets.choice("0123456789") for _ in range(6))

generated_otp=generate_otp()

sendMail(email,generated_otp)

enterOTP=input("enter the otp received ")
verifyMail(enterOTP,generated_otp)
if verifyMail(enterOTP,generated_otp):
    print("email verified!")
else:
    print("not verified!")