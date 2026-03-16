# for i in range(2,6):
#     print(i,end=' ')


# x = 5
# while x > 0:
#     print(x)
#     x-= 2

# for i in range(1,10,3):
#     print(i,end=' ')



# for i in range(3):
#     for j in range(2):
#      print(i+j, end=' ')



# user=input("enter your number")
# string=str(user)
# totaal=0
# for i in string:
#     if i.isdigit:
#         totaal=totaal+int(i)
# print(totaal)



# user=input("enter your number")
# rev=''
# for i in user:
#     rev=i+rev
# if rev==user:
#     print("pollindrom")
# else:
#     print("not pollindrom")



# a= [1,2,2,3,1,2]
# khali_dict={}
# for i in a:
#     if i in khali_dict:
#         khali_dict[i]=khali_dict[i]+1
#     else:
#         khali_dict[i]=1
# print(khali_dict)




# a=[20,50,30,80,4]
# maximum=a[0]
# for i in a:
#     if i>maximum:
#         maximum=i
# print(maximum)





# user=int(input("enter your number"))
# factorial=1
# for i in range(1,user+1):
#     factorial=factorial*i
# print(factorial)





# user=int(input('enter your number'))
# for i in range(2,user):
#     if user%i==0:
#         print("not prime")
#         break
# else:
#  print("prime")






# l=[]
# for i in range(10):
#     l.append(i)
# print(l)




# # Step 1: User se pucha kitne terms chahiye
# n =int(input("enter your number"))

# # Step 2: Shuruat ke do fixed numbers (Inhe 'Seed' kehte hain)
# a = 0
# b = 1

# print("Series shuru hoti hai:")

# # Step 3: Loop chalaya n baar
# for i in range(n):
#     # Sabse pehle 'a' ko print kar do
#     print(a, end=" ")
    
#     # Step 4: Agla number dimaag mein rakho (Sum)
#     next_number = a + b
    
#     # Step 5: Values ko shift karo (Yahi sabse zaroori hai!)
#     a = b             # Purana 'b' ab 'a' ban gaya
#     b = next_number   # Naya sum ab 'b' ban gaya






# s = "apple"
# checked = ""

# for i in s:
#     # Check kar rahe hain ki kya ye letter pehle aa chuka hai?
#     if i not in checked:
#         count = 0
        
#         # Pure word mein ghum kar count karo
#         for x in s:
#            if x == i:
#                 count = count + 1
        
#         print(i, "-", count, end=", ")
        
#         # Letter ko 'checked' mein daal do taaki dobara count na ho
#         checked = checked + i




# a={
# "maaz":3,
# "amjad":4,
# "sohail":6}




# user=int(input("enter your number"))
# for i in range(user,0,-1):
#     x=1
#     for j in range(1,i+1):
#         print(x,end=' ')
#         x=x+1
#     print()




