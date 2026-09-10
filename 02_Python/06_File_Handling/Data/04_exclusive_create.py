
"""
=============================================================================
TOPIC: 'x' Mode (Exclusive Creation Mode)
=============================================================================
DEFINITION:
- 'x' mode ka matlab hai: "Sirf aur sirf NAYI file create karo".
- Create_new: HAAN (Nayi file create karke usme data likhega).
- Existing_file: NAHI (Agar file pehle se disk par maujood hai, to FileExistsError dega).
- Readable: NAHI.
- Writable: HAAN.
- Cursor Position: Shuruat me rehta hai (0th-index par).

USE CASE: Security ke liye, taaki galti se bhi kisi purani critical file ka 
data overwrite na ho jaye.
=============================================================================
"""

# Code Implementation:
try:
    with open("secret_notes.txt", "x") as f:
        f.write("Ye bilkul brand new secret file hai.\n")
        f.write("Yeh tabhi bani kyunki ye pehle se exist nahi karti thi.\n")
    print("04_exclusive_create: secret_notes.txt successfully create ho gayi!")

except FileExistsError:
    print("04_exclusive_create: File pehle se exist karti hai! Overwrite hone se bacha liya gaya.")