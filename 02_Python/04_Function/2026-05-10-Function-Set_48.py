
# 'logic question'

# basket1={"apple",'banana',"cherry"}
# basket2={"banana","cherry","date"}
# print(basket1-basket2)






'''
Find the "Middle" Element(s)
Sawal: List ka beech wala element dhoondho. Agar list ki length even (sama) hai, toh dono beech wale elements dikhao.

Input: [1, 2, 3, 4, 5] -> 3 | [1, 2, 3, 4] -> 2, 3

'''

# def find_middle_element(l):
#     middle=len(l)//2
#     for i in l:
#         if l[middle]==l[i]:
#             return f'mddle element is:{l[i]}'
        

# user=eval(input("enter your list"))
# result=find_middle_element(user)
# print(result)    






'''
Ek list mein har number do baar aaya hai, lekin ek number aisa hai jo sirf ek hi baar aaya hai. Use dhoondho.

Input: [2, 4, 7, 2, 7]

Output: 4

'''
# def find_single_element(l):
#     res=[]
#     for i in l:
#         count=0
#         for j in l:
#             if i==j:
#                 count=count+1
#         if count==1:
#             res.append(i)
#     return res


# user=eval(input("enter your list"))
# result=find_single_element(user)
# print(result)








'''
 Check if Array is a Palindrome
Sawal: Batao ki kya list ko seedha padho ya ulta, wo ek jaisi hai?

Input: [1, 2, 3, 2, 1] -> True | [1, 2, 3] -> False
'''

# def check_list_pollindrom(l):
#     rev=[]
#     for i in l:
#         rev.insert(0,i)
#     if rev==l:
#         return True
#     else:
#         return False
    
# user=eval(input("enter your list"))
# result=check_list_pollindrom(user)
# print(result)









'''
List mein aise kitne numbers hain jo apne padosiyon (left aur right dono) se bade hain?

Input: [1, 3, 2, 4, 1]

Output: 2 (Kyunki 3, 1 aur 2 se bada hai; aur 4, 2 aur 1 se bada hai).

'''

# def count_element_gretaer_neighbour(l):
#     total=0
#     for i in range(len(l)):
#        if l[i]>l[i-1] and l[i+1]:
#            total=total+1
#     return total

# user=eval(input("enter your list"))
# result=count_element_gretaer_neighbour(user)
# print(result)








'''

Wo number dhoondho jo list mein sabse zyada baar aaya hai (Agar ek se zyada hain, toh koi bhi ek).

Input: [1, 3, 2, 3, 4, 1, 3]

Output: 3

'''
# def maximum_find(l):
#     maximum=None
#     for i in l:
#         count=0
#         for j in l:
#             if i==j:
#                 count=count+1
#         if maximum is None or count>maximum:
#             maximum=count
#     return f'sabse zyadh bar aya hai {maximum}'

# user=eval(input("enter your list"))
# result=maximum_find(user)
# print(result)




'''
List ke sirf pehle aadhe (first half) hisse ko ulta (reverse) kar do, baaki waisa hi rehne do.

Input: [1, 2, 3, 4, 5, 6]

Output: [3, 2, 1, 4, 5, 6]
'''

# def reverse_half_0f_list(l):
#     length=len(l)//2
#     temp=l[length:]
#     rev=l[length-1::-1]
#     result=rev+temp
#     return result

# user=eval(input("enter your list"))
# result=reverse_half_0f_list(user)
# print(result)







