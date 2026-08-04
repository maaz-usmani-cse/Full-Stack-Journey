'''
'Write a program to check if two arrays are equal.'?
' (Order Not Same)??

'''
# def is_list_equal_ignore_order(l1,l2):
#     if len(l1) != len(l2):
#         return False

#     res={}
#     for i in l1:
#         if i in res:
#             res[i]=res[i]+1
#         else:
#             res[i]=1

#     for i in l2:
#         if i not in  res or res[i]==0:
#             return False

#         res[i]=res[i]-1
#     return True



# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=is_list_equal_ignore_order(l1,l2)
# print(result)






'''
Array me un sabhi elements ki list return karo jo $K$ se zyada baar aaye hain.Input: nums = 
[1, 2, 2, 3, 3, 3, 4, 4, 4, 4], k = 2Expected Output: [3, 4]
 (kyunki 3 teen baar aur 4 char baar aaya hai)

'''
# def find_element_gt_k(l,k=2):
#     res={}
#     for i in l:
#         if i in res:
#            res[i]=res[i]+1
#         else:
#             res[i]=1

#     final_res=[]
#     for i in res:
#         if res[i]>k:
#             final_res.append(i)
#     return final_res



# user=eval(input("enter your list"))
# result=find_element_gt_k(user)
# print(result)








'''
Move Zeroes to End
Task: Array ke saare 0 ko end me shift karo bina non-zero elements ka order change kiye.

Input: nums = [0, 1, 0, 3, 12]

Expected Output: [1, 3, 12, 0, 0]

'''


# def move_zeroes_end(l):
#     position=0
#     for i in range(len(l)):
#         if l[i]!=0:
          
#             temp=l[position]
#             l[position]=l[i]
#             l[i]=temp
#             position=position+1
#     return l




# user=eval(input("enter your list"))
# result=move_zeroes_end(user)
# print(result)

            
            



    
    
                