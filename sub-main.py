from tkinter import *
from tkinter import messagebox
import json
class Find():
    def __init__(self):
        pass
    def search(self,date):
        
        try:
            with open("data.json") as data_file:
                data=json.load(data_file)
            
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        
        else:
            if date in data:
                title=data[date]["title"]
                description=data[date]["description"]
                messagebox.showinfo(title=date, message=f"Tile:{title}\nDescription:{description}")
                

            else:
                messagebox.showinfo(title="Error",message="No such todo exist")
        


    win=Tk()
    win.title("MAIN")
    button=Button(text="Search", command=search)
    button.pack()
    win.mainloop()