'''
Ek aisa function banao create_counter(), jo ek initial value le.
Iske andar ek aisa function hona chahiye jo jab bhi call ho,
toh purani value mein +1 karke return kare.
'''
# def counter(start_value):
#     counter=start_value
#     def increment():
#         nonlocal counter
#         counter=counter+1
#         return counter
#     return increment



# result=counter(10)
# print(result())
# print(result())










'Ek function banao jo list mein se sirf un Prime numbers ka sum nikalta ho jo 5 se bade hain.'
# def sum_of_prime_geraterthan5(l):
#     total=0
#     for i in l:
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 break
#         if i>5:
#             total=total+i
#     return total


# user=eval(input("enter your list"))
# result=sum_of_prime_geraterthan5(user)
# print(result)









' Ek generator banao jo 1 se lekar 10,000 tak ke saare numbers ka Square ($n^2$) nikalta ho.'

# squares_gen = (num ** 2 for num in range(1, 10001))

# for i in range(10):
#     print(next(squares_gen))
#     print(next(squares_gen))
   
   








'''

Maan lo tum Amazon ke warehouse database par kaam kar rahe ho jisme 10 lakh items hain.
Tumhe ek aisa function banana hai jo check kare ki kya pooray data mein koi 
bhi item 'DAMAGED' status ka hai. Efficiency ke liye tum kaunsa line of code select karoge?

'''
# item=['good','best']
# is_damaged=any('damaged'in item for i in item)
# print(is_damaged)












'''
Tum Flipkart ya Amazon ke backend engineer ho.
Tumhare paas ek lakh transactions (transactions) ki list aane wali hai. 
Har transaction ek dictionary hai, jaise: {"tx_id": 101, "amount": 5000, "status": "SUCCESS"}.
Tumhe manager ne bola hai ki security ke liye check karo ki kya poori list mein ek bhi transaction aisa hai jiska amount NEGATIVE (fraud) ho?

'''

# dictionary={"tx_id": 101, "amount": 5000, "status": "SUCCESS"}
# result=any(dictionary['amount']<0 for i in dictionary )
# print(result)








'''
Maan lo tumhare paas ek list hai aur tumhe sirf specific numbers/items alag nikalne hain.

Problem: Ek list se sirf Even Numbers (jo 2 se kat-te hain) nikaal kar nayi list banao.

'''


# user=eval(input("enter your list"))
# result=[i for i in user if i%2==0]
# print(result)







'logical question iska answr soch k btao???'

# result = [ (1, 2), {"name": "Maaz"}, {10, 20} ][1]["name"].upper()
# print(result)











'''

Ek Matrix (List of Lists) di gayi hai: matrix = 
[[1, 2], [3, 4], [5, 6]].
 Isko ek single list [1, 2, 3, 4, 5, 6]
mein convert karo sirf ek line mein.

'''

# def convert_single_list(l):
#     res=[j for i in l for j in i]
#     return res


# user=eval(input("enter your list"))
# result=convert_single_list(user)
# print(result)













'''
Ek list di hai users ki: users = [{"id": 1, "active": True}, {"id": 2, "active": False}, {"id": 3, "active": True}]. 
Sirf un users ki ID nikaalo jo Active hain.
'''
# def find_active_user(l):
#    res=[i['id']for i in l if 'active' in i and i['active']]
#    return res



# user=eval(input("enetr your list"))
# result=find_active_user(user)
# print(result)