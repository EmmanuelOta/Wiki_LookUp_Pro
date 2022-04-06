from tkinter import *
import wikipedia

root = Tk()
root.title("Krawler")
root.geometry("700x600")
root.resizable(0,0)

def clear():
    global search_bar
    global text
    search_bar.delete(0, END)
    text.delete(1.0, END)



def search():
    global search_bar
    global text

    try:
        search = search_bar.get()
        clear()
        data = wikipedia.summary(search, sentences=20)
        text.insert(END, data)
    
    except Exception as e:
        suggestion = wikipedia.suggest(search)
        data = wikipedia.summary(suggestion, sentences=20)
        text.insert(END, data)
        text.insert(END, e)


canvas = Canvas(root, width=800, height=600)
img = PhotoImage(file="Python/Krawler/kali.png")
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=img)

label_frame = LabelFrame(root, text="Krawler", width=70, bg="grey", font=("Consolas", 15))
label_frame1 = canvas.create_window(350, 10, anchor="n", window=label_frame)

search_bar = Entry(label_frame, width=70)
search_bar.pack()

text = Text(root,fg="white", bg="#363636", font=("Helvetica", 10))
text.config(insertbackground="white")
text1 = canvas.create_window(350, 70, anchor="n", window=text)

clear_btn = Button(root, bg="green", fg="black", width=7, text="Clear", font=("Helvetica", 15), 
                   command=lambda: clear())
clear_btn1 = canvas.create_window(310, 500, window=clear_btn)

search_btn = Button(root, bg="green", fg="black", width=7, text="Search", font=("Helvetica", 15),
                    command=lambda: search())
search_btn1 = canvas.create_window(400, 500, window=search_btn)

root.mainloop()