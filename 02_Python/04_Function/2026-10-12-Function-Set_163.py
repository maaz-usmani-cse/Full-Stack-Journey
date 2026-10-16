'Check karo ki string me saare vowels (a, e, i, o, u) maujood hain ya nahi'
# def is_all_vowels(s):
#     vowels='aeiou'
#     res=all(i in s for i in vowels)
#     return res

# user=input("enter your word")
# result=is_all_vowels(user)
# print(result)



'Check karo ki string me koi bhi digit nahi hai'
# def is_digit_in_string(s):
#     res=all(not i.isdigit() for i in s)
#     return res

# user=input("enyter your word")
# result=is_digit_in_string(user)
# print(result)

'Check karo kya string me kam se kam ek uppercase aur kam se kam ek digit hai'
# def is_uppercase_or_digit(s):
#     digit=any(i.isdigit()for i in s)
#     upper_case=any(i.isupper() for i in s)
#     return digit and upper_case

# user=input("enter your word")
# result=is_uppercase_or_digit(user)
# print(result)



'Check karo kya string ke saare letters alphabetical order me sorted hain'
# def is_sorted_alphabetical_order(s):
#     res=all(s[i]<=s[i+1] for i in range(len(s)-1))
#     return res

# user=input("enter your word")
# res=is_sorted_alphabetical_order(user)
# print(res)





'ATM PIN Try Limit (3 attempts wala logic)'
# correct_pin = 4321
# attempts = 3

# while attempts > 0:
#     entered_pin = int(input("Apna 4-digit PIN dalo: "))
    
#     if entered_pin == correct_pin:
#         print("Login Successful!")
#         break
#     else:
#         attempts -= 1
#         print(f"Galat PIN! {attempts} koshishein baaki hain.")
# if attempts==0:
#     print("Aapka account block ho gaya hai!")



'''
Ek phone ki battery 100% se shuru hoti hai. 
Jab tak battery 0% nahi ho jati, tab tak user YouTube chalata rehta hai aur har minute battery kam hoti hai. 
0% hone par "Phone Switched Off" print hona chahiye. (while battery > 0)

'''
# battery=100
# while battery>0:
#     print(f"battery:{battery} youtube chaliye")
#     battery-=1

# print('phone swich offed')




'''
Ek video load ho rahi hai. Jab tak percentage 100% nahi ho jata, 
tab tak loop chalega aur "Loading... X%" print karega. 100% hote hi "Playing Video" aa jayega.
'''

# def load_video():
#     percentage=0
#     while percentage<100:
#         print(f"loading..{percentage}")
#         percentage+=1
#     print('playing video')



'''
User se tab tak ek-ek karke item ka price puchte raho jab tak user
"done" ya "0" type na kar de. Aakhir mein sabhi items ka total bill print kar do.
'''

# def calculate_bill():
#     total_bill=0
#     while True:
#         user=input("Item ka price daalein (ya 'done' / '0' likhein band karne ke liye): ")

#         if user.lower()=='done' or user=='0':
#             break

#         try:
#             price=float(user)
#             if price<0:
#                 print('negative price nahi dijiye aaap')
#                 continue
#             total_bill=total_bill+price

#         except ValueError:
#             print('ek valid number ya DOne enter krey')

#     print(f"apka total bill:{total_bill}")


# calculate_bill()




