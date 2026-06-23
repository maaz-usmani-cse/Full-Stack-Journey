'Find equilibrium index '
# def find_equilibrium_index(l):
#     total=0
#     left=0
#     for i in l:
#         total=total+i
#     for j in range(len(l)):
#         right=total-left-l[j]
#         if left==right:
#             return j
        
#         left=left+l[j]
#     return -1

# user=eval(input("enter your list"))
# result=find_equilibrium_index(user)
# print(result)





'Swap first and last element '
# def swap_first_and_last(s):
#     first=s[0]
#     middle=s[1:-1]
#     last=s[-1]
#     return last+middle+first


# user=input("enter your word")
# result=swap_first_and_last(user)
# print(result)








'Swap largest and smallest element '
# def swap_largest_smallest_element(l):
#     smallest=None
#     largest=None
#     smallest_index=None
#     largest_index=None
#     for i in range(len(l)):
#         if smallest is None or l[i]<smallest:
#             smallest=l[i]
#             smallest_index=i
#         if largest is None or l[i]>largest:
#             largest=l[i]
#             largest_index=i
#     temp=l[largest_index]
#     l[largest_index]=l[smallest_index]
#     l[smallest_index]=temp
#     return l


# user=eval(input("enter your list"))
# result=swap_largest_smallest_element(user)
# print(result)






         
'Zigzag arrange (> < > <) '
# def zig_zag_element(l):
#     for i in range(len(l)-1):
#         if i%2==0:
#             if l[i]<l[i+1]:
#                 temp=l[i]
#                 l[i]=l[i+1]
#                 l[i+1]=temp
#         else:
#             if l[i]>l[i+1]:
#                 temp=l[i]
#                 l[i]=l[i+1]
#                 l[i+1]=temp
#     return l
       
# user=eval(input("enter your list"))
# result=zig_zag_element(user)
# print(result)



'sort the list'
# def quick_sort_pivot(l):
#     if len(l) <= 1:
#         return l
#     pivot = l[0]
#     left = []
#     middle = []
#     right = [1,3,]
    

#     for num in l:
#         if num < pivot:
#             left.append(num)   
#         elif num == pivot:
#             middle.append(num)  
#         else:
#             right.append(num)  
            
#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)

# user_list = eval(input("enter your list"))
# result = quick_sort_pivot(user_list)
# print("Pivot se Sorted List:", result)











'Sort only even elements '
# def quick_sort_pivot(l):
#     if len(l) <= 1:
#         return l
#     pivot = l[0]
#     left, middle, right = [], [], []
#     for num in l:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)



# def sort_only_even(l):
#     evens = []
#     for num in l:
#         if num % 2 == 0:
#             evens.append(num)
            
#     sorted_evens = quick_sort_pivot(evens)
    
#     j = 0 
#     for i in range(len(l)):
#         if l[i] % 2 == 0:
#             l[i] = sorted_evens[j]
#             j += 1 
            
#     return l


# user_list = [5, 8, 1, 4, 2, 7]
# result = sort_only_even(user_list)
# print("Sirf Even Sort Ke Baad:", result)








