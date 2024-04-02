import tkinter as tk
import hashlib
import pyperclip

pyperclip.copy('The text to be copied to the clipboard.')
pyperclip.paste()

def handle_click():
  text = text_area.get("0.0", tk.END)
  if len(text) > 3:
    text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    text_output.config(text=text_hash)
    
def copy_to_clipboard(event):
  text = text_output.cget("text")  # Obter texto do text_output
  if len(text) > 3:
    pyperclip.copy(text)

window = tk.Tk()
window.geometry('500x280')
window.title("Cryptography")

frame = tk.Frame(window)
frame.pack(padx=30, pady=30)

label = tk.Label(frame, text="Type the text: ")
label.pack(expand=True)

text_area = tk.Text(frame, height=5)
text_area.pack(fill="x", expand=True)
text_area.configure(padx=10, pady=10)

button = tk.Button(frame, text="Click to", command=handle_click)
button.pack(padx='10', pady='10', expand=True)

text_output = tk.Label(frame, text="")
text_output.pack(expand=True)

text_output = tk.Label(frame, text="\nClick to Copy")
text_output.pack(expand=True)
text_output.bind('<Button-1>',  copy_to_clipboard)
window.mainloop()

