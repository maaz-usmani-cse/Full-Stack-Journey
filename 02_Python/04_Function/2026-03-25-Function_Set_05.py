'wap to take input from runtime and find out their data type'
# def check_dta_type(n):
#    try:
#      result=eval(n)
#      return(type(result))
#    except:
#       return type(n)
   
# user=input("enter your number")
# result=check_dta_type(user)
# print(result)




'wap to take a list from run time and find out maximum digit without using max()'
# def maximum_digit_in_list(n):
#     maximum_digiit=None
#     for i in n:
#         if maximum_digiit is None or i>maximum_digiit:
#             maximum_digiit=i
#     return maximum_digiit

# user=eval(input('enter your number'))
# result=maximum_digit_in_list(user)
# print(result)



'wap to arrange all zeroes at the end '
# def zeros_one_side(n):
#     zeroes=[]
#     nonzeroes=[]
#     for i in n:
#         if i==0:
#             zeroes.append(i)
#     for i in n:
#         if i!=0:
#             nonzeroes.append(i)
#     result=zeroes+nonzeroes
#     return result

# user=eval(input("enter your number"))
# result=zeros_one_side(user)
# print(result)


'wap to take input string at run time and return a string incremented by 2 to every charactors'
# def incremented_by_2_every_string(n):
#     result=''
#     for i in n:
#       x=ord(i)
#       y=x+2
#       z=chr(y)
#       result=result+z
#     return result
      

# user=input('enter your number')
# result=incremented_by_2_every_string(user)
# print(result)




'wap to take input from '
# def perfect_number(n):
#     total=0
#     for i in range(1,n):
#         if n%i==0:
#             total=total+i
#     if total==n:
#         return "perfect number"
#     else:
#         return "not perfect"


# user=int(input('enter your number'))
# result=perfect_number(user)
# print(result)
        


'wap to arrenge all items from list in assending order '
# def arrange_asending_order(n):
#     for i in range(len(n)):
#         for j in range(0,len(n)-1):
#             if n[j]>n[j+1]:
#                 temp=n[j]
#                 n[j]=n[j+1]
#                 n[j+1]=temp
#     return n

# user=eval(input("enter your list"))
# result=arrange_asending_order(user)
# print(result)