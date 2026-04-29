'Check if list is palindrome '
# def find_pallindrom(l):
#     rev=l[::-1]
#     if l==rev:
#         return 'list is palindrom'
#     else:
#         return 'list not pallindrom'


# user=eval(input("enter your list"))
# result=find_pallindrom(user)
# print(result)








'Merge two lists '
# def merge_list(l1,l2):
#     return l1+l2




# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=merge_list(l1,l2)
# print(result)







 
'ek list lo list ka half reverse krwao phir jo bacha hua h usko jod do  '
'''
mene pehle devide krke half kr diya phir adhe ko loop lga k reverse kiya phir adhe ko append kr diya ho gya

'''
# def half_list_reverse(l):
#    rev=[]
#    length=len(l)//2
#    half_rev=l[0:length]
#    bachi_hui=l[length:]
#    for i in half_rev:
#       rev.insert(0,i)

#    for i in bachi_hui:
#       rev.append(i)
#    return rev

# user=eval(input('enter yoyr list'))
# result=half_list_reverse(user)
# print(result)




'Find pair with given sum '
# def find_pair(l,target):
#     pair=[]
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]+l[j]==target:
#                 pair.append((l[i],l[j]))
#     return pair



# l=eval(input("enter your list"))
# target=int(input("enter your number"))
# result=find_pair(l,target)
# print(result)




'Find maximum difference between elements '
# def find_maximum_diffrence(l):
#     maximum=None
#     minimum=None
#     for i in l:
#         if maximum is None or i >maximum:
#             maximum=i
#         if minimum is None or i<minimum:
#             minimum=i

#     maximum_diffrence=maximum-minimum
#     return maximum_diffrence

# user=eval(input("enter your list"))
# result=find_maximum_diffrence(user)
# print(result)

