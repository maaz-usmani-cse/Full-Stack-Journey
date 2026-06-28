'Find pair whose sum is closest to k '
# def find_pair_wos_sum_is_closed_to_k(l,k):
#     left=0
#     right=len(l)-1
#     min_diff=float('inf')
#     closest_pair=(None,None)
#     while left<right:
#         current_sum=l[left]+l[right]
#         diff=abs(current_sum-k)
#         if diff<min_diff:
#             min_diff=diff
#             closest_pair=(l[left],l[right])
#         if current_sum<k:
#             left=left+1
#         else:
#             right=right-1
#     return closest_pair

# user=eval(input("enter your list"))
# target=eval(input("enter your target number"))
# result=find_pair_wos_sum_is_closed_to_k(user,target)
# print(result)





'Find pair whose product is minimum'
# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l
#     pivot=l[0]
#     left=[]
#     middle=[]
#     right=[]
#     for i in l:
#         if i<pivot:
#             left.appebnd(i)
#         elif i==pivot:
#             middle.append(i)
#         else:
#             right.append(i)
#     return quick_sort_pivot(left)+middle+quick_sort_pivot(right)

# def find_pair_product_minimum(l):
#     res=quick_sort_pivot(l)
#     product1=res[0]*res[-1]
#     product2=res[0]*res[1]
#     if product1<product2:
#         return (res[0],res[-1])
#     else:
#         return (res[0],res[1])
    

# user=eval(input("enter your list"))
# result=find_pair_product_minimum(user)
# print(result)






'''
Strings ki Length nikalna
Aapko ek words ki list di gayi hai: words = ['apple', 'bat', 'orange', 'cat', 'banana']

Task: Ek nayi list banani hai jismein sirf un words ki length (aksharon ki sankhya) ho, 
jo 3 se bade hain.

Expected Output: [5, 6, 6]  (Kyunki 'bat' aur 'cat' ki length 3 hai, toh wo hat jayenge)
'''

# def word_length(l):
#     res=[len(i) for i in l if len(i)>3]
#     return res


# user=eval(input("enter your list"))
# result=word_length(user)
# print(result)







'''
Matrix ko Flat karna (Flattener)
Aapke paas ek 2D list (matrix) hai: matrix = [[1, 2], [3, 4], [5, 6]]

Task: Nested list comprehension ka use karke is 2D list ko ek single normal 
list mein convert karna hai.

Expected Output: [1, 2, 3, 4, 5, 6]

'''

# def convert_single_listr(l):
#     res=[j for i in l for j in i]
#     return res


# user=eval(input("enter your list"))
# result=convert_single_listr(user)
# print(result)







'''

If-Else ka Khel (Even/Odd Labelling)
Aapko ek list di gayi hai: nums = [1, 2, 3, 4, 5]

Task: List comprehension mein if-else ka use karke ek nayi list banani hai. 
Agar number even hai toh uski jagah string 'Even' aana chahiye, aur odd hai toh 'Odd'.

Expected Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

'''

# def even_odd(l):
#     res=['Even' if i%2==0 else 'Odd' for i in l]
#     return res


# user=eval(input("enter your list"))
# result=even_odd(user)
# print(result)








'''
Vowels (Swar) ko Hatana
Aapko ek string di gayi hai: text = "Python Programming"

Task: List comprehension ka use karke is string mein se saare vowels (a, e, i, o, u) ko gayab kar 
dena hai aur bache hue characters ki list banani hai.

Expected Output: ['P', 'y', 't', 'h', 'n', ' ', 'P', 'r', 'g', 'r', 'm', 'm', 'n', 'g']

Chalo bhai, ho jao shuru! Pehle wale se start karo, code likho aur mujhe batao, fir hum check karte hain.

'''

# def remove_vowels(s):
#     d={'a':True ,'e':True ,'i':True ,'o':True ,'u':True}
#     res=[i for i in s if i.lower()  not in d]
#     return res


# user=input("entr your word")
# result=remove_vowels(user)
# print(result)