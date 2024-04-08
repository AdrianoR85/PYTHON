import tkinter as tk

window = tk.Tk()
window.geometry("300x150")
window.title("Gerenciador de frases")

frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

label = tk.Label(frame, text='Hello, world')
label.pack(fill='x', expand=True)

phrase_lab = tk.Label(frame, text='Frase')
phrase_lab.pack(fill='x', expand=True)

phrase_inp = tk.Entry(frame)
phrase_inp.pack(fill='x', expand=True)


def click():
    label.config(text=phrase_inp.get())
    phrase_inp.delete(0, tk.END)


button = tk.Button(frame, text='Enviar', command=click)
button.pack(pady=10)

window.mainloop()
