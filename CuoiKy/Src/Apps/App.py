import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
# thu vien xu ly anh
import cv2
import PIL.Image, PIL.ImageTk
# thu vien xu ly duong dan
# import sys
# sys.path.append('../Apps/img/')


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Load an image using OpenCV
        cv_img = cv2.imread("Apps/img/d.png")
        cv_img = cv2.blur(cv_img, (45,45 ))
        self.canvas = tk.Canvas(self.master, width = 800, height = 600)
        self.canvas.pack()
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)


        self.label = tk.Label(text="Danh bạ")
        self.label.pack()
        self.label.place(x=10, y=10, width=70, height=30)

        self.txb = tk.Entry()
        self.txb.pack()
        self.txb.place(x=90, y=10, width=300, height=30)
        self.bt = tk.Button(bg="#C9DCEA")
        self.bt['text'] = 'Nhấn vào'
        self.bt['command']=self.event1
        self.bt.pack()
        self.bt.place(x=400, y=10, width=100, height=30)

        self.all_comboboxes = []
        self.cb = ttk.Combobox(self.master, values=("1", "2", "3", "4", "5"))
        self.cb.set("1")
        self.cb.pack()
        self.cb.place(x=90, y=50, width=300, height=30)
        self.cb.bind('<<ComboboxSelected>>', self.on_select)
        self.all_comboboxes.append(self.cb)



    def on_select(self,event=None):
        if event: # <-- this works only with bind because `command=` doesn't send event
            print("event.widget:", event.widget.get())
        for i, x in enumerate(self.all_comboboxes):
            print("all_comboboxes[%d]: %s" % (i, x.get()))
        self.label.place(x=10, y=10, width=70, height=30)

    def event1(self,event=None):
        print(self.txb.get())
        #messagebox.showinfo("Danh Bạ",self.txb.get())
        self.label.place(x=-100, y=10, width=70, height=30)

app = Application(master=tk.Tk())
app.master.title('Ung Dung Moi')
app.master.minsize(800, 500)
app.mainloop()
