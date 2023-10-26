from tkinter import *


# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=160, pady=100)



# Label
my_label1 = Label(text="is equal to", font=("Times New Roman", 12, "normal"))
my_label1.grid(column=0, row=1)
my_label2 = Label(text="Miles", font=("Times New Roman", 12, "normal"))
my_label2.grid(column=2, row=0)
my_label3 = Label(text="Km", font=("Times New Roman", 12, "normal"))
my_label3.grid(column=2, row=1)
my_label4 = Label(text="0", font=("Times New Roman", 12, "normal"))
my_label4.grid(column=1, row=1)

# Text

# Text
text = Text(height=1, width=10)
# Cursor in Text
text.focus()
# Adds default text
text.insert(END, "0")
# Gets current value of box in line 1, Character zero
print(text.get("1.0", END))
text.grid(column=1, row=0)


# Button

def update_my_label():
    my_text = text.get("1.0", END)
    my_text.replace("0/", " ")
    final_text = round(int(my_text) * 1.60934, 2)
    my_label4.config(text=final_text)


button1 = Button(text="Calculate", command=update_my_label)
button1.grid(column=1, row=3)


"""
# Entry

entry = Entry(width=10)
entry.grid(column=1, row=0)
"""



# print(entry.configure().keys())
window.mainloop()