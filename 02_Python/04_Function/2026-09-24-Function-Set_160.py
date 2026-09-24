'Check karo kya list strictly monotonically increasing hai'

# def is_list_monotonically_increasing(l):
#     res=all(l[i]<l[i+1] for i in range (len(l)-1) )
#     return res


# user=eval(input("enter your list"))
# result=is_list_monotonically_increasing(user)
# print(result)




'Check karo kya list me koi element apne adjacent element ke barabar hai'

# def is_adjacent_element(l):
#     res=any(l[i]==l[i+1] for i in range(len(l)-1))
#     return res


# user=eval(input("enter your list"))
# result=is_adjacent_element(user)
# print(result)




'heck karo kya list ke saare numbers kisi number K ke multiples hain'
# def is_all_number_multiple_with_k(l,k):
#     return all(i%k==0 for i in l)


# user=eval(input("enter your list"))
# result=is_all_number_multiple_with_k(user)
# print(result)    



'Check karo kya list me koi sub-array/sub-list empty hai'
# def is_sub_empty_list(l):
#     res=any(len(i)==0 for i in l if isinstance(i,list))
#     return res

# user=eval(input("enter your list"))
# result=is_sub_empty_list(user)
# print(result)



'Check karo kya list me koi aisa number hai jiska square list me hi exist karta hai'
# def is_square_exist(l):
#     res=any(i**2 in l for i in l)
#     return res


# user=eval(input("enter your list"))
# result=is_square_exist(user)
# print(result)