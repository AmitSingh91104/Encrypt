from tkinter import *
import tkinter as tk
from tkinter import messagebox
import base64
import os

global screen
global code
global text

root = Tk()
image = tk.PhotoImage(file="bg.png")
background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title("Secret Message")
root.geometry("500x750+600+1")
root.resizable(False, False)

def reset():
    st.delete(0, tk.END)
    tex.delete(1.0, tk.END)

def decrypt():
    password = st.get()
    if password == "123":
        message = tex.get(1.0, tk.END).strip()
        decoded_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decoded_message)
        decrypted_message = base64_bytes.decode("ascii")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, decrypted_message)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != "123":
        messagebox.showerror("encryption", "Invalid Password")

def encrypt():
    password = st.get()
    if password == "123":
        message = tex.get(1.0, tk.END).strip()
        encoded_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encoded_message)
        encrypted_message = base64_bytes.decode("ascii")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, encrypted_message)

    elif password == "":
        messagebox.showerror("encryption","Input Password")
    elif password != "123":
        messagebox.showerror("encryption","Invalid Password")

icon = PhotoImage(file="logo.png")
root.iconphoto(False, icon)

head = Label(root, text="Encryption or Decryption", font=('arial', 15))
head.place(x=120, y=10)

tex = Text(root, font="Robot 20", bg="White", relief=GROOVE, wrap=WORD, bd=0)
tex.place(x=20, y=50, width=450, height=220)

text1 = Label(root,text="Enter Secret Password",fg="black",font=('arial',15))
text1.place(x=50,y=280)

cod = StringVar()
st = Entry(root, textvariable=cod, width=20, bd=0, font=("arial", 15), show="!")
st.place(x=30,y=315)

cl1 = PhotoImage(file="button_encrypt.png")
cl1_image = Button(root,image=cl1,borderwidth=0,cursor="hand2",bd=1,command=encrypt)
cl1_image.place(x=10, y=350)

cl2 = PhotoImage(file="button_decrypt.png")
cl2_image = Button(root,image=cl2,borderwidth=1,cursor="hand2",bd=0,command=decrypt)
cl2_image.place(x=260, y=350)

cl3 = PhotoImage(file="button_reset.png")
cl3_image = Button(root,image=cl3,borderwidth=0,cursor="hand2",bd=0,command=reset)
cl3_image.place(x=20,y=425)

output_text = tk.Text(root, font=("Roboto", 20), bg="white", relief=tk.GROOVE, wrap=tk.WORD, bd=0)
output_text.place(x=20, y=510, width=450, height=200)

root.mainloop()