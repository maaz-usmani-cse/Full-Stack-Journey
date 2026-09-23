"""
================================================================================
TOPIC: Object Creation Lifecycle - __new__ vs __init__
================================================================================

🧠 SIR KA CONCEPT (ASLI KAHANI):
Jab bhi hum kisi class ka object banate hain, jaise:
    obj = Student("Rahul")

Toh log samajhte hain ki sirf __init__ chalta hai, LEKIN AISA NAHI HAI!
Backend mein 2 special methods ek ke baad ek execute hote hain:

  STEP 1: __new__(cls, ...)   ---> OBJECT CREATOR (Pehle ye chalta hai)
  STEP 2: __init__(self, ...)  ---> OBJECT INITIALIZER (Fir ye chalta hai)

--------------------------------------------------------------------------------
1. Step 1: __new__(cls, name)
   - Kaam: Yeh Python ka asli 'Constructor' hai. Iska kaam hai RAM mein nayi jagah 
           (Memory space) book karna aur object create karna.
   - Parameter: Iska pehla parameter `cls` hota hai (matlab class khud).
   - Return: Yeh banaye gaye naye object (instance) ko RETURN karta hai.
   - super().__new__(cls): Hum base class (object) ke __new__ ko bolte hain ki 
     bhai is class ke liye RAM mein naya dabba bana do.

--------------------------------------------------------------------------------
2. Step 2: __init__(self, name)
   - Kaam: Jab __new__ ne memory dabba bana kar return kar diya, tab __init__ chalta hai.
           Iska kaam hai us khali dabbe ke andar values/attributes bharna.
   - Parameter: Iska pehla parameter `self` hota hai. Ye `self` wahi instance hai jo 
     __new__ ne abhi-abhi bana kar return kiya tha!
   - Return: Yeh kuch return NAHI karta (sirf None return karta hai). Agar return likhoge 
     toh TypeError aayega.

--------------------------------------------------------------------------------
🔍 PROOF OF EXECUTION (id() ka khel):
__new__ ke andar instance ka memory address `id(instance)` aur 
__init__ ke andar `id(self)` BILKUL SAME hota hai.
Iska matlab object pehle hi ban chuka hota hai, __init__ sirf usme data daalta hai.

--------------------------------------------------------------------------------
🎯 INTERVIEW Q&A:
Q: Kya bina __new__ ke __init__ chal sakta hai?
Ans: Nahi! Agar __new__ instance return nahi karega, toh __init__ call hi nahi hoga.

Q: In dono ka main difference 1 line mein batao?
Ans: "__new__ creates the object in memory, while __init__ initializes its values."
================================================================================
"""

class Student:
    # 1. Pehle ye chalega (Memory banayega)
    def __new__(cls, name):
        print("\n--- [STEP 1] __new__ EXECUTE HUA ---")
        print("1. RAM mein naya memory block allocate ho raha hai...")
        
        # super().__new__(cls) se actual memory allocate hoti hai
        instance = super().__new__(cls)
        
        print(f"2. Naya Object ban gaya! Memory ID (Address): {id(instance)}")
        print("3. Ab __new__ is instance ko __init__ ke paas bhej raha hai...\n")
        
        return instance  # Yeh instance ab neeche self ban kar jayega

    # 2. Memory banne ke baad ye chalega (Values bharega)
    def __init__(self, name):
        print("--- [STEP 2] __init__ EXECUTE HUA ---")
        print(f"1. self ka Memory ID dekho: {id(self)}")
        print("   (Dhyan do: __new__ aur self ka ID bilkul SAME hai!)")
        
        # Instance attribute initialize karna
        self.stu_name = name
        print(f"2. Object values initialize ho gayi: stu_name = '{self.stu_name}'")


# ==============================================================================
# EXECUTION & TESTING
# ==============================================================================
if __name__ == "__main__":
    print("================ OBJECT CREATION START ================")
    # Jaise hi humne Student("Rahul") call kiya, pehle __new__ chala fir __init__
    obj1 = Student("Rahul")
    
    print("\n================ FINAL VERIFICATION ================")
    print(f"Bahar jo 'obj1' variable mila uska Memory ID: {id(obj1)}")
    print(f"Student ka naam: {obj1.stu_name}")
    print("=====================================================")