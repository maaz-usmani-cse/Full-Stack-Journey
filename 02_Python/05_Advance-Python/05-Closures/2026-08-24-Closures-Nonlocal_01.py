'''
Closure kya hota hai?
A simple definition:
Jab ek nested function (andar wala function) apne outer function ke variables ko yaad rakhta hai,
chahe outer function execute hokar memory se khatam (return) hi kyu na ho chuka ho,
toh us combination ko Closure kehte hain.



Rule 1: Variable ka Scope (Kahan kaun accessible hai).


Outer function ke andar ka variable inner function read kar sakta hai,
lekin outer function khatam hote hi uske variables memory se delete ho jate hain.
'''

# def outer():
#     msg = "Main bahar hoon"
#     def inner():
#         print(msg)  # Inner function outer ke variable ko padh sakta hai
#     inner()

# outer()



'''
Rule 2: Function ko Run mat karo, Reference Return karo.

Function ke aage () lagane se wo turant chal jata hai. 
Bina () ke wo sirf ek object (reference) hota hai jisko return kiya ja sakta hai.


'''

# def outer():
#     msg='Hello'

#     def inner():
#         print(msg)

#     return inner


# my_func=outer()
# my_func()




'''
Agar value badalni ho to nonlocal use karo

Inner function outer variable ko sirf padh (read) sakta hai. 
Agar uski value badalni (modify) hai, to Python ko batana padega ki ye naya local variable nahi hai, balki bahar wala hai:

'''


# def make_cunter():
#     count=0
#     def increment():
#         nonlocal count
#         count=count+1
#         return count
#     return increment



# result=make_cunter()
# print(result())
# print(result())
# print(result())
# print(result())



