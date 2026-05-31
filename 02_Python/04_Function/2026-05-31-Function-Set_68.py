'''
Ek list di hai jisme bade numbers hain. Aapko har number ke andar jaana hai,
aur uske jitne bhi Even digits (2, 4, 6, 8) hain, unko 0 se replace kar dena hai.
Odd digits ko nahi chhedna hai.
Example: [4532, 8917] $\rightarrow$ Output: 
[530, 917] (Dhyan se dekho: 4532 mein 4 aur 2 even the toh wo 0530 yani 530 
ban gaya. 8917 mein 8 even tha toh wo 0917 yani 917 ban gaya).

'''
# def replace_even_digit_in_list(l):
#     for i in range(len(l)):
#         original_num = l[i]
#         place = 1
#         res = 0
        
#         if original_num == 0:
#             l[i] = 0
#             continue
            
#         while original_num > 0:
#             digit = original_num % 10
#             if digit % 2 == 0:
#                 digit = 0
#             res = res + (digit * place)
#             place = place * 10
#             original_num = original_num // 10
            
#         l[i] = res
#     return l

# user = eval(input("enter your list: "))  
# result = replace_even_digit_in_list(user)
# print("Sahi Result:", result)
            




'''
:Ek numbers ki list di hai aur ek target sum diya hai. Aapko un do numbers ke
indices (positions) return karne hain jinko jodne par target mile.
Example: nums = [2, 7, 11, 15], target = 9 $\rightarrow$ Output: [0, 1]
(Kyunki $2 + 7 = 9$).

'''


# def sum_of_target_index(l,target):
#     d={}
#     for i in range(len(l)):
#         required=target-l[i]
#         if required in d:
#             return (d[required],i)
#         d[l[i]]=i


# user=eval(input("enter your list"))
# target=int(input("enter your target"))
# result=sum_of_target_index(user,target)
# print(result)




'''
Ek list di hai, use right side mein k baar rotate (aage khiskana) karna hai.
Jo elements aakhri se bahar nikal rahe hain, wo ghoom kar shuruat mein
aa jayenge.
Example: [1, 2, 3, 4, 5], k = 2
$\rightarrow$ Output: [4, 5, 1, 2, 3] (Aakhri ke do bande 4, 5
ghoom kar aage aa gaye).
'''

# def rotate_list(l,k):
#     k=k%len(l)
#     result=l[len(l)-k:]+l[:len(l)-k]
#     return result



# user=eval(input("enter your list"))
# k=int(input("enter your list"))
# result=rotate_list(user,k)
# print(result)







'find peak element find in list'
# def find_peak_element(l):
#     if l[0]>=l[1]:
#         return l[0]

#     for i in range(1,len(l)-1): 
#         if l[i]>=l[i+1] and l[i]>=l[i-1]:
#             return l[i]
#     if l[-1]>=l[-2]:
#         return l[i]


# user=eval(input("enter your list"))
# result=find_peak_element(user)
# print(result)
        




