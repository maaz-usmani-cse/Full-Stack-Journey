'''
Tumhe 1 se lekar $n$ tak ke saare numbers ki ek list di gayi hai, lekin beech mein se ek number gayab hai.
 Bina sort kiye batao kaunsa?Input: 
 [1, 2, 4, 5, 6] (Yahan $n=6$ hai, aur 3 gayab hai)Output: 3
'''
# def find_gap(l):
#    for i in range(len(l)-1):
#       if l[i+1]!=l[i]+1:
#          return l[i]+1
#    return True

# user=eval(input("enter your list"))
# result=find_gap(user)
# print(result)      





'reverse number'
# def reverse(n):
#     rev=0
#     while n>0:
#         digit=n%10
#         rev=(rev*10)+digit
#         n=n//10
#     return rev

# user=int(input("enter your number"))
# result=reverse(user)
# print(result)








'''

List ke har element ko ek kadam aage sarka do, aur aakhri wala element uth kar shuruat mein aa jayega.

Input: [1, 2, 3, 4, 5]

Output: [5, 1, 2, 3, 4]

'''

# def right_shift(l):
#     temp=l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=temp
#     return l

# user=eval(input("enter your list"))
# result=right_shift(user)
# print(result)





'The Default Argument Trap (List/Dictionary)'
# def add_to_list(item, my_list=[]):
#     my_list.append(item)
#     return my_list

# print(add_to_list(1))
# print(add_to_list(2))
# print(add_to_list(3, []))
# print(add_to_list(4))




# Question: Inme se kaunsa line error dega aur kyun?
# s = {1, 2, (3, 4)}   # Line A
# s = {1, 2, [3, 4]}   # Line B





# multipliers = [lambda x: i * x for i in range(4)]

# # Agar hum ye execute karein:
# print([m(2) for m in multipliers])











# data = {}
# data[1] = "Apple"
# data[1.0] = "Banana"
# data[True] = "Cherry"

# print(data)
# print(len(data))






# t1 = (1, 2, 3)
# t2 = t1
# t1 = t1+(4, 5)

# print(t1)
# print(t2)





# multipliers = [lambda x: i * x for i in range(4)]
# # Agar hum ye execute karein:
# print([m(2) for m in multipliers])



