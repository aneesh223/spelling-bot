import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height=150, width=300)
canvas.pack()

frame = tk.Frame(root, bg='#6B5A00')
frame.place(relheight=1, relwidth=1)

wrd = tk.Entry(frame, width=50, bg='#6B5A00', fg='#FFFFFF')
wrd.pack()

submit = tk.Button(frame, text='Send', padx=10,
                 pady=5, fg='#FFFFFF', bg='#6B5A00',
                 command=lambda: print(wrd.get))
submit.pack()

root.mainloop()