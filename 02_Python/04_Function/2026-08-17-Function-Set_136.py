'''
Number Group to Range Format

Task: Sorted integers ki list mein se continuous numbers ke groups banao aur range string return karo.

Input: nums = [1, 2, 3, 5, 6, 8, 9, 10]

Expected Output: ["1->3", "5->6", "8->10"]

'''
# def number_group_range_format(l):
#     res=[]
#     start=l[0]

#     for i in range(len(l)-1):
#         if l[i+1]==l[i]+1:
#             pass

#         else:
#             end=l[i]
#             res.append(f'{start}-->{end}')
#             start=l[i+1]
#     res.append(f'{start}->{l[-1]}')
#     return res


# user=eval(input("enter your list"))
# result=number_group_range_format(user)
# print(result)




 


'4 list m se common element nikalo'
# def common_element(l1,l2,l3,l4):
#     d1={}
#     d2={}
#     d3={}
#     res=[]
#     for i in l1:
#         d1[i]=True
#     for j in l2:
#         if j in d1:
#             d2[j]=True
          
#     for k in l3:
#         if k in d2:
#             d3[k]=True

#     for l in l4:
#         if l in d3:
#             res.append(l)
#             del d3[l]

#     return res



# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# l3=eval(input("enter your list"))
# l4=eval(input("enter your list"))

# result=common_element(l1,l2,l3,l4)
# print(result)







'''
Students ke marks ki dictionary mein se us student ka naam aur score return karo jiske sabse zyada marks hain.

Input: scores = {'Amit': 85, 'Rahul': 92, 'Pooja': 78, 'Neha': 95}

Expected Output: ('Neha', 95)

 '''
# def highest_mark_student(d):
#     marks=None
#     name=''
#     for i in d:
#         if marks is None or  d[i]>marks:
#             marks=d[i]
#             name=i
#     return (name,marks)


# user=eval(input("enter your list"))
# result=highest_mark_student(user)
# print(result)



        

    

'''
Words ki list di gayi hai. Unhe unki length (characters count) ke hisaab se group karke dictionary mein return karo.

Input: words = ["cat", "dog", "apple", "bat", "mango", "ox"]

Expected Output: {3: ['cat', 'dog', 'bat'], 5: ['apple', 'mango'], 2: ['ox']}

'''
# def length_accordind_filter(l):
#     res={}
#     for i in l:
#        if len(i) not in res:
#            res[len(i)]=[]

#        res[len(i)].append(i)

#     return res


# user=eval(input("enter your list"))
# result=length_accordind_filter(user)
# print(result)







'''
*****
 ****
  ***
   **
    *
   **
  ***
 ****
*****
'''

# n = int(input('entere any number : '))
# i = 0
# while i < n :
#     print( '*'*(n-i))
#     i = i+1
# i = n-2
# while i >= 0 :
#     print( '*'*(n-i))
#     i = i-1



