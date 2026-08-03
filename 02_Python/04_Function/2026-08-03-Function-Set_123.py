'Implement a program to find thefrequency of each element in an array.'

# def find_frequency(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d


# user=eval(input("enter your list"))
# result=find_frequency(user)
# print(result)





'''
Find First Repeating Character
Task: String mein sabse pehla aisa character dhoondho jo phir se repeat hua ho (jiski frequency 1 se zyada ho aur wo pehli baar repeat hote hi mil jaye).

Input: s = "geeksforgeeks"

Expected Output: {"char": "e", "index": 1}

(Explanation: 'e' character index 1 par pehli baar aaya jo aage chalkar repeat hota hai)

'''

# def find_first_repeating(s):
#     res={}
#     for i in range(len(s)):
#          if s[i] in res:
#             return {'char':s[i], 'Index':res[s[i]]}
#          else:
#              res[s[i]]=i


#     return f'koi v non repeating n mila'


# user=input("enter your word")
# result=find_first_repeating(user)
# print(result)





'''
Task: Array me se wo saare elements dhoondho jo sirf 1 baar aaye hain, unka value aur index as a dictionary list return karo.

Input: nums = [4, 5, 1, 2, 0, 4, 1]

Expected Output: [{"val": 5, "index": 1}, {"val": 2, "index": 3}, {"val": 0, "index": 4}]

'''


# def find_one_time_present_element(l):
#     res=[]
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1

#     for i in range(len(l)):
#         if d[l[i]]==1:
#             res.append({'Value':l[i], 'Index':i})

#     return res


# user=eval(input("enter your list"))
# result=find_one_time_present_element(user)
# print(result)







'. Implement a program to shift array elements to the left or right.'


# def list_shift(l,position):
#     position=position.lower()
#     if position=='right':
#         right=l[-1:]+l[:-1]
#         return right


#     elif position=='left':
#         left=l[1:]+l[:1]
#         return left

   


# user=eval(input("enter your list"))
# position=input('enter your positopn ? Left/Right')
# result=list_shift(user,position)
# print(result)




'Create a program to rotate an array. k time'

# def rotate_list(l,k,position):
#     k=k%len(l)
#     position=position.lower()

#     if position=='right':
#           right = l[-k:] + l[:-k]
#           return right

#     elif position=='left':
#          left=l[k:]+l[:k]
#          return left




# l=eval(input('enter your list'))
# k=int(input('enter your k number?'))
# position=input('enter your position? left/righ')
# result=rotate_list(l,k,position)
# print(result)







'Write a program to find themissing numberin a series.'
# def find_misssing_number(l):
#     res={}
#     for i in l:
#         res[i]=True

#     for i in range(1,len(l)+1):
#         if i not in res:
#             return f' missing number is: {i}'



# user=eval(input("enter your list"))
# result=find_misssing_number(user)
# print(result)



'. Implement a program to count positive and negative numbers in an array.'
# def count_possitive_negative_number(l):
#    possitive=0
#    negative=0
#    for i in l:
#       if i>0:
#          possitive=possitive+1
#       else:
#          negative=negative+1

#    return f'positive: {possitive}, Negative: {negative}'


# user=eval(input("enter your list"))
# result=count_possitive_negative_number(user)
# print(result)
      








'Write a program to check if two arrays are equal.'

# def is_two_list_equal(l1,l2):
#     if len(l1)!=len(l2):
#         return False

#     for i in range(len(l1)):
#         if l1[i] != l2[i]:
#             return False


#     return True

# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=is_two_list_equal(l1,l2)
# print(result)