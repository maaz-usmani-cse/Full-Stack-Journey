'''
Duplicate elements hatao lekin first occurrence ka order maintain rakho
[1, 2, 2, 3, 4, 1, 5, 3]
'''
# d={}
# def remove_dublicate(n):
#     if n in d:
#         return False

#     else:
#         d[n]=True
#         return True

# user=eval(input("enter your list"))
# result=list(filter(remove_dublicate,user))
# print(result)
        



'''
ist me se check karo kaunse numbers Fibonacci series ke part hain.
nums = [2, 4, 5, 8, 13, 20, 21]
'''
# def is_fibonacci_series(n):
#     if n<0:
#         return False

#     n1=0
#     n2=1
#     while n1<n:
#         add=n1+n2
#         n1=n2
#         n2=add

#     if n1==n:
#         return True
#     return False

# user=eval(input("enter your list"))
# result=list(filter(is_fibonacci_series,user))
# print(result)



'Filter numbers divisible by both 3 and 5. nums = [15, 20, 30, 45, 52, 60]'

# user=eval(input("enter your list"))
# result=list(filter(lambda x: x%3==0 and x%5==0,user))
# print(result)


'Filter words jo already capital letter se start hote hain  words = ["delhi", "Mumbai", "pune", "Bangalore"]'

# user=eval(input("enter your list"))
# res=list(filter(lambda x: x.istitle(), user))
# print(res)



'Domains me se sirf corporate subdomains ("corp.") filter karo. domains = ["api.corp.google.com", "myblog.org", "internal.corp.amazon.com"]'

# user=eval(input("enter yur list"))
# res=list(filter(lambda x: '.corp.' in  x ,user))
# print(res)


'Sensor readings me se normal readings 20 to 35 filter karo.temps = [18.5, 22.0, 34.5, 41.2, 29.8]'

# user=eval(input("enter your list"))
# result=list(filter(lambda x: x>=20.0 and x<=35.0,user))
# print(result)


'''
E-commerce products me se out-of-stock products flter kro
inventory = [
    {"name": "Mouse", "in_stock": True},
    {"name": "Keyboard", "in_stock": False},
    {"name": "Monitor", "in_stock": False}
]

'''
# user=eval(input("enter your list"))
# result=list(filter(lambda x: not x['in_stock'] , user))
# print(result)

