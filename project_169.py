from tkinter import*
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("classes")
root.geometry("900x900")
list1 = ["button","label","dropdown"]
dropdown1 = ttk.Combobox(root,state="readonly",values=list1)
dropdown1.pack()
class elements:
    def __init__(self):
        print("classes are being used for creating the elements")
    def show_button(self):
        btn = Button(root,text="enter",command=self.show_mesagebox)
        btn.pack(padx=20,pady=20)
    def show_label(self):
        label = Label(root,text="a new label is made using class.",fg="red")
        label.pack()
    def show_dropdown(self):
        list2 = [1,2,3]
        dropdown2 = ttk.Combobox(root,state="readonly",values=list2)
        dropdown2.pack()
    def show_mesagebox(self):
        messagebox.showinfo("text","you haveclicked funtion")
    def choose(self):
        global dropdown
        element= dropdown1.get()
        if(element=="label"):
            self.show_label()
        elif (element=="button"):
            self.show_button()
        elif (element=="dropdown"):
            self.show_dropdown()
        
        
objects = elements()

btn1 = Button(root,text="click to see the descripton",command=objects.choose)
btn1.pack(padx=10,pady=10)

root.mainloop()