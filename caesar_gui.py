import tkinter as tk
from tkinter import messagebox
def encrypt(message,shift):
    encrypted_value = ""
     

    for letter in message:
        if letter.isalpha():
         if letter.isupper() :

            encrypted_value += chr((ord(letter) - ord("A") + shift) % 26 +ord("A"))
         else:
            encrypted_value += chr((ord(letter) - ord("a") + shift)% 26 +ord("a"))   
        else:
            encrypted_value += letter

    return encrypted_value
def decrypt(message,shift):
   return encrypt(message,-shift)
root = tk.Tk()
def encrypt_text():
    try:
        message = message_entry.get()
        if message=="":
           messagebox.showwarning("Warning","Please enter a message!")
           return
        if shift_entry.get()=="":
           messagebox.showwarning("Warning","Please enter a message!")
           return   
        shift = int(shift_entry.get())
        result = encrypt(message,shift)
        result_label.config(text=f"Result:{result}")
        messagebox.showinfo(
            "Encryption Successful",
            f"Encrypted Message:\n\n {result}"
        )
    except ValueError:
       result_label.config(text="Shift must be a number!")
def decrypt_text():
   try:
       message = message_entry.get()
       if message=="":
           messagebox.showwarning("Warning","Please enter a message!")
           return
       if shift_entry.get()=="":
           messagebox.showwarning("Warning","Please enter a message!")
           return   
       shift = int(shift_entry.get())
       result = decrypt(message,shift)
       result_label.config(text=f"Result:{result}")   
       messagebox.showinfo(
           "Decryption Successful",
           f"Decrypted Message:\n\n {result}"
       )
   except ValueError:  
      result_label.config(text="Shift must be a number!")  
def clear_text():
   message_entry.delete(0,tk.END)   
   shift_entry.delete(0,tk.END)
   result_label.config(text="Result:")  
def copy_result():
    result = result_label.cget("text")
    result = result.replace("Result: ", "")

    root.clipboard_clear()
    root.clipboard_append(result)

    messagebox.showinfo("Copied", "Result copied to clipboard!") 
root.title("Caesar Cipher")
root.geometry("500x500")
root.resizable(False,False)
root.configure(bg="#E8F0FE")
heading = tk.Label(
    root,
    text="🔐 Caesar Cipher",
    font = ("Arial",22,"bold"),
    bg = "#E8F0FE",
    fg="#0b5394"
    )
heading.pack(pady=20)
message_label =tk.Label(
    root,
    text = "Enter Message :",
    font=("Arial",11),
    bg="#E8F0FE"
)
message_label.pack()
message_entry = tk.Entry(
    root,
    width = 40,
    font=("Arial",12),
    bd=3
)
message_entry.pack(pady=5)
shift_label = tk.Label(
    root,
    text = "Enter Shift Value :",
    font=("Arial",11),
    bg="#E8F0FE"
)
shift_label.pack()
shift_entry = tk.Entry(
    root,
    width = 10,
    font=("Arial",12),
    bd=3
)
shift_entry.pack(pady=5)
result_label = tk.Label(
    root,
    text = "Result :",
    font = ("Arial",12,"bold"),
    fg="green",
    bg="#E8F0FE"
)
result_label.pack(pady=10)
button_frame = tk.Frame(
   root, bg="#E8F0FE"
)
button_frame.pack(pady=15)
encrypt_button = tk.Button(  
    button_frame,
    text = "Encrypt",
    width = 15,
    command = encrypt_text,
        bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    cursor="hand2"
)
encrypt_button.grid(row=0,column=0,padx=10,pady=10)
decrypt_button = tk.Button(
    button_frame,
    text="Decrypt",
    width=15,
    command=decrypt_text,  
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    cursor="hand2"
)

decrypt_button.grid(row=0,column=1,padx=10,pady=10)
clear_button = tk.Button(
   button_frame,
   text ="Clear",
   width=15,
   command =clear_text,
       bg="#FF9800",
    fg="white",
    font=("Arial", 11, "bold"),
    cursor="hand2"
)
clear_button.grid(row=1,column=0,padx=10,pady=10)
exit_button = tk.Button(
    button_frame,
   text = "Exit",
   width=15,
   command=root.destroy,
   bg="#f44336",
    fg="white",
    font=("Arial", 11, "bold"),
    cursor="hand2"
)
exit_button.grid(row=1,column=1,padx=10,pady=10)
copy_button = tk.Button( 
    button_frame,
    text="Copy Result",
    width=15,
    command=copy_result,
    bg="#9C27B0",
    fg="white",
    font=("Arial",11,"bold"),
    cursor="hand2"
)
copy_button.grid(row=2,column=0,columnspan=2,pady=10)
root.mainloop()