import sys

from tkinter import * 

root=Tk()
root.geometry("350x250")
root.title("Text Editor")
root.minsize(height=250, width=350)
root.maxsize(height=250, width=350)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text_info = Text(root, yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH) 

root.mainloop()
