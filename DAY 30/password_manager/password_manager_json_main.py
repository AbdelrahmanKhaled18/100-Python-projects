from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    try:
        letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        numbers = list('0123456789')
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)

        password = "".join(password_list)
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate password:\n{e}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
        return
    is_ok = messagebox.askokcancel(title=website,
                                   message=f"Save the following details?\n\nEmail: {email}\nPassword: {password}")
    if is_ok:
        try:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}
            except json.JSONDecodeError:
                messagebox.showwarning("Warning", "Data file is corrupted. Starting fresh.")
                data = {}

            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            messagebox.showinfo(title="Success", message="Password saved successfully!")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data:\n{e}")


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    if not website:
        messagebox.showinfo(title="Input Required", message="Please enter the website to search for.")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Data file is corrupted.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message="No details for the website were found.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
try:
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
except Exception as e:
    messagebox.showwarning("Logo Error", f"Could not load logo:\n{e}")
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
