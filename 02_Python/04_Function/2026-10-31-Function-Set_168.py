'''
Ek list ke andar multiple dictionaries hain (jaise students ka data), 
unko unke 'marks' ya 'age' ke hisaab se sort karo. Yeh bohot zyada pucha jata hai.
'''
# def quick_sort_by_marks(l):
#     if len(l)<=1:
#         return l
#     pivot=l[0]
#     left=[]
#     middle=[]
#     right=[]
#     for i in l:
#         if i['marks']<pivot['marks']:
#             left.append(i)

#         elif i['marks']==pivot['marks']:
#             middle.append(i)

#         else:
#             right.append(i)

#     return quick_sort_by_marks(left) + middle + quick_sort_by_marks(right)


# user=eval(input("enter your list"))
# result=quick_sort_by_marks(user)
# print(result)   



'Move All Zeros to End'
# def move_zeros_to_end(l):
#     position=0
#     for i in range(len(l)):
#         if l[i]!=0:
#             temp=l[i]
#             l[i]=l[position]
#             l[position]=temp
#             position+=1
#     return l

# user=eval(input("enter your list"))
# result=move_zeros_to_end(user)
# print(result)
            



'''
Ek aisi list di hai jisme sirf 0, 1, aur 2 hain. 
Isko bina sort() function use kiye linear time mein sort karo. 
(Yeh bohot famous interview question hai).

'''
# def sort_color(l):
#     low=0
#     mid=0
#     high=len(l)-1

#     while mid<=high:
#         if l[mid]==0:
#             temp=l[low]
#             l[low]=l[mid]
#             l[mid]=temp

#             low+=1
#             mid+=1

#         elif l[mid]==1:
#             mid+=1

#         else:
#             temp=l[mid]
#             l[mid]=l[high]
#             l[high]=temp

#             high-=1
#     return l

# user=eval(input("enter your list"))
# result=sort_color(user)
# print(result)



'''
List mein even aur odd numbers mixed hain. Aise sort karo ki saare even numbers pehle aayein (ascending order mein) aur saare odd numbers baad mein aayein.
'''

# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l
#     pivot=l[0]
#     left=[]
#     middle=[]
#     right=[]
#     for i in l:
#         if i<pivot:
#             left.append(i)
#         elif i==pivot:
#             middle.append(i)
#         else:
#             right.append(i)
#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)

# def sort_even_odd(l):
#     even=[]
#     odd=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)

#     res_even=quick_sort_pivot(even)
#     res_odd=quick_sort_pivot(odd)
#     return  res_even+res_odd



# user=eval(input("enter your list"))
# result=sort_even_odd(user)
# print(result)




'Ek string ko bina slicing ke ulta (reverse) karne ka function likho.'
# def rev_string(s):
#     res=''
#     for i in s:
#         res=i+res
#     return res

# user=input("enter your res")
# result=rev_string(user)
# print(result)




'Ek list mein kaun-kaun se elements repeat ho rahe hain, unki list nikalo.'
# def find_dublicates(l):
#     res=[]
#     d={}
#     for i in l:
#         if i in d and i not in res:
#             res.append(i)
#         else:
#             d[i]=True
#     return res

# user=eval(input("enter your list"))
# result=find_dublicates(user)
# print(result)




'Check karo ki koi string ya number palindrome hai ya nahi.'
# def is_pallindrom(p):
#     res=''
#     for i in p:
#         res=i+res
#     if res==p:
#         return f"{p} pallindrom hai"
#     return f"{p} palindrom nahi hai"

# user=input("enter your word")
# result=is_pallindrom(user)
# print(result)



'Do lists mein jo elements common hain, unhe find karo.'
# def common_element(l1,l2):
#     res=[]
#     for i in l1:
#         if i in l2 and i not in res:
#             res.append(i)
#     return res

# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=common_element(l1,l2)
# print(result)
        

'List se duplicates hatao lekin original order kharab nahi hona chahiye'
# def remove_dublicate(l):
#     res=[]
#     for i in l:
#         if i not in res:
#             res.append(i)
#     return res

# user=eval(input("enter your list"))
# result=remove_dublicate(user)
# print(result)

