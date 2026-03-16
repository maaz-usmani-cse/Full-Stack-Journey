# n1=0
# n2=1
# for i in range(5):
#     print(n1,end=' ')
#     sum=n1+n2
#     n1=n2
#     n2=sum


# a={
# 12: "Child",
# 19: "Teenager",
# 59: "Adult",
# 60 : "Senior Citizen"
# }

# age=int(input("enter your number"))
# # age=int(input("enter your number"))
# for i in a:
#     if age>=0 and age<=12:
#         print(a,a[i])
#         break
#     elif age>12 and age<=19:
#         print(a,a[i])
#         break
#     elif age>19 and age<=59:
#         print(a,a[i])
#         break
#     elif age>=60:
#         print(a,a[i])
#         break





# age_data = {
#     12: "Child",           # 0 se 12 tak
#     19: "Teenager",        # 13 se 19 tak
#     59: "Adult",           # 20 se 59 tak
#     150: "Senior Citizen"  # 60 se upar
# }

# user_age = int(input("Age daalein: "))
# for i in age_data:
#     if user_age <= i:
#         print(age_data[i])
#         break





# data = {'a': 100, 'b': 200, 'c': 300}
# total=0
# for i in data:
#     total=total+data[i]
# print(total)



'reverse dict'

# old_dict = {'A': 1, 'B': 2, 'C': 3}
# rev={}
# for i in old_dict:
#     val=old_dict[i]
#     rev[val]=i
# print(rev)



# 'max value in dict'
# scores = {'Rahul': 85, 'Amit': 92, 'Sita': 78}
# max=0
# for i in scores:
#     if scores[i]>max:
#         max=scores[i]
# print(max)




'frequency count'
# fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# count={}
# for i in fruits:
#     if i in count:
#         count[i]=count[i]+1
#     else:
#         count[i]=1
# print(count)



'merged karna tha value ko do dic ko ek me merge kaarna tha isliye teesra dict lena pa'
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# merged={}
# for i in dict1:
#     merged[i]=dict1[i]
#     for j in dict2:
#         merged[j]=dict2[j]
# print(merged)






# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dictt3={}
# for i in dict1:
#     dictt3[i]=dict1[i]
#     for j in dict2:
#         dictt3[j]=dict2[j]
# print(dictt3)



# l1=[1,2,3,4,5]
# l2=[1,2,3,4,5]
# l3=[1,2,3,4,5]


# def add(n1,n2,n3):
#     return n1+n2+n3


# result=map(add,l1,l2,l3)
# print(list(result))





# l1=[1,2,3,4,5]
# l2=[1,2,3,4,5]
# l3=[1,2,3,4,5]


# result=map(lambda x,y,z:x+y+z,l1,l2,l3)
# print(list(result))





# a=[20,30,50,70]
# total=0
# for i in a:
#     total=total+i
# print(total)
# average=total/len(a)
# print(average)




# def avergae(n):
#     total=0
#     for i in n:
#         total=total+i
#     average=total/len(n)
#     return average

# a=[20,50,70,80,60]
# result=avergae(a)
# print(result)



# a=[20,4,3,7,6,25,27,50,63,91,3,5,60]
# result=filter(lambda x: x%3==0 and x%5==0,a)
# print(list(result))



'list se aysa number nikalo jo 3 aur 5 se devide ho '

# nums=range(1,51)
# result=filter(lambda x: x%3==0 and x%5==0 , nums)
# print(list(result))



# a=[[1, 2], [3, 4], [5, 6]]
# result=map(lambda x:x[0],a)
# print(list(result))


# from functools import reduce
# a=[20,50,20,30,80]
# result=reduce(lambda x,y: x if x>y else y,a)
# print(result)




# data = ["Maaz", "", None, "Python", " "]
# clean = list(filter(lambda x: x and x.strip(), data))




'reverse string'

# result=lambda x:x[::-1]
# print(result("asrina"))


a="maaz"

for i in range(len(a)-1,-1,-1):
   b=(a[i])
   print(b)


