'''
Tumhe ek mixed list di hai: [4, -1, 5, -2, 3, -9]. Tumhe bina poori list ko sort kiye, 
saare negative numbers ko left mein aur saare
 positive numbers ko right mein karna hai. 
Output dikhna chahiye: [-1, -2, -9, 4, 5, 3]
'''
    
# def arrange_possitive_negative(l):
#     position=0
#     for i in range(len(l)):
#         if l[i]<0:
#             temp=l[position]
#             l[position]=l[i]
#             l[i]=temp
#             position=position+1
#     return l

# user=eval(input('enter your list'))
# result=arrange_possitive_negative(user)
# print(result)






'''
Ek list hai [1, 3, 20, 4, 1, 0]. Tumhe isme se woh "Peak Element" nikaalna hai jo 
apne padosi (left aur right dono) se bada ho. 
Jaise yahan 20 apne padosi 3 aur 4 dono se bada hai, toh output 20 aana chahiye.

'''
# def find_peak_element(l):
#     for i in range(1,len(l)-1):
#         if l[i]>l[i+1] and l[i]>l[i-1]:
#             return f'pick element is {l[i]}'
    
# user=eval(input("enter your list"))
# result=find_peak_element(user)
# print(result)






'First Non-Repeating Element '
# def first_non_repeating_element(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in l:
#         if d[j]==1:
#             return f'first non repeating is{j}'

# user=eval(input("enter your list"))
# result=first_non_repeating_element(user)
# print(result)





'First Repeating Element '

# def find_first_repeating_eleent(l):
#     d={}
#     for i in l:
#         if i in d:
#           d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in l:
#         if d[j]>1:
#             return f'first repating element is {j}'
#     return "No repeating element found"


# user=eval(input("enter your list"))
# result=find_first_repeating_eleent(user)
# print(result)





'	Leaders in Array '
# def leaders_element(l):
#     leader=l[-1]
#     leaders=[leader]
#     for i in range(len(l)-2,-1,-1):
#         if l[i]>leader:
#             leader=l[i]
#             leaders.insert(0,l[i])
#     return leaders



# user=eval(input("enter your list"))
# result=leaders_element(user)
# print(result)




'Next Greater Element '
# def next_greater(l):
#     n = len(l)
#     res = [-1] * n 
#     stack = []     
    
#     for i in range(n - 1, -1, -1): 
        
#         while stack and stack[-1] <= l[i]:  
#             stack.pop()                    
            
#         if stack:           
#             res[i] = stack[-1]  
            
#         stack.append(l[i])  
        
#     return res  





'Majority Element '
# def majority_element(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in l:
#         if d[j]>len(l)//2:
#             return f'majority element is {j}'
#     return f'no majority element'

# user=eval(input("enter your list"))
# result=majority_element(user)
# print(result)





'Missing Number '
# def is_missing_number(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in range(len(l)+1):
#         if j not in d:
#             return f'missing number is {j}'
        
# user=eval(input("enter your list"))
# result=is_missing_number(user)
# print(result)
