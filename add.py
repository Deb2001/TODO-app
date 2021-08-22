from tkinter import *
import json

class Add_data():
    def add(self,date,title,desc):   
        new_data={
                date:{
                "title":title,
                "description":desc,
                }
            }
        try:
            with open("data.json", "r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)


        