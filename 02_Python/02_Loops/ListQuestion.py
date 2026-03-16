'total of list'

# a=[20,30,40,50,60]
# total=0
# for i in a:
#     total=total+i
# print(total)



'sbse bda number list ka'
# a=[20,30,40,50,60]
# big=a[0]
# for i in a:
#     if i>big:
#         big=i
# print(big)


'sabse chota number'
# a=[20,30,40,50,60]
# chota=a[0]
# for i in a:
#     if i<chota:
#         chota=i
# print(chota)


'list reverse karo'
# a=[20,30,40,50,60]
# d=[]
# for i in a:
#     d.insert(0,i)
# print(d)

'with range list reverse'
# a=[20,30,40,50,60]
# d=[]
# for i in range(len(a)-1,-1,-1):
#     d.append(a[i])
# print(d)


'list me koi element kitni bar aya hai count karo'
# a=[20,30,40,50,50,60,2,2,60]
# d={}
# for i in a:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)


'list m se dublicate value kaise hataye'
# a=[20,30,40,50,50,60,2,2,60]
# d=[]
# for i in a:
#     for j in a:
#        if i not in d:
#              d.append(i)
# print(d)


'kya list palindrom hai'
# a=[1,2,1]
# rev=[]
# for i in a:
#     rev.insert(0,i)
# if rev==a:
#     print("pollindrom")
# else:
#     print("not pollindrom")


'list ka total count karne k bad pata kro list pollindrom hai ya nahi'
# a=[10,5,2,4,100,1]
# total=0
# for i in a:
#     total=total+i # pehle mene total ko nikala 
# print("y total:",total)
# change=str(total) #mene total ka data type badla taki check kru 
# if change==change[::-1]: 
#     print("pollindrom hai")
# else:
#     print("nahi hai")




"list m '2' element kitni bar aya hai"
# a=[2,2,4,5,6,7,3,6,5,7]
# target=2
# count=0
# for i in a:
#     if i==target:
#         count=count+1
# print(count)
        


'second largest nikal k dekhao list ka'
# a = [10, 25, 25, 15]

# first = a[0]
# second = None


# for i in a:
#     if i > first:
#         second = first
#         first = i
#     elif i < first:
#         if second is None or i > second:
#             second = i

# print("Final Second Largest is:", second)

# user=input("enter your number")
# first=user[0]
# last=user[-1]
# middle=''

# for i in range(1,len(user),-1):
#         middle=middle+user[i]
# result=last+middle+first
# print(result,end=' ')











