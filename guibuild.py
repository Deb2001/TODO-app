from tkinter import *
from add import Add_data
from search import Find

add=Add_data()
search=Find()

window=Tk()
window.title("TODO")
window.config(padx=40,pady=40)

#logo import
canvas=Canvas(height=200,width=200)
logo=PhotoImage(file="Todo logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

#Labels
date_label=Label(text="Date:")
date_label.grid(row=1,column=0)
title_label=Label(text="Title:")
title_label.grid(row=2,column=0)
description_label=Label(text="Description:")
description_label.grid(row=3,column=0)


#Entries
date_entry=""
title_entry=""
description_entry=""

date_entry = Entry(width=48)
date_entry.grid(row=1, column=1, columnspan=3)
date_entry.insert(0, "22.08.2021")
title_entry = Entry(width=48)
title_entry.grid(row=2, column=1, columnspan=3)
description_entry = Entry(width=48)
description_entry.grid(row=3, column=1, columnspan=3)
search_entry= Entry(width=10)
search_entry.grid(row=4, column=2)
search_entry.insert(0, "22.08.2021")
 
def on_add():
    global date_entry
    global title_entry
    global description_entry
    add.add(date_entry.get(),title_entry.get(),description_entry.get())
    title_entry.delete(0,END)
    description_entry.delete(0,END)

    
def on_search():
    global search_entry
    search.search(search_entry.get())

# Buttons
add_button = Button(text="Add to TODO List", width=13,command=on_add)
add_button.grid(row=4, column=0)
display_button = Button(text="Display today's TODO List")
display_button.grid(row=4, column=1)
search_button = Button(text="🔍", width=2,command=on_search)
search_button.grid(row=4, column=3)

window.mainloop()