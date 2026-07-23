'''

Conditional String Truncation

Task: Agar string ki length 5 se badi hai toh use pehle 5 characters tak kaat kar aage "..." lagana hai, warna string waisi hi rehne deni hai.

Input: sentences = ["hi", "development", "django", "ok"]

Expected Output: ["hi", "devel...", "djang...", "ok"]

'''

# def check_string_length(l):
#     res=[]
#     for i in l:
#         if len(i)>5:
#             cut=i[:5]+"..."
#             res.append(cut)
#         else:
#             res.append(i)
#     return res



# user=eval(input("enter your list"))
# result=check_string_length(user)
# print(result)









'''
Cumulative Max Tracker

Task: Number list se har point tak ka running maximum value (ab tak ka sabse bada number) nikal kar list banani hai.

Input: nums = [3, 1, 5, 2, 8, 4]

Expected Output: [3, 3, 5, 5, 8, 8]

'''

# def comulative_max_tracker(l):
#     res=[]
#     current_max=l[0]
#     for i in l:
#         if i>current_max:
#             current_max=i
#         res.append(current_max)
#     return res

# user=eval(input('enter your list'))
# result=comulative_max_tracker(user)
# print(result)
        







'''
Filter Prime Index Elements

Task: enumerate() ka use karke list se sirf un elements ko uthana hai jo Prime Number 
indices (yaani index 2, 3, 5, 7...) par baithe hain.

Input: arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']  (Indices 0 to 6)

Expected Output: ['c', 'd', 'f'] (Indices 2, 3, 5 par baithe elements)
'''

# def is_prime(n):
#     if n<=1:
#         return False
#     if n==2:
#         return True
#     if n%2==0:
#         return False
#     for i in range(3,int(n**0.5)+1,2):
#         if n%i==0:
#             return False
#     return True


# def filter_prime_index(l):
#     res=[]
#     for index,value in enumerate(l):
#         if is_prime(index):
#             res.append(value)
#     return res


# user=eval(input("enter your list"))
# result=filter_prime_index(user)
# print(result)










'''


Cross Product with Condition (Filtered Pairs)

Task: Do lists ka cartesian product banana hai lekin sirf un tuples ko rakhna hai jinka sum (jod) Even ho.

Input: l1 = [1, 2], l2 = [3, 4]

Expected Output: [(1, 3), (2, 4)] (Kyunki 1+3=4 aur 2+4=6)
'''


# def filter_get_even_sum_pairs(l1,l2):
#     res=[]
#     for i in l1:
#         for j in l2:
#             if (i+j)%2==0:
#                 res.append((i,j))
#     return res


# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=filter_get_even_sum_pairs(l1,l2)
# print(result)







'''

Swap First and Last Characters of Words

Task: Words ki list ke har string ke pehle aur aakhri letter ko aapas mein swap (palat) dena hai.

Input: words = ["code", "maaz", "python"]

Expected Output: ["eodc", "zaam", "nythop"]

'''

# def swap_first_last_char(l):
#     res=[]
#     for i in l:
#         first=i[0]
#         middle=i[1:len(i)-1]
#         last=i[-1]
#         swap=last+middle+first
#         res.append(swap)
#     return res


# user=eval(input("enter your list"))
# result=swap_first_last_char(user)
# print(result)
