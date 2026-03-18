# user=input("enter your number")
# print(user,type(user),bool(user)) #y print sirf isliye hai taki aapko screen per dikh sake ki aapne kya type kya hai,uska data type kya hai,python usse true manta hai ya false(ye line sirf aapki jankari k liye hai if else s iska koi lena dena nahi hai)



# if user:
#     print("vale is =",user)
# else:
#     print("empty data") 
    



# user=input("enter your number") #agr user ne kuch type kiya to if chalega wrna else chalega
# if user:
#     print("maaz")
# else:
#     print("kuch na")


# n="0"
# if n:
#     print("option A",bool(n))
# else:
#     print("optin B",bool)



# n=0
# if n:
#     print("sacha")
# else:
#     print("jhoot")




# n=input("enter your number")
# if n:
#     print("kuch to h variable m")
# else:
#     print("kuch type nahi kia gaya hai")

""""
1.python me if vadriable:ka matlab hota hai:

.bhara hua dabba=True (Hamesha if chalega)
.khali dabba/zero=False (Hamesha else chalega)


2. kab if nahi chalega ?(sach/True)
dunya ka koi bhi letter ,koi v number (zero ko chhor ko chhod kar)
ya ek chota sa space bhi aa jayega,toh if hi chalega


examples:
  n= "500"(number hai) True
  . n= . n="A"(letter hai)-> True
  . "0" (quotes me string hai yani string bhari hai)-> True
  . n= " " (sirf space hai)-->True

  



  string ek variable m ho jyse a= "maaz" ya a="0"
  ya tum user s input le rhe ho string meh wo jsyse, input("enter your number")
  to bus khai string,beech m ek gap  nahi  ("") ko chorke baki sab chiz true hai yani sab if m chalegga bas khali string he else ka par mana jayega bus khali sting me he else ka part chalega.
"""





# n=input("enter your number")
# if n:
#     print("maaz")
# else:
#     print("usmani")





# a=0
# b="0"
# if a:
#     print(a)
# elif b:
#     print(b)
# else:
#     print("dono m s koi nahi")



# n=10
# if n>5:
#     print("greater than 5")
# if n>8:
#     print("greater than 8")
# else:
#     print("small number")






# x=bool(print("hello"))
# if x:
#     print("condition true")
# else:
#     print("condition false")


# while True: 
#    print("hello")

# n= int(input("enter your number"))
# x=1
# while x<=n:
#     print(x)
#     x=x+1
    



# n=int(input("ente your number"))
# a=1
# factoril=1
# while a<=n:
#     factoril=factoril*a
#     a=a+1
# print(factoril)


# user=int(input("enter yout number"))
   
# value=1
# store=0
# for i in range(500,511):
#    store= value*user
#    print(store)
#    value=value+1
   

    
# n= int(input("enter your number"))
# i=1
# while i<=n:
#     print(i)
#     i=i+1


# n=int(input("enter your number"))
# i=1
# while i<=n:
#     print(i,end=' ')
#     i=i+1



# n=int(input("enter your number"))
# i=1
# while i<=n:
#     print(i,end='+')
#     i=i+1




# n=int(input("enter your number"))
# i=1
# while i<=n:
#     if i<n:
#       print(i,end='+')
  
#     else:
#        print(i)
#     i=i+1





# n=int(input("enter your number"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     if i<n:
#       print(i,end='+')
  
#     else:
#        print(i,end=' =')
#     i=i+1
# print(sum)
   
   




# n=int(input("enter your number"))
# i=1
# multiply=1
# while i<=n:
#     multiply=multiply*i
#     if i<n:
#       print(i,end='*')
  
#     else:
#        print(i,end=' =')
#     i=i+1
# print(multiply)
   


# n=int(input("enter your number"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     if i<n:
#       print(2*i,end='*')
  
#     else:
#        print(2*i,end=' =')
#     i=i+1
# print(sum)
   
