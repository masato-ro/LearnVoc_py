import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk
import webbrowser

window = tk.Tk()
window.title('背單字v1.0')
window.geometry('500x400')

def callback(url):
    webbrowser.open_new(url)

def about_window():
    window = tk.Toplevel()
    window.title('關於我')
    window.geometry('300x350')
    label = tk.Label(window, text="趕快通過日檢吧!")
    label.place(x=90,y=20)
    img = Image.open('about.png')
    photo = ImageTk.PhotoImage(img)
    imglabel = tk.Label(window, image=photo)
    imglabel.place(x=100, y=50)
    link1 = tk.Label(window, text="官網", fg="blue", cursor="hand2")
    link1.bind("<Button-1>", lambda e: callback("http://www.karltt.com"))
    link1.place(x=130,y=260)
    button1 = tk.Button(window, text="了解了", width=15, command=window.destroy, borderwidth=2, relief="groove")
    button1.place(x=85, y=300)
    window.mainloop()

def question_factory():
    with sqlite3.connect('n3.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT nihongo,kanji,chinese FROM n3 ORDER BY RANDOM() limit 1')
        for row in cur.fetchall():
            global kanji,chinese
            nihongo = row[0]
            kanji = row[1]
            chinese = row[2]
        return nihongo


def clickme():
    var_answer_kanji.set(kanji)
    var_answer.set(chinese)


def next_question():
    var_question.set(question_factory())


def click_reset():
    var_answer_kanji.set('日文漢字')
    var_answer.set('中文解答')


var_answer_kanji = tk.StringVar()
var_answer_kanji.set('日文漢字')

var_answer = tk.StringVar()
var_answer.set('中文解答')

var_question = tk.StringVar()
var_question.set(question_factory())

putsubject = tk.Label(window,bg='lavender', font=('', 28), textvariable=var_question, borderwidth=2, relief="sunken")
putsubject.place(x=50, y=80)

q_frame = ttk.LabelFrame(window, text=" Answer ",padding=10, relief="groove")
q_frame.place(x=50, y=200)
label0 = tk.Label(q_frame, font=('', 16), textvariable=var_answer_kanji)
label0.grid(column=0, row=0,sticky=tk.W)
label1 = tk.Label(q_frame,font=('', 20), textvariable=var_answer,borderwidth=2, relief="groove")
label1.grid(column=0, row=1,sticky=tk.W)

answer1 = tk.Button(window, text='解答', width=5, height=1, command=clickme, borderwidth=2, relief="groove")
answer1.place(x=40, y=340)
answer2 = tk.Button(window, text="下一題", width=5, height=1, command=next_question,borderwidth=2, relief="groove")
answer2.place(x=110, y=340)
answer3 = tk.Button(window, text="reset", width=5, height=1, command=click_reset,borderwidth=2, relief="groove")
answer3.place(x=240, y=340)

button1 = tk.Button(window, text="離開", width=15, command=window.destroy, borderwidth=2, relief="groove")
button1.place(x=340, y=340)
button2 = tk.Button(window, text="關於我", width=15, command=about_window, borderwidth=2, relief="groove")
button2.place(x=340, y=300)

window.mainloop()