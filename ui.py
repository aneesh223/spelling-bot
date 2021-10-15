import tkinter as tk
import spellingbot as bot

engine = bot.pyttsx3.init()

root = tk.Tk()

canvas = tk.Canvas(root, height=150, width=300)
canvas.pack()

frame = tk.Frame(root, bg='#6B5A00')
frame.place(relheight=1, relwidth=1)

btn = tk.Button(frame, text="Ask Word", command=lambda: bot.askword(engine, bot.parsedlst))
btn.pack()

wrd = tk.Entry(frame, width=50, bg='#6B5A00', fg='#FFFFFF')
wrd.pack()

submit = tk.Button(frame, text='Send', padx=10,
                pady=5, fg='#FFFFFF', bg='#6B5A00',
                command=lambda: bot.checkword(engine, wrd.get(), bot.word))
submit.pack()

root.mainloop()