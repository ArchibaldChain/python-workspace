import tkinter as tk

root = tk.Tk()
root.geometry('400x300')

txt = tk.StringVar()
label = tk.Label(root, textvariable=txt, background='green', width=30)

label.pack()

ent = tk.Entry(root, width=60)
ent.pack()


def click_here():
    text = ent.get()
    txt.set(text)


btn = tk.Button(root, text='click here', command=click_here)
btn.pack()

root.mainloop()
