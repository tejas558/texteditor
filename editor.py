import sys

from tkinter import * 

root=Tk()
root.geometry("500x500")
root.title("Text Editor")
root.minsize(height=500, width=500)
root.maxsize(height=500, width=500)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text_info = Text(root, yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH) 

root.mainloop()
