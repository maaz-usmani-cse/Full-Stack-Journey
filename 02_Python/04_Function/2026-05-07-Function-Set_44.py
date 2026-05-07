'''
Filter Odd Squares: Ek numbers ki list di gayi hai. Pehle sabka square karo, phir sirf unhe filter karo jo Odd (visham) numbers hain.

Input: [1, 2, 3, 4, 5, 6]

Output: [1, 9, 25]
'''
# s=[1, 2, 3, 4, 5, 6]
# square=list(map(lambda x: x**2,s))
# odd=list(filter(lambda x: x%2!=0,square))
# print(odd)




'''
Ek names ki list mein se sirf wahi names filter karo jinki length 4 characters se kam hai.

Input: ["Maaz", "Abhi", "Jay", "Alok", "Om"]

Output: ["Jay", "Om"]
'''

# li=["Maaz", "Abhi", "Jay", "Alok", "Om"]
# result=list(filter(lambda x: len(x)<4,li))
# print(result)





'''
Ek list mein positive, negative aur zero mix hain. Sirf Positive numbers (greater than 0) filter karke dikhao.

Input: [10, -5, 0, 20, -1, 3]

'''
# l=[10, -5, 0, 20, -1, 3]
# result=list(filter(lambda x:x>0,l))
# print(result)







'''
Valid Mobile Numbers: Ek list mein phone numbers hain (kuch string, kuch int).
 Sirf wo numbers filter karo jo exactly 10 digits ke hain.
Hint: Pehle str() mein convert karna pad sakta hai.
'''
# li=[9430661054,542154,7324886683,'541235','9006221453']
# result=list(filter(lambda x: len(str(x))==10, li))
# print(result)





'''
Find the "Leader" in the List
Sawal: Ek number "Leader" tab hota hai jab uske right side ke saare numbers usse chhote hon. Saare Leaders dhoondho.

Input: [16, 17, 4, 3, 5, 2]

Output: [17, 5, 2]

'''
# def find_leader(l):
#     leader=[]
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]<l[j]:
#                 break
#         else:
#             leader.append(l[i])
#     return leader

# user=eval(input("enter your list"))
# result=find_leader(user)
# print(result)    






'''
Ek list mein sirf 0 aur 1 hain. Saare zeros ko shuruat mein aur saare ones ko aakhir mein lao bina sort kiye.
Input: [0, 1, 0, 1, 1, 0]
Output: [0, 0, 0, 1, 1, 1]
'''

# def oneside_zero_oneside_1(l):
#     li=[]
#     for i in l:
#         if i==0:
#             li.insert(0,i)
#         else:
#             li.append(i)
#     return li
# user=eval(input("enter your list"))
# result=oneside_zero_oneside_1(user)
# print(result)






'''
Wo number dhoondho jo list mein aadhe se zyada baar aaya hai.

Input: [3, 3, 4, 2, 4, 4, 2, 4, 4] (Total 9 elements hain, toh jo 5+ baar aaya ho)

Output: 4

'''
# def count_number(l):
#     res=None
#     list_length=len(l)//2
#     for i in l:
#         count=0
#         for j in l:
#             if i==j:
#                 count=count+1
#         if count>list_length:
#             res=i
#             break
#     return res

# user=eval(input("enter your list"))
# result=count_number(user)
# print(result)














