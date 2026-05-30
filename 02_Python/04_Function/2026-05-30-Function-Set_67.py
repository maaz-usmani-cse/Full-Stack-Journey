'''
Ek list di hai numbers ki, aapko wo pehla number dhoodhna hai jo list mein ek se zyada baar (repeat) aaya ho aur uski
occurrence sabse pehle hui ho.
Example: [10, 5, 3, 4, 3, 5, 6] -> 
Output: 5 (Kyunki 5 aur 3 dono repeat ho rahe hain,
par 5 index 1 par hi aa gaya tha, jo ki 3 ke index 2 se pehle hai).

'''

# def first_repeating(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in l:
#         if d[j]>1:
#             return f'first repaeting is {j}'

# user=eval(input("enter your list"))
# result=first_repeating(user)
# print(result)
    





'''
Ek list di hai, aapko ek aisa logic banana hai jo har number ko uske
count ke sath alag-alag jod de, ya fir bataye ki kaun kitni baar aaya hai'
bina kisi inbuilt counter ke.
Example: [1, 2, 1, 3, 2, 1] -> Output:  {1: 3, 2: 2, 3: 1}'''

# def frequency_count(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d

# user=input("enter your number")
# result=frequency_count(user)
# print(result)







'''
Aapko ek list di hai jisme 1 se lekar N tak ke numbers hone chahiye the,
par usme se ek number missing (gayab) hai. List un-sorted ho sakti hai.
Aapko wo missing number dhoodhna hai dictionary ka use karke.
Example: nums = [3, 0, 1] (Yahan size 3 hai, toh range 0 se 3 honi chahiye.
Missing kya hai? 2).

'''

# def finfd_missing_numbr(l):
#     d={}
#     for i in l:
#         d[i]=True
#     for i in range(len(l)+1):
#         if i not in d:
#             return f'missing number is {i}'
        
# user=eval(input("enetr your list"))
# result=finfd_missing_numbr(user)
# print(result)









'''
Do lists di gayi hain. Aapko un saare elements ka sum 
(jod) nikalna hai
jo dono lists mein common nahi hain
(yani jo unique hain dono ko mila kar).
Example: l1 = [1, 2, 3], l2 = [2, 3, 4] ->
Common kya hai? 2 aur 3. Non-common kya bacha?
1 aur 4. Sum = $1 + 4 = 5$.
'''
# def sum_of_non_common(l1,l2):
#     d={}
#     total=0
#     for i in l1:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in l2:
#         if j in d:
#             d[j]=d[j]+1
#         else:
#             d[j]=1
#     for key in d:
#         if d[key]==1:
#             total=total+key
#     return total

# l1=eval(input("enter your list"))        
# l2=eval(input("enter your list"))
# result=sum_of_non_common(l1,l2)
# print(result)
        






'''
Ek list di hai. Aapko check karna hai ki kya har
element ka count (frequency) unique hai ya nahi? 
Matlab aisa na ho ki do alag numbers se same
baar aaye hon.Example: [1, 2, 2, 1, 1, 3]

'''
# def is_check_count_unique(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     frequency_check={}
#     for key in d:
#         if d[key] in frequency_check:
#             return False, f'ye to kis number ki a chuki h'
#         else:
#           frequency_check[d[key]]=True
#     return True


# user=eval(input("enter your list"))
# result=is_check_count_unique(user)
# print(result)




