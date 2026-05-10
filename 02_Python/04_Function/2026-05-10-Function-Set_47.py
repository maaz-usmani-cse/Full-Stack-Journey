'''
Batao ki kya list mein koi bhi number repeat ho raha hai? (Sirf True ya False mein jawab do).

Input: [1, 2, 3, 4, 2]
'''

# def repeat_check(l):
#     for i in l:
#           count=0
#           for j in l:
#              if i==j:
#                  count=count+1
#           if count>1:
#               return True
#     return False

# user=eval(input("enter your list"))
# result=repeat_check(user)
# print(result)    
            




'''
Saare negative numbers ko list ki shuruat mein lao bina nayi list banaye (Swapping use karke).

Input: [1, -2, 3, -4, 5]

Output: [-2, -4, 3, 1, 5]

'''

# def swap_negative_number(l):
#     index=0
#     for i in range(len(l)):
#         if l[i]<0:
#           temp = l[i]    
#           l[i] = l[index]  
#           l[index] = temp
#           index=index+1

#     return l



# user=eval(input("enter your list"))
# result=swap_negative_number(user)
# print(result)






'''
Find the Average of Positive NumbersSawal: Sirf positive numbers ka Average (Ausat) nikalna hai.
Input: [10, -5, 20, -2, 30]Output: 20.0 ($(10+20+30) / 3$)
'''
# def average_of_possitive_number(l):
#     count=0
#     total=0
#     for i in l:
#         if i>0:
#             count=count+1
#             total=total+i
#     averag=total/count
#     return averag

# user=eval(input("enter your list"))
# result=average_of_possitive_number(user)
# print(result)







'''
List mein sabse chota number kitni baar aaya hai, wo gino.

Input: [2, 5, 2, 8, 2, 10]

Output: 3
# '''
# def count_smallest_element(l):
#     smallest=None
#     smallest_count=0
#     for i in l:
#         if smallest is None or i<smallest:
#             smallest=i
#     for j in l:
#         if smallest==j:
#            smallest_count=smallest_count+1

#     return smallest_count

# user=eval(input("enter your list"))
# result=count_smallest_element(user)
# print(result)








'''
Batao ki kya di gayi list pehle se hi sorted (badhte kram mein) hai ya nahi? (True ya False).

Input: [1, 5, 10, 20] -> True | [1, 10, 5, 20] -> False

# '''
# def check_sorted(l):
#     for i in range(len(l)-1):
#         if l[i]>l[i+1]:
#             return False
#     return True

# user=eval(input("enter your list"))
# result=check_sorted(user)
# print(result)




