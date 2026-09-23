"""
================================================================================
TOPIC: Class & Object Fundamentals (Day 1 - Basics)
================================================================================

🧠 ASLI CONCEPT (SIMPLE HINGLISH MEIN):

1. CLASS KYA HAI? (Blueprint / Naksha / Sancha)
   - Class ek user-defined design ya blueprint hoti hai.
   - Example: Maan lo ek ghar ka naksha (map) paper par bana hai. Naksha khud koi 
     ghar nahi hai, uske andar koi reh nahi sakta, aur na hi wo zameen par jagah 
     gher raha hai.
   - Isi tarah Class sirf rules aur structure tay karti hai ki aane wale object 
     ke paas kya data (variables) aur kya actions (functions/methods) honge.
   - Technical Point: Class likhne se RAM mein actual data ke liye koi memory 
     allocate nahi hoti.

2. OBJECT KYA HAI? (Real Entity / Actual Ghar)
   - Object us nakshe (Class) se banaya gaya actual ghar hai jo zameen (RAM) par 
     jagah leta hai.
   - Isko hum Class ka "Instance" bhi bolte hain.
   - Har object ke paas 3 main cheezein hoti hain:
     1. State (Attributes/Data): Object ke paas kya value hai (jaise: roll_no, name).
     2. Behavior (Methods): Object kya kaam kar sakta hai (jaise: study(), exam()).
     3. Identity (Unique Memory Address): RAM ke andar object ka apna unique address 
        jo `id(obj)` se pata chalta hai.

--------------------------------------------------------------------------------
🎯 INTERVIEW Q&A (Point-to-Point):

Q1: Class aur Object mein 1 line ka main farak kya hai?
Ans: "Class ek design/template hai jo logic define karti hai, jabki Object us design 
     ka real memory instance hai jo data hold karta hai."

Q2: Kya ek class se multiple objects ban sakte hain?
Ans: Haan, ek single blueprint se hazaron alag-alag objects banaye ja sakte hain, aur 
     sabka memory address (`id`) alag hoga.

Q3: Python mein class khud kya hai?
Ans: Python mein "Everything is an object". Class khud bhi ek object hai jo 
     metaclass `type` se banti hai.
================================================================================
"""

class Student:
    # 1. Class Variable (Jo sabhi students ke liye common/shared hoga)
    college_name = "Engineering College"

    # 2. Initializer Method (Har naye student ka personal data set karega)
    def __init__(self, name: str, roll_no: int, branch: str):
        # Instance Variables (Har object ka personal data)
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    # 3. Instance Method (Object ka behavior/action)
    def introduce(self):
        return f"Namaste! Mera naam {self.name} hai, Roll No: {self.roll_no}, Branch: {self.branch}."

    def attend_class(self, subject: str):
        return f"{self.name} abhi '{subject}' ki class attend kar raha hai."


# ==============================================================================
# EXECUTION & TESTING
# ==============================================================================
if __name__ == "__main__":
    print("================ OBJECT INSTANTIATION (CREATION) ================\n")

    # Yahan humne blueprint (Student) se 2 real objects banaye
    s1 = Student("Maaz", 101, "CSE")
    s2 = Student("Aman", 102, "IT")

    # Object 1 ka data aur behavior
    print("--- Student 1 Details ---")
    print(s1.introduce())
    print(s1.attend_class("Python OOPs"))
    print(f"s1 ka College: {s1.college_name}")
    print(f"s1 ka RAM Memory Address [id(s1)]: {id(s1)}")

    print("\n--- Student 2 Details ---")
    # Object 2 ka data aur behavior
    print(s2.introduce())
    print(s2.attend_class("Data Structures"))
    print(f"s2 ka College: {s2.college_name}")
    print(f"s2 ka RAM Memory Address [id(s2)]: {id(s2)}")

    print("\n================ PROOF: IDENTITY & METACLASS ================")
    # Proof 1: Dono objects ka address alag hota hai
    print(f"Kya s1 aur s2 ka memory address alag hai?: {id(s1) != id(s2)}")

    # Proof 2: Python mein class khud bhi ek object hai
    print(f"s1 kis class ka instance hai?: {type(s1)}")
    print(f"Student class khud kis cheez ka object hai?: {type(Student)}")
    print("=============================================================")