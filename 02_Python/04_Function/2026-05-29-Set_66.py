'''

Tumhe ek numbers ki list di gayi hai. Tumhe us list ke saare 0 (zeroes) ko uthakar
ekdam aakhir (end) mein bhejna hai,
lekin baki saare numbers ka sequence (order) waisa ka waisa hi rehna chahiye!

'''

# def shif_zero(l):
#     pointer=0
#     for i in range(len(l)):
#         if l[i]!=0:
#            temp=l[pointer]
#            l[pointer]=l[i]
#            l[i]=temp

#            pointer=pointer+1
#     return l


# user=eval(input("enter your list"))
# result=shif_zero(user)
# print(result)




'''
Ek string di hai, aapko usme se wo pehla character dhoodhna hai jo
poori string mein sirf ek hi baar aaya ho.
Agar saare repeat ho rahe hain, toh return karo None.
Example: "swiss" -> Output: "w" (S char do baar aa chuka hai,
par w pehla aisa banda hai jo repeat nahi hua).
'''
# def find_unique_character(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in d:
#         if d[j]==1:
#             return j
#     return None


# user=input("enter your word")
# result=find_unique_character(user)
# print(result)






'''
Ek list di hai numbers ki, aapko wo number dhoodhna hai jo list mein
aadhi se zyada 
baar ($> N/2$) aaya ho. Maan lo aisa ek number list mein hamesha hoga.
Example: [3, 2, 3] -> Output: 3 (Kyunki list ki size 3 hai,
aur 3 do baar aaya hai, jo ki $3/2 = 1.5$ se zyada hai).
'''
# def majority_element(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in d:
#         if d[j]>len(l)//2:
#             return j
 

# user=eval(input("enter your list"))
# result=majority_element(user)
# print(result)




'''
Ek list di hai integers ki. Agar koi bhi value list mein kam se kam do baar
(duplicate) aayi hai toh True return karo, aur agar saare numbers 
unique hain toh False return karo.
Example: [1, 2, 3, 1] -> Output: True
'''

# def is_dublicate(l):
#     d={}
#     for i in l:
#         if i in d:
#             return True
#         else:
#             d[i]=1
#     return False


# user=eval(input("enter your list"))
# result=is_dublicate(user)
# print(result)
        




'''

Aapko do lists di gayi hain. Aapko unke beech ke common elements 
(jo dono mein hon) dhoodhne hain aur ek naye list mein return karna hai.
Repeat nahi hona chahiye elements output mein.
Example: list1 = [1, 2, 2, 1], list2 = [2, 2] -> Output: [2]

'''
# def intersection(l1,l2):
#     d={}
#     l=[]
#     for i in l1:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in l2:
#         if j in d:
#             l.append(j)
#             del d[j]
#     return l

# user1=eval(input("enter your list"))
# user2=eval(input("enter your list"))
# result=intersection(user1,user2)
# print(result)          


