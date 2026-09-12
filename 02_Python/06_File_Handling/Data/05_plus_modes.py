"""
========================================================================================
TOPIC: Plus Modes ('r+', 'w+', 'a+', 'x+') - Combined Read & Write
========================================================================================

1. MAIN CONCEPT (+ SYMBOL):
   - Jab kisi mode ke sath '+' lagta hai, to usme READ aur WRITE dono powers aa jati hain.
   - Lekin base rule (ki file delete hogi ya bachegi) wahi purane letter se tay hota hai:

   a) 'r+' (Read + Write):
      - File pehle se honi chahiye (warna FileNotFoundError).
      - Purana data DELETE NAHI HOTA (safe rehta hai).
      - Cursor 0th-index par baithta hai.

   b) 'w+' (Write + Read) [KHATARNAK]:
      - File nahi hai to banayega.
      - Purana data PEHLE HI PURA WIPE OUT (delete) kar deta hai!
      - Cursor 0th-index par baithta hai.

   c) 'a+' (Append + Read):
      - File nahi hai to banayega. Purana data safe rahega.
      - Cursor writing ke liye HAMESHA aakhri (end) mein rehta hai.
      - Read karne ke liye cursor ko wapas shuruat me lana padta hai (seek(0)).

   d) 'x+' (Exclusive Create + Read):
      - Sirf nayi file pe chalega (Purani file hui to FileExistsError dega).
      - Nayi file bana kar read aur write dono ki permission dega.

2. TWO HERO FUNCTIONS:
   - f.tell() : Batata hai ki cursor abhi kaunse byte/number par khada hai.
   - f.seek(0): Cursor ko wapas shuruat (index 0) par bhej deta hai.
========================================================================================
"""

# --- 1. Testing 'w+' (Pehle pura clear karega, fir naya likhega aur padhne dega) ---
print("--- 1. Testing 'w+' ---")
with open("plus_demo.txt", "w+") as f:
    f.write("Batch 2026: Python Full Stack")
    
    # Likhne ke baad cursor text ke aakhri me chala gaya hai
    # Read karne ke liye cursor ko index 0 par lana zaroori hai:
    f.seek(0)
    data = f.read()
    print("Content read from 'w+':", data)


# --- 2. Testing 'r+' (Purana data bacha kar read karega aur modify karne dega) ---
print("\n--- 2. Testing 'r+' ---")
with open("plus_demo.txt", "r+") as f:
    purana_text = f.read()
    print("Purana text jo 'r+' ko mila:", purana_text)
    
    # End me naya text joda:
    f.write(" | Status: Active")
    
    # Wapas shuru me jakar pura text verify kiya:
    f.seek(0)
    print("Modify ke baad updated content:", f.read())


# --- 3. Testing 'a+' (Hamesha last me likhega aur read bhi karega) ---
print("\n--- 3. Testing 'a+' ---")
with open("plus_demo.txt", "a+") as f:
    f.write("\nNew record appended via a+")
    
    # 'a+' me cursor hamesha end me hota hai, isliye seek(0) bina read nahi hoga
    f.seek(0)
    print("Final content after 'a+':\n" + f.read())