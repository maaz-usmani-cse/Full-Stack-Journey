"""
================================================================================
TOPIC: Class Variables (Static Variables) & Class Methods (@classmethod)
================================================================================

🧠 ASLI INTERVIEW DEFINITIONS (HINGLISH MEIN):

1. CLASS VARIABLE KYA HOTA HAI?
   - Class Variable wo variable hota hai jo CLASS LEVEL par banta hai, na ki kisi 
     single object ke liye.
   - Yeh "OBJECT INDEPENDENT VARIABLE" hota hai. Iska matlab yeh saare objects 
     ke liye COMMON (SHARED) hota hai.
   - Memory Benefit: Har object ke liye alag se naya dabba nahi banta; poori class 
     ke liye RAM mein sirf 1 copy banti hai jo sabhi share karte hain.

2. CLASS VARIABLE DECLARE KARNE KE 4 TARIQE (Sir Ne Live Code Mein Padhaya):
   Tareeqa 1: Inside Class (Directly outside any method)
      - Example: stu_class = "10th"
   Tareeqa 2: Inside Constructor (__init__ ke andar)
      - Syntax: ClassName.variable_name = value
      - Example: Student.stu_city = "Bhopal"
   Tareeqa 3: Inside Instance Method
      - Syntax: ClassName.variable_name = value
      - Example: Student.stu_country = "India"
   Tareeqa 4: Inside Class Method (@classmethod ke andar)
      - Syntax: cls.variable_name = value
      - Example: cls.stu_state = "Madhya Pradesh"

3. CLASS METHOD KYA HOTA HAI?
   - Aisa method jo class ke state/variables ke sath deal karta hai, na ki object ke sath.
   - Pehchan:
     1. Iske upar `@classmethod` decorator lagana compulsory hota hai.
     2. Iska pehla parameter hamesha `cls` hota hai (jo poori class ko point karta hai).
   - Calling: Isko Class ke naam se bhi call kar sakte hain (`Student.method()`) aur 
     object ke reference se bhi (`obj.method()`).

--------------------------------------------------------------------------------
🎯 INTERVIEW TRAP QUESTIONS & DEEP CONCEPTS:

Q1: Class Variable aur Instance Variable mein sabse bada difference kya hai?
Ans: Instance variable har object ka apna personal data hota hai (`self.name`), jabki 
     Class variable sabhi objects ke liye common/shared hota hai (`Student.school_city`).

Q2: Class method mein `cls` parameter ka kya matlab hota hai?
Ans: Jaise instance method mein `self` current OBJECT ko point karta hai, waise hi class 
     method mein `cls` current CLASS ko point karta hai.

Q3: Agar hum object ke through Class Variable ko modify karein (`obj.stu_class = "12th"`), 
    toh kya doosre objects ke liye bhi badlega?
Ans: NAHI! Yeh sabse bada interview trap hai. Agar tum `obj.stu_class = "12th"` likhoge, 
     toh class variable modify nahi hoga, balki us particular object ka ek naya INSTANCE 
     VARIABLE ban jayega! Class variable ko sach mein badalne ke liye `Student.stu_class = "12th"` 
     ya Class Method ke through hi modify karna chahiye.

Q4: Class variable ko access karne ke kitne tareeqe hain?
Ans: 
     1. Inside class direct: `print(stu_class)` (sirf class body mein directly access hota hai).
     2. Class name ke through (Recommended): `Student.stu_city`.
     3. Object reference ke through: `obj.stu_city`.
================================================================================
"""

class Student:
    # -------------------------------------------------------------------------
    # Tareeqa 1: Inside Class body directly (Outside methods)
    # -------------------------------------------------------------------------
    stu_class = "10th"  # Class Variable 1

    # Class body ke andar direct call karke print karna
    print(stu_class)  # Output: 10th (Class load hote hi chal jata hai)

    def __init__(self, name: str, age: int, email: str):
        # Instance Variables (har object ka apna alag data)
        self.stu_name = name
        self.stu_age = age
        self.stu_email = email

        # ---------------------------------------------------------------------
        # Tareeqa 2: Inside Constructor (__init__) using ClassName
        # ---------------------------------------------------------------------
        Student.stu_city = "Bhopal"  # Class Variable 2

        # Constructor ke andar Class variable ko access/print karna
        print(Student.stu_class)
        print(Student.stu_city)

    def student_details(self, contact: str):
        # Instance variable
        self.stu_contact = contact

        # ---------------------------------------------------------------------
        # Tareeqa 3: Inside Instance Method using ClassName
        # ---------------------------------------------------------------------
        Student.stu_country = "India"  # Class Variable 3

    # -------------------------------------------------------------------------
    # Tareeqa 4: Inside Class Method using @classmethod & cls
    # -------------------------------------------------------------------------
    @classmethod
    def student_class_method(cls, new_class: str = None):
        # cls ke through Class Variable declare karna
        cls.stu_state = "Madhya Pradesh"  # Class Variable 4

        # Agar new_class pass kiya gaya ho toh modify karna
        if new_class:
            cls.stu_class = new_class


# ==============================================================================
# EXECUTION & PROOF
# ==============================================================================
if __name__ == "__main__":
    print("\n================ 1. OBJECT BANAYENGE ================")
    # Constructor chalega, Bhopal aur 10th print hoga
    obj = Student("Neeraj", 37, "nee@gmail.com")

    print("\n================ 2. INSTANCE METHOD CALL ================")
    # Ab student_details method chalega aur stu_country set ho jayega
    obj.student_details("1234567890")
    print(f"Class Variable from outside: {Student.stu_country}")

    print("\n================ 3. CLASS METHOD CALL ================")
    # Class method ko direct Class Name se call kar rahe hain
    Student.student_class_method()
    print(f"State set via Class Method: {Student.stu_state}")

    print("\n================ 4. ALL CLASS VARIABLES SUMMARY ================")
    print("Class Name ke through:")
    print(f"Class:   {Student.stu_class}")
    print(f"City:    {Student.stu_city}")
    print(f"Country: {Student.stu_country}")
    print(f"State:   {Student.stu_state}")

    print("\nObject Reference ke through access karna:")
    print(f"obj.stu_class:   {obj.stu_class}")
    print(f"obj.stu_city:    {obj.stu_city}")

    print("\n================ 5. MODIFYING CLASS VARIABLE ================")
    # Class Method se class variable update karte hain
    Student.student_class_method(new_class="12th")
    print(f"Updated Class: {Student.stu_class}")
    print(f"Object par reflect hua?: {obj.stu_class}")  # Output: 12th
    print("================================================================")


