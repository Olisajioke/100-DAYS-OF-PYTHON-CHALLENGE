from tkinter import *
from tkinter import messagebox as mb
from random import shuffle, choice, randint
import pyperclip
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

print("Print working directory", os.getcwd())


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v',
                    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters2 = [choice(letters) for _ in range(randint(8, 10))]
    symbols2 = [choice(symbols) for _ in range(randint(2, 4))]
    numbers2 = [choice(numbers) for _ in range(randint(2, 4))]
    final_password1 = letters2 + symbols2 + numbers2
    shuffle(final_password1)
    final_password = "".join(final_password1)

    pw = password_text.get(1.0, END)
    if pw != "":
        password_text.delete(1.0, END)
        password_text.insert(END, chars=final_password)
    else:
        password_text.insert(END, chars=final_password)
    pyperclip.copy(final_password)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40, bg="white")


# Canvas and image
key_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200,  highlightthickness=0, bg="white")
canvas.create_image(100, 110, image=key_image)
canvas.grid(row=0, column=1)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = text_website.get(1.0, END).strip()
    email = email_text.get(1.0, END).strip()
    password = password_text.get(1.0, END).strip()
    final_text = f"{website} | {email} | {password}"
    try:
        if (len(website) == 0) or (len(password) == 0) or (len(email) == 0):
            mb.showwarning(title="Oops", message="Please make sure you didn't leave any field empty!")
        else:
            ask = mb.askokcancel(title=website, message=f"You entered Email: {email}"
                                                    f" Password: {password}. Are they correct?")
            if ask:
                with open("data.txt", "a") as total_file2:
                    total_file2.write(final_text + "\n")
                text_website.delete(1.0, END)
                password_text.delete(1.0, END)
                mb.showinfo(title=website, message=f"Your Email: {email} and"
                                                   f" Password: {password} have been saved successfully")
    except TypeError:
        print("Error")


# Labels
website_label = Label(text="Website:", bg="white", fg="black", highlightthickness=0)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="white", fg="black", highlightthickness=0)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="white", fg="black", highlightthickness=0)
password_label.grid(row=3, column=0)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=40, command=save)
add_button.grid(row=4, column=1, columnspan=3)


# Texts
text_website = Text(height=1, width=35)
text_website.focus()
text_website.grid(row=1, column=1, columnspan=2)
email_text = Text(height=1, width=35)
email_text.insert(END, chars="chijioke914@gmail.com")
email_text.grid(row=2, column=1, columnspan=2)
password_text = Text(height=1, width=21)
password_text.grid(row=3, column=1)

window.mainloop()