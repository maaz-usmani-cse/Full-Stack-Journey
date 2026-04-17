'second largest nikal k do list se hame '
# def second_largest(n):
#     first=None
#     second=None
#     for i in n:
#         if first is None or i>first:
#             second=first
#             first=i
#         elif i!=first and (second is None or i>second ):
#                 second=i
#     return 'first:',first ,'second',second
    

# user=eval(input("enter your list:"))
# result=second_largest(user)
# print(result)








'Write a program to find the missing number in a series.'
def find_missing_value(n):
    for i in range(1,len(n)):
        if n[i]!=n[i-1]+1:
            return n[i-1]+1

user=eval(input("enter your list"))
result=find_missing_value(user)
print(result)




