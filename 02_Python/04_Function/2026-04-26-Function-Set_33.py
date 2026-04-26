
'''
Next Smaller Element (Circular): Jaise aapne "Next Greater" kiya, waise hi circular list mein har
 element ke liye usse chota agla element dhoondo.
 '''
# def next_smallest_element(n):
#     l=[-1]*len(n)
#     for i in range(len(n)):
#         for j in range(1,len(n)):
#             index=(i+j)%len(n)
#             if n[index]<n[i]:
#                 l[i]=n[index]
#                 break
#     return l

# user=eval(input("enter your list"))
# result=next_smallest_element(user)
# print(result)












'''
Next Smaller Element (Circular): Jaise aapne "Next Greater" kiya, waise hi circular list mein har
 element ke liye usse chota agla element dhoondo.
'''
# def previous_smallest_element(n):
#    l=[-1]*len(n)
#    for i in range(len(n)):
#       for j in range(1,len(n)):
#          index=(i-j)%len(n)
#          if n[index]<n[i]:
#             l[i]=n[index]
#             break
#    return l


# user=eval(input('enter your list'))
# result=previous_smallest_element(user)
# print(result)










'''
Missing Number in AP: Aapko ek list di gayi hai jo AP honi chahiye thi, lekin ek number beech mein se gayab hai. 
Use dhoond kar nikaalo.Input: [2, 4, 8, 10] $\rightarrow$ Output: 6

'''


# def find_missing_number(n):
#    gap=n[1]-n[0]
#    for i in range(len(n)-1):
#       if n[i+1]!=n[i]+gap:
#          return 'gap is:',n[i]+gap
      
#    return True

# user=eval(input("enter your list"))
# result=find_missing_number(user)
# print(result)












'second smallest elemnt nikalo'
# def second_smallest(l):
#     first=None
#     second=None
#     for i in l:
#         if first is None or i<first:
#             second=first
#             first=i
#         elif i!=first and (second is None or i<second ):
#             second=i

#     return f'first smallest:{first} second smallest:{second}'

# user=eval(input('enter your list'))
# result=second_smallest(user)
# print(result)
    











'''
eak Element: Ek list mein wo number dhoondo jo apne piche wale aur aage wale dono numbers se bada ho.Input: 
[1, 2, 3, 1] $\rightarrow$ Output: 3

'''
# def find_peak_element(n):
#     peak=[]
#     for i in range(len(n)):
#         if i==0:
#             if n[i]>n[i+1]:
#                 peak.append(n[i])
#         elif i==len(n)-1:
#             if n[i]>n[i-1]:
#                 peak.append(n[i])
#         else:
#            if n[i]>n[i+1] and n[i]> n[i-1]:
#                peak.append(n[i])
#     return peak

# user=eval(input("enter your list"))
# result=find_peak_element(user)
# print(result)













'el list m ka sbse bada gap dhundho aap  jaise [1,10,20,30,35,40]'

# def find_biggest_gap(l):
#     biggest_gap=None
#     for i in range(len(l)-1):
#         current_gap=l[i+1]-l[i]
#         if biggest_gap is None or current_gap>biggest_gap:
#             biggest_gap=l[i]
#     return f' biggest gap is:{biggest_gap}'


# user=eval(input('enter your list'))
# reuslt=find_biggest_gap(user)
# print(reuslt)

   




'''
Leader in the list (Peeche Mud kar mat dekho)
Ek list mein wo number dhoondo jo apne right side ke saare numbers se bada ho.

'''

# def greater_than_all_right_element(l):
#    greater_element=[]
#    for i in range(len(l)):
#       for j in range(i+1,len(l)):
#          if l[i]<l[j]:
#             break
#       else:
#        greater_element.append(l[i])
#    return greater_element


# user=eval(input("enetr your list"))
# result=greater_than_all_right_element(user)
# print(result)




'luhn algorithm'
# def luhn_algorithm(n):
#     if n.isdigit(): 
#         rev = n[::-1]
#         odd = rev[0::2]
#         even = rev[1::2]
#         total = 0
#         for i in odd:
#             total = total + int(i)
#         for i in even:
#             multiply = int(i) * 2
#             if multiply > 9:
#                 multiply = multiply - 9
#             total = total + multiply
        
#         if total % 10 == 0:
#             return f'ye valid luhn algorithm hai {n}'
#         else:
#             return f'y valid luhn algorithm nahi h {n}'
#     else:
#         return "Bhai sahi number dalo, letters nahi!"
        


# user=input('enter your number')
# result=luhn_algorithm(user)
# print(result)




