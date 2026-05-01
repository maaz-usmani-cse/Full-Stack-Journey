'''
Max Difference Between Adjacent Elements
Isme tumhe puri list ka max aur min nahi dekhna, balki sirf saath-saath (padosi) 
 numbers ka difference nikalna hai aur batana hai ki sabse bada antar kahan hai.
''' 

# def max_diffrence_between_adjacent_element(l):
#    maximum_diffrence=None
#    for i in range(len(l)-1):
#       diffrence=l[i+1]-l[i]
#       if maximum_diffrence is None or diffrence>maximum_diffrence:
#          maximum_diffrence=diffrence
#    return maximum_diffrence


# user=eval(input("enter your list"))
# result=max_diffrence_between_adjacent_element(user)
# print(result)
     



'''

Smallest Positive Difference
Jaise tumne "Maximum" difference nikala, waise hi ab tumhe sabse chota positive difference dhoondna hai do alag numbers ke beech mein.

Input: [1, 15, 3, 9, 10]

Output: 1 (Kyunki 9 aur 10 ke beech ka antar sabse kam hai).

'''

# def smallest_possitive_diffrence(l):
#     smallest_diff=None
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]>l[j]:
#                 dif=l[i]-l[j]
#             else:
#               dif=l[j]-l[i]
#             if dif>0:
#               if smallest_diff is None or dif<smallest_diff:
#                   smallest_diff=dif
#     return smallest_diff

# user=eval(input("enter your list"))
# result=smallest_possitive_diffrence(user)
# print(result)








