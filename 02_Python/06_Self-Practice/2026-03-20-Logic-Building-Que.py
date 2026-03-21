'LUHN ALGORITHM'
user=input("enter your number")
rev=user[::-1]
odd=rev[1::2]
even=user[0::-2]
total=0
for i in even:
    total=total+int(i)
for i in odd:
    digit=int(i)*2
    if digit>9:
      digit=digit-9
    else:
        total=total+multiply
if total%10==0:
    print("LUHN ALGORITHM HAI")
else:
    print("NAHI HAI LUHN ALGORITHM")
