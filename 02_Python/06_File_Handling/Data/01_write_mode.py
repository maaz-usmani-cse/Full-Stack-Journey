"""
=============================================================================
TOPIC: 'w' Mode (Write Mode)
=============================================================================
DEFINITION:
- 'w' mode file me data LIKHNE ke liye use hota hai.
- Create_new: HAAN (Agar file pehle se nahi hai, to nayi blank file banayega).
- Existing_file: HAAN (Lekin purana saara data DELETE/OVERWRITE kar dega).
- Readable: NAHI (Is mode me f.read() nahi chalega).
- Writable: HAAN.
- Cursor Position: Shuruat me rehta hai (0th-index par).

NOTE: Yeh destructive mode hai, purana content save nahi rehta.
=============================================================================
"""




with open("notes.txt",'w') as f:
    f.write('ye hamara pehla notes hai ')
    f.write('ya to naya file banata hai  ye ya phir agr file pehle se h to usse meta k shuru s likhgea')

    print('file ban gyi hai bhai successfully')