'Ek function jo check kare do strings Anagrams hain ya nahi.'
# def anagram(n1,n2):
#     if len(n1)!=len(n2):
#         print("angram nahi ho sakta hai")
#         return 
    
#     d={}
#     for  i in n1:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in n2:
#         if j in d:
#             d[j]=d[j]-1
#         else:
#             print("ye angram nahi ho skta hai")
#             return
#     for i in d:
#         if d[i]!=0:
#             return 
#     print("anagram hai")


# user1=input("enter your word")
# user2=input('enter your word')
# anagram(user1,user2)




# user1=input("enter your number")
# user2=input("enter your number")
# if len(user1)!=len(user2):
#     print("ye angram nahi hai")




'Ek "Closure" function ka example likho jo counter ki tarah kaam kare.'


# def closure():
#     counter=0
#     def inner():
#         nonlocal counter
#         counter=counter+1
#         return counter
#     return inner

# result=closure()
# print(result())
# print(result())
# print(result())



'''
Ek aisa function make_multiplier(n) likho jo ek number n le aur ek naya function return kare. 
Wo naya function kisi bhi number ko n se multiply kare.

'''

# def make_multiplier(n):
   
    
#     def multiplier(x):
       
#         return x * n  
#     return multiplier
# doubler = make_multiplier(2)


# print(doubler(5)) 
# print(doubler(10)) 

# tripler = make_multiplier(3)
# print(tripler(5)) 






