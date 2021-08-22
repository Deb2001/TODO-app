from tkinter import *

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

# Buttons
add_button = Button(text="Add to TODO List", width=13)
add_button.grid(row=4, column=0)
display_button = Button(text="Display today's TODO List")
display_button.grid(row=4, column=1)
search_button = Button(text="🔍", width=2)
search_button.grid(row=4, column=3)

window.mainloop()