from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Matching Game")
root.wm_iconbitmap("C:\\Users\\lucas\\source\\repos\\Matching Game\\Matching Game\\match_head.ico")

pairs = 0
pairlist = [1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(pairlist)

frame = Frame(root)
frame.pack()

count = 0
answer_list = []
answer_dict = {}

def winner():
    messagebox.showinfo("Congrats!", "You won!")
    blist = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]
    for b in blist:
        b.config(bg="green")

def button_click(b, num):
    global count, answer_list, answer_dict, pairs
    if b["text"] == '' and count < 2:
        b["text"] = pairlist[num-1]
        answer_list.append(num-1)
        answer_dict[b] = pairlist[num-1]
        count += 1
    if len(answer_list) == 2:
        if pairlist[answer_list[0]] == pairlist[answer_list[1]]:
            messagebox.showinfo("Correct", "Match found!")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_list = []
            answer_dict = {}
            pairs += 1
            if pairs == 6:
                winner()
        else:
            count = 0
            answer_list = []
            messagebox.showinfo("Incorrect", "Not a match.")
            for key in answer_dict:
                key["text"] = ""
            answer_dict = {}


b1 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b1, 1), relief="sunken")
b1.grid(row=0, column=0)
b2 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b2, 2), relief="sunken")
b2.grid(row=0, column=1)
b3 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b3, 3), relief="sunken")
b3.grid(row=0, column=2)
b4 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b4, 4), relief="sunken")
b4.grid(row=0, column=3)
b5 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b5, 5), relief="sunken")
b5.grid(row=1, column=0)
b6 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b6, 6), relief="sunken")
b6.grid(row=1, column=1)
b7 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b7, 7), relief="sunken")
b7.grid(row=1, column=2)
b8 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b8, 8), relief="sunken")
b8.grid(row=1, column=3)
b9 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b9, 9), relief="sunken")
b9.grid(row=2, column=0)
b10 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b10, 10), relief="sunken")
b10.grid(row=2, column=1)
b11 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b11, 11), relief="sunken")
b11.grid(row=2, column=2)
b12 = Button(frame, text='', height=15, width=20, command=lambda: button_click(b12, 12), relief="sunken")
b12.grid(row=2, column=3)

root.mainloop()
