
'Ek circular list mein har element ke liye usse bada agla element dhoondo.''(i already discuss this question in previous set)'
# def next_greater(n):
#     greater=[-1]*len(n)
#     for i in range(len(n)):
#         for j in range(1,len(n)):
#             index=(i+j)%len(n)
#             if n[index]>n[i]:
#                 greater[i]=n[index]
#                 break
#     return greater

# user=eval(input("enter your list"))
# result=next_greater(user)
# print(result)










'''


 Circular Sum Check: Kya list mein koi aisa element hai jiske
 left aur right ka sum (circularly) barabar ho?


'''


# def find_circular_iquilibrium(n):
#     iquilibrium_index = []
#     length = len(n)

#     for i in range(length):
#         # i hamara wo element hai jise humne pivot mana hai
#         # Ab baaki bache huye length-1 elements ko check karna hai
#       
#         for split in range(1, length):
#             left_sum = 0
#             # Split ke hisab se left side ke elements uthao
#             for j in range(1, split + 1):
#                 idx = (i + j) % length
#                 left_sum = left_sum + n[idx]
            
#             right_sum = 0
#             # Baaki bache huye elements right side mein
#             for k in range(split + 1, length):
#                 idx = (i + k) % length
#                 right_sum = right_sum + n[idx]
                
#             if left_sum == right_sum:
#                 # Agar mil gaya toh pivot element ko list mein daal do
#                 if i not in iquilibrium_index:
#                     iquilibrium_index.append(i)
#                 break 
                
#     return iquilibrium_index

# user = eval(input("enter your list: "))
# result = find_circular_iquilibrium(user)
# print(result)









'''


Next Smaller Element (Circular): Jaise aapne "Next Greater" kiya, waise hi circular list mein har
 element ke liye usse chota agla element dhoondo.



# '''
# def next_smaller(n):
#     # Shuruat mein sabko -1 maan lo
#     smaller = [-1] * len(n)
    
#     for i in range(len(n)):
#         # i hamara current element hai
#         for j in range(1, len(n)):
#             # Circularly agla index nikal rahe ho
#             index = (i + j) % len(n)
            
#             # BAS YAHAN FARQ HAI: > ki jagah < kar diya
#             if n[index] < n[i]:
#                 smaller[i] = n[index]
#                 break # Pehla chota milte hi bahar nikal jao
                
#     return smaller

# user = eval(input("enter your list: "))
# result = next_smaller(user)
# print(result)