"user se input leke check kro kitna vowels hai kitna consonant hai"
'isalpha() ye check karta hai ki character a-z k beech ka leterhi hai na kyuki agr sentance m space  ya comma ya number hoga to hame usko count nahi karna hai'
# user=input("enter your number")
# vowel=0
# consonant=0
# user=user.lower()
# for i in user:
#     if i.isalpha():  
#       if i in["a","e","i","o","u"]:
#         vowel=vowel+1
#       else:
#         consonant=consonant+1
# print("vowel hai",vowel)
# print("consonent",consonant)



"ek word ko check karo ki wo aage s yaa peeche s padhne m same hai ki nahi (yani pallindrom hai ki nahi ye check karna haii)"
# word=input("enter your number")
# reverse=''
# for i in word:
#     reverse=i+reverse

# if word==reverse:
#       print(word,"ek pallindrom hai")
# else:
#       print(word,"pallindrom nhi hai")




'check karo konsa akshar kitni bar aaya hai'
# user=input("enter your number")
# khali_dict={}
# for i in user:
#     if i in khali_dict:
#         khali_dict[i]=khali_dict[i]+1  #Python ke niyam ke hisaab se, aap ek Container aur ek Number ko aapas mein + nahi kar sakte. Isliye wo terminal par error deta hai:jyse hamlog (khalidict+1) nahi kar skte 
#     else:
#         khali_dict[i]=1
# print(khali_dict)


"word dal k pata karo ki usme kon kitni bar aAYA HAI BAHi"

# user=input("enter your number")
# khalidict={}
# for i in user:
#     if i in khalidict:
#         khalidict[i]=khalidict[i]+1
#     else:
#         khalidict[i]=1
# print(khalidict)



# user=input("enter your number")
# vowel=0
# consonant=0
# for i in user:
#     if i.isalpha():
#         if i in["a","e","i","o","u"]:
#             vowel=vowel+1
#         else:
#             consonant=consonant+1
# print('total vowe :',vowel)
# print("total consonant :",consonant)
   



# a=[20,50,30,50,80,50,60,60,70,50,5]
# khali_dict={}
# for i in a:
#     if i in khali_dict:
#         khali_dict[i]=khali_dict[i]+1
#     else:
#         khali_dict[i]=1
# print(khali_dict)


'list ka sabse bada aur sabse chota number'

# a=[12,50,80,56,80,1,0,25]
# smal=a[0]
# big=a[0]
# for i in a:
#     if i<smal:
#         smal=i
       
#     elif i>big:
#         big=i
# print('ye sabse chota jai',smal)
# print("ye sabse bada hai list ka ",big)

# 'check kro kon kitni bar aya hai'
# sales=["pen","pencil","pencil","pen","pencil","pencil"]
# khali_dict={}
# for i in sales:
#     if i in khali_dict: #agr i khali dict m h condition true hai to he y block execute hoga otherwise else likha hai to won kisi ka baap v mnahi rok sakta wo to chakega he chalega 100
#         khali_dict[i]=khali_dict[i]+1
        
#     else:
#         khali_dict[i]=1 
# print(khali_dict)



# khali_dict={}
# for i in "maazusmani":
#     if i in khali_dict:
#         khali_dict[i]=khali_dict[i]+1
#     else:
#         khali_dict[i]=1

# print(khali_dict)



# user=int(input("enter your number"))
# for i in range(1,user+1):
#    x=2
#    for j in range(1,i+1):
#       print(x,end=' ')
#       x=x+2
#    print()




'Find the difference between largest and smallest digit in for loop '
# a = [20, 50, 2, 5, 90, 5, 4]
# small=a[0]
# big=a[0]
# for i in a:
#     if i<small:
#         small=i
#     elif i>big:
#         big=i
# diffrence=big-small
# print("sbse bda number hai",big)
# print("sabse chota number hai",small)
# print("dono k beech ka diffrence hai",diffrence)





#check kro kon leap year h kon nahi hai leap year
for years in range (1990,2027):
    if years%4==0 and years%100!=0 or years%400==0:
        print(years,"ye year leap year hai")
    else:
        print(years,"ye normal year hai ")
        