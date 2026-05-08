'''
Find the Second Largest Element

Sawal: List mein se dusra sabse bada number dhoondho.

Input: [12, 35, 1, 10, 34, 1]

Output: 34

Logic Hint: Do variables rakho, max1 aur max2. Har element ko dono se compare karo.

'''
# def second_largest(l):
#     fisrt=None
#     second=None
#     for i in l:
#         if fisrt is None or i>fisrt:
#             second=fisrt
#             fisrt=i
#         elif i!=fisrt and(second is None or i>second):
#             second=i
#     return f' first is {fisrt} second is {second}'

# user=eval(input("enter your list"))
# result=second_largest(user)
# print(result)






'''
st to Dict: Do lists hain keys = ['name', 'age'] aur values = 
['maaz', 20]. Inhe combine karke ek dictionary banao.
'''

# def combine_two_list(l1_key,l2_value):
#    res=dict(zip(l1_key,l2_value))
#    return res





# l1=eval(input("enter your list"))
# l2=eval(input("enetr your list"))
# result=combine_two_list(l1,l2)
# print(result)






'''
Frequency Counter: Ek string "aapne kya kiya bhai"
 mein har character kitni baar aaya hai,
 uska count dictionary mein dikhao.
'''

# def character_count(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d

# user=input("enter your list")
# result=character_count(user)
# print(result)







'Find maximum among negative numbers '
# def find_maximum_negative(l):
#     maximum_negative=None
#     for i in l:
#         if i<0:
#             if maximum_negative is None or i>maximum_negative:
#                 maximum_negative=i
#     return maximum_negative

# user=eval(input("enter your list"))
# result=find_maximum_negative(user)
# print(result)








'Find minimum among positive numbers '
# def minimum_among_positive_number(l):
#     minimum_among=None
#     for i in l:
#         if i>0:
#             if minimum_among is None or i<minimum_among:
#                 minimum_among=i
#     return minimum_among

# user=eval(input("enetr your list"))
# result=minimum_among_positive_number(user)
# print(result)







