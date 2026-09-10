
"""
=============================================================================
TOPIC: 'a' Mode (Append Mode)
=============================================================================
DEFINITION:
- 'a' mode purane data ke aage NAYA DATA JODNE ke liye use hota hai.
- Create_new: HAAN (Agar file nahi hai, to nayi blank file create kar dega).
- Existing_file: HAAN (Purane data ko chhueta bhi nahi, safe rakhta hai).
- Readable: NAHI (Is mode me f.read() nahi chalega).
- Writable: HAAN.
- Cursor Position: Purane content ke theek aakhri me (Previous last).

USE CASE: Logs save karne ke liye ya chat history maintain karne ke liye.
=============================================================================
"""

# Code Implementation:
with open("notes.txt", "a") as f:
    f.write("Line 3: Ye line 'a' mode ne aakhri me jodi hai.\n")
    f.write("Line 4: Purana likha hua safe raha, naya data add ho gaya.\n")

print("03_append_mode: Naya data successfully append ho gaya!")