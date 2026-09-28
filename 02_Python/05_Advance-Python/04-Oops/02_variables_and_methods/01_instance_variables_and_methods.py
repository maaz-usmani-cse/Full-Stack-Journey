'''
================================================================================
TOPIC: Instance Variables & Instance Methods (Deep Dive)
================================================================================

1. INSTANCE VARIABLE KYA HOTA HAI?
Jo variable har object ka apna alag personal data rakhta hai, usko Instance Variable kehte hain.

Jaise aapka naam alag hai, doosre student ka naam alag hoga.


Isko access ya modify karne ke liye hamesha `self.variable_name` (class ke andar) 
     ya `obj.variable_name` (class ke bahar) use kiya jata hai.



2. INSTANCE VARIABLE BANANE KE 3 TARIQA:
Tareeqa 1: Inside Constructor (__init__ ke andar)
      - Ye sabse standard aur safe tareeqa hai. Object bante hi variables ban jaate hain.
      - Jaise: self.stu_name = name, self.age = age

   Tareeqa 2: Inside Instance Method (Method ke andar)
      - Isme variable tab tak create NAHI hota jab tak wo method call na ho!
      - Jaise: def student_details(self, contact): self.contact = contact
      - Rule: Agar method call nahi karoge aur variable access karoge, toh AttributeError aayega.

   Tareeqa 3: Outside Class (Class ke bahar direct object reference se)
      - Class ke bahar seedhe: obj.address = "Bhopal" likh kar naya variable chipka dena.





3. INSTANCE METHOD KYA HOTA HAI?
Class ke andar bana aisa normal function jo kisi specific object ke data (instance variables) ke sath kaam karta hai.
Pehchan: Iska pehla parameter hamesha self hota hai (jaise sir ne banaya: 
def student_details(self, contact):). 
Call karne ka tareeqa: Isko object ke naam se dot laga kar call kiya jata hai, jaise: obj.student_details(...). 


Q2: Mujhe kaise pata chalega ki kisi object ke paas abhi kaunse instance variables hain?
Ans: Python ke built-in attribute `obj.__dict__` se! Yeh dictionary format mein object 
     ke saare instance variables aur unki values dikha deta hai.
================================================================================

'''


class Student:
    # ---------------------------------------------------------
    # Tareeqa 1: Inside Constructor (__init__ ke andar create karna)
    # ---------------------------------------------------------
    def __init__(self, name: str, age: int, email: str):
        self.stu_name = name      # Instance Variable 1
        self.age = age            # Instance Variable 2
        self.email = email        # Instance Variable 3


    # ---------------------------------------------------------
    # Tareeqa 2: Inside Instance Method ke andar create karna
    # ---------------------------------------------------------
    def student_details(self, contact: str):
        # Yeh variable tabhi banega jab ye method call hoga
        self.contact = contact    # Instance Variable 4


    # Instance method object ka data read karne ke liye
    def display_full_profile(self):
        print(f"\n--- Student Profile: {self.stu_name} ---")
        print(f"Age: {self.age} | Email: {self.email}")
        # Check karte hain contact exist karta hai ya nahi
        if hasattr(self, 'contact'):
            print(f"Contact: {self.contact}")
        if hasattr(self, 'address'):
            print(f"Address: {self.address}")



obj = Student("Maaz", 25, "maazusmani15@gmail.com")
# Check point 1: Abhi object ke paas sirf 3 variables hai
print(f"\nAbhi obj.__dict__ dekho: {obj.__dict__}")



# Agar bina contact pass kiye call karenge:
try:
     obj.student_details()  # TypeError aayega
except TypeError as e:
    print(f"Bina argument call karne par Error aaya: {e}")




# Sahi tareeqa: Argument pass karke call karo
obj.student_details("1234567890")


# Check point 2: Ab contact variable bhi object ke andar add ho chuka hai!
print(f"Abhi obj.__dict__ dekho: {obj.__dict__}")



# Tareeqa 3: Class ke bahar direct add kiya
# Tareeqa 3: Class ke bahar direct add kiya
obj.address = "Bhopal"
print(f"Address bahar se set ho gaya: {obj.address}")


# Check point 3: Ab 5 variables ho chuke hain
print(f"Final obj.__dict__: {obj.__dict__}")

# Full details print
obj.display_full_profile()