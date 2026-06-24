'''
Absolute Difference Sort (Famous Interview Round)
Interviewer Bola: "Maaz, ek un-sorted list hai aur ek target number hai. 
Mujhe saare numbers ko unke absolute difference (bade me se chota minus) 
ke hisab se sort karke do."

Pattern Sequence:

Ek loop chalao aur har element ka target se difference nikal kar ek 
nayi list mein bharo (jaise abs(num - target)).

Apne wahi favorite Pivot Sort se un differences ko sort kar do!

Input: l = [10, 2, 8, 5, 6], target = 6

'''

# def quick_sort_diff(l):
#     if len(l) <= 1:
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
#     return quick_sort_diff(left) + middle + quick_sort_diff(right)


# def absoulute_diff(l,target):
#     diff=[]
#     for i in l:
#         if i>target:
#             diff.append(i-target)
#         else:
#             diff.append(target-i)
#     result=quick_sort_diff(diff)
#     return result


# user=eval(input("enter your list"))
# target=int(input("enter your target number"))
# result=absoulute_diff(user,target)
# print(result)

    






'''

Sort Only Odd Elements (Even ka Bhai)
Interviewer Bola: "Maaz, abhi tumne sirf even elements ko sort kiya tha. Ab mujhe ek un-sorted list doon, 
toh usme se sirf ODD elements ko sort karke dikhao, even numbers apni jagah se hilne nahi chahiye!"

Pattern Sequence:

Loop chala kar saare odd elements alag nikaal lo.

Apne Pivot Sort se un odds ko sort karo.

Main list mein jahan odd mile, wahan sorted wala bitha do.

Input: l = [5, 4, 1, 8, 3, 2]

'''



# def quiock_sort_pivot(l):
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
#     return quiock_sort_pivot(left)+ middle+ quiock_sort_pivot(right)


# def sort_odd_number(l):
#     odd=[]
#     for i in range(len(l)):
#         if l[i]%2!=0:
#             odd.append(l[i])
#     sorted_odd=quiock_sort_pivot(odd)
   

#     j=0
#     for i in range(len(l)):
#         if l[i]%2!=0:
#             l[i]=sorted_odd[j]
#             j=j+1
#     return l




# user=eval(input("enter your list"))
# result=sort_odd_number(user)
# print(result)
    















'''
Square and Sort a Sorted Array (Google/Adobe Round)
Interviewer Bola: "Aapko ek sorted list di hai jisme negative numbers bhi ho sakte hain 
(jaise [-4, -1, 0, 3, 10]). Mujhe har number ka square (square matrix style) chahiye aur final array bhi sorted 
hona chahiye, par bade numbers ko piche se bithaana shuru karna hai bina kisi extra sort function ke."

Hint: Kyunki list sorted hai, sabse bada square ya toh ekdum left waale negative ka hoga ya ekdum right waale 
positive ka. Do pointer shuruat aur aakhri mein bitha kar muqabla karwao!

Input: l = [-4, -1, 0, 3, 10]

Output: [0, 1, 9, 16, 100]

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



# def sort_square(l):
#     square=[]
#     for i in range(len(l)):
#         square.append(abs(l[i])**2)
#     sorted_square=quick_sort_pivot(square)
#     return sorted_square


# user=eval(input("enter your list"))
# result=sort_square(user)
# print(result)
        





