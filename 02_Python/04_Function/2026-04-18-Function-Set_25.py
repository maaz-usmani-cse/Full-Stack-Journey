'bina ksi in built function k cube nikalo kisi v number ka '
# def cube(n):
#     count=0
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 count=count+1
#     return f"cube hai{count}"


# user=int(input("entr your number"))
# result=cube(user)
# print(result)







'bin kis inbuilt function k square nikal k dekhao'
# def square(n):
#     count=0
#     for i in range(n):
#         for j in range(n):
#             count=count+1
#     return count

# user=int(input("enter your number"))
# result=square(user)
# print(result)






'.Count frequency of each element '
# def count_frequency(n):
#     d={}
#     for i in n:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d


# user=input("enter your word/ number")
# result=count_frequency(user)
# print(result)





'.Find most frequent element '
# def find_most_frequent_element(n):
#     d={}
#     for i in n:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     maximum=None
#     value=0
#     for i in d:
#         if maximum is None or i>maximum:
#             maximum=d[i]
#             value=i
#     return value

# user=eval(input("enter your list"))
# result=find_most_frequent_element(user)
# print(result)       






'.	Find least frequent element '
# def find_least_frequent(n):
#     d={}
#     for i in n:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     minimum=None
#     least_frequent=0
#     for j in d:
#         if minimum is None or d[j]<minimum:
#             minimum=d[j]
#             least_frequent=j
#     return least_frequent



# user=eval(input("enter your list"))
# result=find_least_frequent(user)
# print(result)
        





'	Count elements appearing more than once '
# def count_apperaing_morethan_once(n):
#     d={}
#     l=[]
#     for i in n:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#            d[i]=1
#     for j in d:
#         if d[j]>1:
#             l.append(j)
#     return l

# user=eval(input("enter your list"))
# result=count_apperaing_morethan_once(user)
# print(result)       

    



'.Print duplicate elements '
# def dublicate_element(n):
#     l=[]
#     dublicate=[]
#     for i in n:
#        if i not in l:
#            l.append(i)
#        else:
#            dublicate.append(i)
#     return dublicate
# user=eval(input("enter your list"))
# result= dublicate_element(user)    
# print(result)      
           




'Find first non-repeating element '
# def nonrepeating_element(n):
#     d={}
#     for i in n:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in d:
#         if d[j]==1:
#             return j
#     else:
#         return None
    
# user=eval(input("enter your list"))
# result=nonrepeating_element(user)
# print(result)
        
    


    
'.	Reverse a list '
# def reverse_list(n):
#     l=[]
#     for i in range(len(n)-1,-1,-1):
#         l.append(n[i])
#     return l
       
# user=eval(input("enetr your list"))
# result=reverse_list(user)
# print(result)






'.Rotate list left by 1 '
# def rotateleft_list(n):
#     temp=n[0]
#     for i in range(len(n)-1):
#         n[i]=n[i+1]
#     n[-1]=temp
#     return n

# user=eval(input("enter yoru list"))
# result=rotateleft_list(user)
# print(result)
