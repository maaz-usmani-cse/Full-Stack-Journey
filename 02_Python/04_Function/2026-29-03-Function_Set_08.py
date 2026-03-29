'dublicate item remove from list'
# def dublicate_remove(n):
#     l=[]
#     for i in n:
#         if i not in l:
#             l.append(i)
#     return l


# user=eval(input("enter your number"))
# result=dublicate_remove(user)
# print(result)



'dictiory me se key ko value aur value ko key bna ke dekhao'
# def key_value_exchange(n):
#     d={}
#     for i in n:
#         value=n[i]
#         d[value]=i
#     return d

# user=eval(input("enter your word"))
# result=key_value_exchange(user)
# print(result)



'ek function se count karke batao kitne Capital letters hain aur kitne Small.'
# def count_small_capital(n):
#     small_letter=0
#     capital_letter=0
#     for i in n:
#         if i.isalpha():
#             if i.islower():
#                 small_letter=small_letter+1
#             else:
#                capital_letter=capital_letter+1
#     return "small letter",small_letter,"capital letter", capital_letter

# user=input("enter ypour number")
# result=count_small_capital(user)
# print(result)




'''
ek function likho jo  ek nayi list return kare jisme har index par baaki saare numbers ka product (multiplication) ho.
Input: [1, 2, 3, 4]Output: [24, 12, 8, 6]  (Kyunki $2 \times 3 \times 4 = 24$, $1 \times 3 \times 4 = 12$, etc.)


'''


# def product_except_self(n):
 #     l=[]
#     for i in range(len(n)):
#         product=1
#         for j in range(len(n)):
#             if i!=j:
#                 product=product*n[j]
#         l.append(product)
#     return l

# user=eval(input("enter your number"))
# result=product_except_self(user)
# print(result)