'''
Product of Array Except Self (TCS Digital / Infosys)Sawaal: 
Ek list di hai numbers ki. Aapko ek naye list return karni hai jisme
har index par jo value ho, wo baaki saare numbers ka guna (product) ho,
par us khud ke index wale number ko chhod kar. Interviewer bolega:
Division (/) operator ka use nahi karna hai!Example: [1, 2, 3, 4]
$\rightarrow$ Output: [24, 12, 8, 6](Index 0 par: 
$2 \times 3 \times 4 = 24$.
Index 1 par: $1 \times 3 \times 4 = 12$)

'''

# def except_self_product(l):
#     res=[-1]*len(l)
#     left_product=1
#     for i in range(len(l)):
#         res[i]=left_product
#         left_product=left_product*l[i]
#     right_product=1
#     for j in range(len(l)-1,-1,-1):
#         res[j]=right_product*res[j]
#         right_product=right_product*l[j]
#     return res


# user=eval(input("enter your list"))
# result=except_self_product(user)
# print(result)







'''
Ek list di hai numbers ki, aapko bina kisi min() ya max() function ke,
manually loop chala kar sabse chota aur sabse bada number dhoodhna hai.
Example: [7, 2, 1, 9, 5] $\rightarrow$ Output: Smallest = 1, Largest = 9.
'''

# def greatest_smallest(l):
#     greatest=None
#     smallest=None
#     for i in l:
#         if greatest is None or i>greatest:
#             greatest=i
#         if smallest is None or i<smallest:
#             smallest=i
#     return smallest,greatest

# user=eval(input("enter your list"))
# result=greatest_smallest(user)
# print(result)





'''
Count the Elements Greater Than Their Left Neighbors (TCS NQT Real Question)

'''
# def count_greater_left_neighbour(l):
#     count=0
#     for i in range(1,len(l)):
#         if l[i]>l[i-1]:
#             count=count+1
#     return count

# user=eval(input("eter your list"))
# result=count_greater_left_neighbour(user)
# print(result)







'''
Ek list di hai. Aapko wo saare elements dhoodhne hain jo apne daayein
(right) taraf ke saare elements se bade ya barabar hon. List ka jo sabse 
akhri element hota hai, wo hamesha ek "Leader" hota hai kyunki uske right
mein koi nahi hota.
Real Example: [16, 17, 4, 3, 5, 2] $\rightarrow$ Output: [17, 5, 2]
'''


# def find_leaders(l):
#     leader=[]

#     max_so_far=l[-1]
#     for i in range(len(l)-2,-1,-1):
#         if l[i]>max_so_far:
#             max_so_far=l[i]
#             leader.insert(0,l[i])
#     leader.append(l[-1])
#     return leader

# user=eval(input("enter your list"))
# result=find_leaders(user)
# print(result)






'''
Do strings diye hain (jaise "listen" aur "silent"). 
Aapko batana hai ki kya dono aapas mein Anagram hain?
Anagram ka matlab hota hai ki dono words mein ekdum same akshar hon aur barabar ginti mein hon,
bas aage-piche likhe hon.
Example: "cat" aur "act" $\rightarrow$ Output: True.
'''

# def check_anagram(s1,s2):
#     if len(s1)!=len(s2):
#         return f'anagram nahi ho sakta hai y to'
#     dict_1={}
#     dict_2={}
#     for i in dict_1:
#         if i in dict_1:
#             dict_1[i]=dict_1[i]+1
#         else:
#             dict_1[i]=1
    
#     for j in dict_2:
#         if i in dict_2:
#             dict_2[i]=dict_2[i]+1
#         else:
#             dict_2[i]=1
    
#     if dict_1==dict_2:
#         return True
#     else:
#         return False
    
           
# s1=input("enter your word")
# s2=input("enter your word")
# result=check_anagram(s1,s2)
# print(result)









'''
Ek list di hai numbers ki. Aapko wo number dhoodhna hai jo list mein
sabse zyada baar (maximum times) aaya hai.
Aapka Seedha Dimaag:
'''
# def most_frequesnt_elemnt(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     maximum=None
#     maximum_element=None
#     for j in d:
#         if maximum is None or d[j]>maximum:
#             maximum=d[j]
#             maximum_element=j
#     return maximum_element

# user=eval(input("enter your list"))
# result=most_frequesnt_elemnt(user)
# print(result)












'delete dublicate value'
# def delete_dublicate(l):
#     dublicate=[]
#     for i in l:
#         if i not in dublicate:
#             dublicate.append(i)
#     return dublicate
      

# user=eval(input('enter your list'))
# result=delete_dublicate(user)
# print(result)






