"""
=============================================================================
TOPIC: 'r' Mode (Read Mode) - Default Mode
=============================================================================
DEFINITION:
- 'r' mode file ke content ko SIRF PADHNE ke liye use hota hai.
- Create_new: NAHI (Agar file exist nahi karti, to FileNotFoundError dega).
- Existing_file: HAAN (File pehle se hard drive par honi zaroori hai).
- Readable: HAAN.
- Writable: NAHI (Is mode me f.write() nahi chalega, error aayega).
- Cursor Position: Shuruat me rehta hai (0th-index par).
=============================================================================
"""



with open('notes.txt' ,'r') as f:
    content=f.read()
    print("--- notes.txt ka content neeche hai ---")
    print(content)






# try:
#     with open("notes.txt", "r") as f:
#         content = f.read()
#         print("--- notes.txt ka content neeche hai ---")
#         print(content)
# except FileNotFoundError:
#     print("Error: File nahi mili! Pehle 01_write_mode.py run karke file banayein.")