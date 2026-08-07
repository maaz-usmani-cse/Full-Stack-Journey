'Find all pairs having same digit sum '

# def get_digit_sum(n):
#     total=0
#     while n>0:
#         total=total+(n%10)
#         n=n//10
#     return total



# def group_pairs_digit_sum(l):
#     res={}
#     pair=[]
#     for i in l:
#         d_sum=get_digit_sum(i)
#         if d_sum in res:
#             for j in res[d_sum]:
#                 pair.append((j,i))

#             res[d_sum].append(i)
#         else:
#             res[d_sum]=[i]
#     return pair



# user=eval(input("enter your list"))
# result=group_pairs_digit_sum(user)
# print(result)

       




'Find longest increasing sequence in array'
# def longest_consecuitive_seq(l):
#     current=1
#     longest=1
#     for i in range(len(l)-1):
#         if l[i+1]>l[i]:
#             current=current+1
#         else:
#             if current>longest:
#                 longest=current
#     if current>longest:
#         longest=current

#     return longest

# user=eval(input("enter your list"))
# result=longest_consecuitive_seq(user)
# print(result)







'''
Ek 2D matrix ko 1D list mein flatten karo, lekin sirf wahi numbers include karo jo even hain aur 5 se bade hain.

Input: matrix = [[1, 8, 3], [4, 10, 6], [7, 2, 12]]

Expected Output: [8, 10, 6, 12]

'''

# def flatten_1d(l):
#     return[j for i in l for j in i if j>5 and j%2==0]


# user=eval(input("enter your list"))
# result=flatten_1d(user)
# print(result)






'''

Conditional Transformation (if-else in Comprehension)Task:
Words ki list se ek nayi list banao:Agar word ki length $> 3$ hai, 
toh use UPPERCASE mein convert karo.Agar length $\le 3$ hai, toh use reverse kar do.Input: words \
= ["cat", "python", "code", "ai", "developer"]Expected Output: ['tac', 'PYTHON', 'CODE', 'ia', 'DEVELOPER']

'''
# def filter_new_list(l):
#     return [ i.upper() if len(i)>3 else i[::-1] for i in l ] 


# user=eval(input("enter your list"))
# result=filter_new_list(user)
# print(result)






'''
Kisi bhi $M \times N$ matrix ka transpose ($N \times M$) nikaalo using nested list 
comprehension.Input: grid = [[1, 2, 3], [4, 5, 6]]Expected Output: [[1, 4], [2, 5], [3, 6]]

'''
# def transpose(l):
#     return[[l[i][j]for i in range(len(l))] for j in range(len(l[0]))]



# user=eval(input("enter your list"))
# result=transpose(user)
# print(result)