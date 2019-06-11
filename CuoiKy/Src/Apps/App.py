import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
# thu vien xu ly anh
import cv2
import PIL.Image, PIL.ImageTk
# thu vien xu ly duong dan
import sys
sys.path.append('../BUS/')
import Multivariable_Regression as MR


tinhToan=[]
isAll=[]
ve=[]


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Load an image using OpenCV
        cv_img = cv2.imread("img/d.png")
        cv_img = cv2.blur(cv_img, (45,45 ))
        self.canvas = tk.Canvas(self.master, width = 800, height = 600)
        self.canvas.pack()
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
#######################################################################################
        self.ketQua_bt = tk.Button(bg="#ffffff")
        self.ketQua_bt.pack()
        self.ketQua_bt.place(x=250, y=300, width=300, height=100)
        ###################################
        self.tinhToan_bt = tk.Button(bg="#C9DCEA")
        self.tinhToan_bt['text'] = 'Tính'
        self.tinhToan_bt['command']=self.tinhToan_bt_Click
        self.tinhToan_bt.pack()
        self.tinhToan_bt.place(x=252, y=420, width=90, height=50)
        ###
        self.ve2d_bt = tk.Button(bg="#C9DCEA")
        self.ve2d_bt['text'] = 'Vẽ 2d'
        self.ve2d_bt['command']=self.ve2d_Click
        self.ve2d_bt.pack()
        self.ve2d_bt.place(x=352, y=420, width=90, height=50)
        ###
        self.ve3d_bt = tk.Button(bg="#C9DCEA")
        self.ve3d_bt['text'] = 'Vẽ 3d'
        self.ve3d_bt['command']=self.ve3d_Click
        self.ve3d_bt.pack()
        self.ve3d_bt.place(x=452, y=420, width=90, height=50)
##########################################################################################
        self.MR_label = tk.Label(text="MR",bg="#FEB857")
        self.MR_label.pack()
        self.MR_label.place(x=260, y=5, width=280, height=60)
        self.MR_label.config(font=("Courier bold", 40))
        self.dactrungtinh_label = tk.Label(text="Chọn đặc trưng tính toán",bg="#FEB857")
        self.dactrungtinh_label.pack()
        self.dactrungtinh_label.place(x=30, y=10, width=280, height=30)
        ##############################
        self.Age_bt = tk.Button(bg="#C9DCEA")
        self.Age_bt['text'] = 'Age'
        self.Age_bt['command']=self.Age_Click
        self.Age_bt.pack()
        self.Age_bt.place(x=30, y=50, width=70, height=30)
        ###
        self.Weight_bt = tk.Button(bg="#C9DCEA")
        self.Weight_bt['text'] = 'Weight'
        self.Weight_bt['command']=self.Weight_Click
        self.Weight_bt.pack()
        self.Weight_bt.place(x=100, y=50, width=70, height=30)
        ###
        self.Height_bt = tk.Button(bg="#C9DCEA")
        self.Height_bt['text'] = 'Height'
        self.Height_bt['command']=self.Height_Click
        self.Height_bt.pack()
        self.Height_bt.place(x=170, y=50, width=70, height=30)
        ###
        self.Neck_bt = tk.Button(bg="#C9DCEA")
        self.Neck_bt['text'] = 'Neck'
        self.Neck_bt['command']=self.Neck_Click
        self.Neck_bt.pack()
        self.Neck_bt.place(x=240, y=50, width=70, height=30)
        ####
        self.Chest_bt = tk.Button(bg="#C9DCEA")
        self.Chest_bt['text'] = 'Chest'
        self.Chest_bt['command']=self.Chest_Click
        self.Chest_bt.pack()
        self.Chest_bt.place(x=30, y=80, width=70, height=30)
        ####
        self.Abdomen_bt = tk.Button(bg="#C9DCEA")
        self.Abdomen_bt['text'] = 'Abdomen'
        self.Abdomen_bt['command']=self.Abdomen_Click
        self.Abdomen_bt.pack()
        self.Abdomen_bt.place(x=100, y=80, width=70, height=30)
        ####
        self.Hip_bt = tk.Button(bg="#C9DCEA")
        self.Hip_bt['text'] = 'Hip'
        self.Hip_bt['command']=self.Hip_Click
        self.Hip_bt.pack()
        self.Hip_bt.place(x=170, y=80, width=70, height=30)
        ####
        self.Thigh_bt = tk.Button(bg="#C9DCEA")
        self.Thigh_bt['text'] = 'Thigh'
        self.Thigh_bt['command']=self.Thigh_Click
        self.Thigh_bt.pack()
        self.Thigh_bt.place(x=240, y=80, width=70, height=30)
        ####
        self.Knee_bt = tk.Button(bg="#C9DCEA")
        self.Knee_bt['text'] = 'Knee'
        self.Knee_bt['command']=self.Knee_Click
        self.Knee_bt.pack()
        self.Knee_bt.place(x=30, y=110, width=70, height=30)
        ####
        self.Ankle_bt = tk.Button(bg="#C9DCEA")
        self.Ankle_bt['text'] = 'Ankle'
        self.Ankle_bt['command']=self.Ankle_Click
        self.Ankle_bt.pack()
        self.Ankle_bt.place(x=100, y=110, width=70, height=30)
        ####
        self.Biceps_bt = tk.Button(bg="#C9DCEA")
        self.Biceps_bt['text'] = 'Biceps'
        self.Biceps_bt['command']=self.Biceps_Click
        self.Biceps_bt.pack()
        self.Biceps_bt.place(x=170, y=110, width=70, height=30)
        ####
        self.Forearm_bt = tk.Button(bg="#C9DCEA")
        self.Forearm_bt['text'] = 'Forearm'
        self.Forearm_bt['command']=self.Forearm_Click
        self.Forearm_bt.pack()
        self.Forearm_bt.place(x=240, y=110, width=70, height=30)
        ####
        self.Wrist_bt = tk.Button(bg="#C9DCEA")
        self.Wrist_bt['text'] = 'Wrist'
        self.Wrist_bt['command']=self.Wrist_Click
        self.Wrist_bt.pack()
        self.Wrist_bt.place(x=30, y=140, width=70, height=30)
        ####
        self.All_bt = tk.Button(bg="#C9DCEA")
        self.All_bt['text'] = 'All'
        self.All_bt['command']=self.All_Click
        self.All_bt.pack()
        self.All_bt.place(x=100, y=140, width=70, height=30)
##########################################################################################
        self.dactrungtinh2_label = tk.Label(text="Chọn đặc trưng vẽ",bg="#FEB857")
        self.dactrungtinh2_label.pack()
        self.dactrungtinh2_label.place(x=480, y=10, width=280, height=30)
        self.Age2_bt = tk.Button(bg="#C9DCEA")
        self.Age2_bt['text'] = 'Age'
        self.Age2_bt['command']=self.Age2_Click
        self.Age2_bt.pack()
        self.Age2_bt.place(x=480, y=50, width=70, height=30)
        ###
        self.Weight2_bt = tk.Button(bg="#C9DCEA")
        self.Weight2_bt['text'] = 'Weight'
        self.Weight2_bt['command']=self.Weight2_Click
        self.Weight2_bt.pack()
        self.Weight2_bt.place(x=550, y=50, width=70, height=30)
        ###
        self.Height2_bt = tk.Button(bg="#C9DCEA")
        self.Height2_bt['text'] = 'Height'
        self.Height2_bt['command']=self.Height2_Click
        self.Height2_bt.pack()
        self.Height2_bt.place(x=620, y=50, width=70, height=30)
        ###
        self.Neck2_bt = tk.Button(bg="#C9DCEA")
        self.Neck2_bt['text'] = 'Neck'
        self.Neck2_bt['command']=self.Neck2_Click
        self.Neck2_bt.pack()
        self.Neck2_bt.place(x=690, y=50, width=70, height=30)
        ####
        self.Chest2_bt = tk.Button(bg="#C9DCEA")
        self.Chest2_bt['text'] = 'Chest'
        self.Chest2_bt['command']=self.Chest2_Click
        self.Chest2_bt.pack()
        self.Chest2_bt.place(x=480, y=80, width=70, height=30)
        ####
        self.Abdomen2_bt = tk.Button(bg="#C9DCEA")
        self.Abdomen2_bt['text'] = 'Abdomen'
        self.Abdomen2_bt['command']=self.Abdomen2_Click
        self.Abdomen2_bt.pack()
        self.Abdomen2_bt.place(x=550, y=80, width=70, height=30)
        ####
        self.Hip2_bt = tk.Button(bg="#C9DCEA")
        self.Hip2_bt['text'] = 'Hip'
        self.Hip2_bt['command']=self.Hip2_Click
        self.Hip2_bt.pack()
        self.Hip2_bt.place(x=620, y=80, width=70, height=30)
        ####
        self.Thigh2_bt = tk.Button(bg="#C9DCEA")
        self.Thigh2_bt['text'] = 'Thigh'
        self.Thigh2_bt['command']=self.Thigh2_Click
        self.Thigh2_bt.pack()
        self.Thigh2_bt.place(x=690, y=80, width=70, height=30)
        ####
        self.Knee2_bt = tk.Button(bg="#C9DCEA")
        self.Knee2_bt['text'] = 'Knee'
        self.Knee2_bt['command']=self.Knee2_Click
        self.Knee2_bt.pack()
        self.Knee2_bt.place(x=480, y=110, width=70, height=30)
        ####
        self.Ankle2_bt = tk.Button(bg="#C9DCEA")
        self.Ankle2_bt['text'] = 'Ankle'
        self.Ankle2_bt['command']=self.Ankle2_Click
        self.Ankle2_bt.pack()
        self.Ankle2_bt.place(x=550, y=110, width=70, height=30)
        ####
        self.Biceps2_bt = tk.Button(bg="#C9DCEA")
        self.Biceps2_bt['text'] = 'Biceps'
        self.Biceps2_bt['command']=self.Biceps2_Click
        self.Biceps2_bt.pack()
        self.Biceps2_bt.place(x=620, y=110, width=70, height=30)
        ####
        self.Forearm2_bt = tk.Button(bg="#C9DCEA")
        self.Forearm2_bt['text'] = 'Forearm'
        self.Forearm2_bt['command']=self.Forearm2_Click
        self.Forearm2_bt.pack()
        self.Forearm2_bt.place(x=690, y=110, width=70, height=30)
        ####
        self.Wrist2_bt = tk.Button(bg="#C9DCEA")
        self.Wrist2_bt['text'] = 'Wrist'
        self.Wrist2_bt['command']=self.Wrist2_Click
        self.Wrist2_bt.pack()
        self.Wrist2_bt.place(x=480, y=140, width=70, height=30)
        ###
    # def on_select(self,event=None):
    #     if event: # <-- this works only with bind because `command=` doesn't send event
    #         print("event.widget:", event.widget.get())
    #     for i, x in enumerate(self.all_comboboxes):
    #         print("all_comboboxes[%d]: %s" % (i, x.get()))
    #     self.label.place(x=10, y=10, width=70, height=30)
    def Age_Click(self,event=None):
        if 'Age' not in tinhToan:
            tinhToan.append('Age')
            self.Age_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Age')
            self.Age_bt.config(bg="#C9DCEA")
    def Weight_Click(self,event=None):
        if 'Weight' not in tinhToan:
            tinhToan.append('Weight')
            self.Weight_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Weight')
            self.Weight_bt.config(bg="#C9DCEA")
    def Height_Click(self,event=None):
        if 'Height' not in tinhToan:
            tinhToan.append('Height')
            self.Height_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Height')
            self.Height_bt.config(bg="#C9DCEA")
    def Neck_Click(self,event=None):
        if 'Neck' not in tinhToan:
            tinhToan.append('Neck')
            self.Neck_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Neck')
            self.Neck_bt.config(bg="#C9DCEA")
    def Chest_Click(self,event=None):
        if 'Chest' not in tinhToan:
            tinhToan.append('Chest')
            self.Chest_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Chest')
            self.Chest_bt.config(bg="#C9DCEA")
    def Abdomen_Click(self,event=None):
        if 'Abdomen' not in tinhToan:
            tinhToan.append('Abdomen')
            self.Abdomen_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Abdomen')
            self.Abdomen_bt.config(bg="#C9DCEA")
    def Hip_Click(self,event=None):
        if 'Hip' not in tinhToan:
            tinhToan.append('Hip')
            self.Hip_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Hip')
            self.Hip_bt.config(bg="#C9DCEA")
    def Thigh_Click(self,event=None):
        if 'Thigh' not in tinhToan:
            tinhToan.append('Thigh')
            self.Thigh_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Thigh')
            self.Thigh_bt.config(bg="#C9DCEA")
    def Knee_Click(self,event=None):
        if 'Knee' not in tinhToan:
            tinhToan.append('Knee')
            self.Knee_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Knee')
            self.Knee_bt.config(bg="#C9DCEA")
    def Ankle_Click(self,event=None):
        if 'Ankle' not in tinhToan:
            tinhToan.append('Ankle')
            self.Ankle_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Ankle')
            self.Ankle_bt.config(bg="#C9DCEA")
    def Biceps_Click(self,event=None):
        if 'Biceps' not in tinhToan:
            tinhToan.append('Biceps')
            self.Biceps_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Biceps')
            self.Biceps_bt.config(bg="#C9DCEA")
    def Forearm_Click(self,event=None):
        if 'Forearm' not in tinhToan:
            tinhToan.append('Forearm')
            self.Forearm_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Forearm')
            self.Forearm_bt.config(bg="#C9DCEA")
    def Wrist_Click(self,event=None):
        if 'Wrist' not in tinhToan:
            tinhToan.append('Wrist')
            self.Wrist_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Wrist')
            self.Wrist_bt.config(bg="#C9DCEA")
    def All_Click(self,event=None):
        if 1 not in isAll:
            t=['Age','Weight','Height','Neck','Chest','Abdomen','Hip','Thigh','Knee','Ankle','Biceps','Forearm','Wrist']
            for i in t:
                if i not in tinhToan:
                    tinhToan.append(i)
            self.Age_bt.config(bg="#FEB857")
            self.Weight_bt.config(bg="#FEB857")
            self.Height_bt.config(bg="#FEB857")
            self.Neck_bt.config(bg="#FEB857")
            self.Chest_bt.config(bg="#FEB857")
            self.Abdomen_bt.config(bg="#FEB857")
            self.Hip_bt.config(bg="#FEB857")
            self.Thigh_bt.config(bg="#FEB857")
            self.Knee_bt.config(bg="#FEB857")
            self.Ankle_bt.config(bg="#FEB857")
            self.Biceps_bt.config(bg="#FEB857")
            self.Forearm_bt.config(bg="#FEB857")
            self.Wrist_bt.config(bg="#FEB857")
            self.All_bt.config(bg="#FEB857")
            isAll.append(1)
        else:
            tinhToan.clear()
            isAll.remove(1)
            self.Age_bt.config(bg="#C9DCEA")
            self.Weight_bt.config(bg="#C9DCEA")
            self.Height_bt.config(bg="#C9DCEA")
            self.Neck_bt.config(bg="#C9DCEA")
            self.Chest_bt.config(bg="#C9DCEA")
            self.Abdomen_bt.config(bg="#C9DCEA")
            self.Hip_bt.config(bg="#C9DCEA")
            self.Thigh_bt.config(bg="#C9DCEA")
            self.Knee_bt.config(bg="#C9DCEA")
            self.Ankle_bt.config(bg="#C9DCEA")
            self.Biceps_bt.config(bg="#C9DCEA")
            self.Forearm_bt.config(bg="#C9DCEA")
            self.Wrist_bt.config(bg="#C9DCEA")
            self.All_bt.config(bg="#C9DCEA")
###########################################################################################################
    def Age2_Click(self,event=None):
        if 'Age' not in ve:
            ve.append('Age')
            self.Age2_bt.config(bg="#FEB857")
        else:
            ve.remove('Age')
            self.Age2_bt.config(bg="#C9DCEA")
    def Weight2_Click(self,event=None):
        if 'Weight' not in ve:
            ve.append('Weight')
            self.Weight2_bt.config(bg="#FEB857")
        else:
            ve.remove('Weight')
            self.Weight2_bt.config(bg="#C9DCEA")
    def Height2_Click(self,event=None):
        if 'Height' not in ve:
            ve.append('Height')
            self.Height2_bt.config(bg="#FEB857")
        else:
            ve.remove('Height')
            self.Height2_bt.config(bg="#C9DCEA")
    def Neck2_Click(self,event=None):
        if 'Neck' not in ve:
            ve.append('Neck')
            self.Neck2_bt.config(bg="#FEB857")
        else:
            ve.remove('Neck')
            self.Neck2_bt.config(bg="#C9DCEA")
    def Chest2_Click(self,event=None):
        if 'Chest' not in ve:
            ve.append('Chest')
            self.Chest2_bt.config(bg="#FEB857")
        else:
            ve.remove('Chest')
            self.Chest2_bt.config(bg="#C9DCEA")
    def Abdomen2_Click(self,event=None):
        if 'Abdomen' not in ve:
            ve.append('Abdomen')
            self.Abdomen2_bt.config(bg="#FEB857")
        else:
            ve.remove('Abdomen')
            self.Abdomen2_bt.config(bg="#C9DCEA")
    def Hip2_Click(self,event=None):
        if 'Hip' not in ve:
            ve.append('Hip')
            self.Hip2_bt.config(bg="#FEB857")
        else:
            ve.remove('Hip')
            self.Hip2_bt.config(bg="#C9DCEA")
    def Thigh2_Click(self,event=None):
        if 'Thigh' not in ve:
            ve.append('Thigh')
            self.Thigh2_bt.config(bg="#FEB857")
        else:
            ve.remove('Thigh')
            self.Thigh2_bt.config(bg="#C9DCEA")
    def Knee2_Click(self,event=None):
        if 'Knee' not in ve:
            ve.append('Knee')
            self.Knee2_bt.config(bg="#FEB857")
        else:
            ve.remove('Knee')
            self.Knee2_bt.config(bg="#C9DCEA")
    def Ankle2_Click(self,event=None):
        if 'Ankle' not in ve:
            ve.append('Ankle')
            self.Ankle2_bt.config(bg="#FEB857")
        else:
            ve.remove('Ankle')
            self.Ankle2_bt.config(bg="#C9DCEA")
    def Biceps2_Click(self,event=None):
        if 'Biceps' not in ve:
            ve.append('Biceps')
            self.Biceps2_bt.config(bg="#FEB857")
        else:
            ve.remove('Biceps')
            self.Biceps2_bt.config(bg="#C9DCEA")
    def Forearm2_Click(self,event=None):
        if 'Forearm' not in ve:
            ve.append('Forearm')
            self.Forearm2_bt.config(bg="#FEB857")
        else:
            ve.remove('Forearm')
            self.Forearm2_bt.config(bg="#C9DCEA")
    def Wrist2_Click(self,event=None):
        if 'Wrist' not in ve:
            ve.append('Wrist')
            self.Wrist2_bt.config(bg="#FEB857")
        else:
            ve.remove('Wrist')
            self.Wrist2_bt.config(bg="#C9DCEA")
    def tinhToan_bt_Click(self,event=None):
        if len(tinhToan)<1:
            messagebox.showerror("Lỗi", "Vui lòng chọn  đặc trưng để tính!")
        if tinhToan is not None:
            self.ketQua_bt.config(text="Lỗi bạn chưa chọn đặc trưng")
            m=MR.tinhToan(tinhToan)
            self.ketQua_bt.config(text="%s"%m)
    def ve2d_Click(self,event=None):
        if len(ve)>=2 :
            messagebox.showerror("Lỗi", "Vẽ 2d bạn vui lòng chọn duy nhất 1 đặc trưng vẽ!")
        elif len(ve)==1 and len(tinhToan)>0:
            m=MR.ve2D(tinhToan,ve)
        elif len(ve)<1:
            messagebox.showerror("Lỗi", "Chưa chọn đặc trưng vẽ!")
    def ve3d_Click(self,event=None):
        if len(ve)>=3:
            messagebox.showerror("Lỗi", "Vẽ 3d bạn vui lòng chọn 2 đặc trưng vẽ!")
        elif len(ve)==1:
            messagebox.showerror("Lỗi", "Vẽ 3d bạn vui lòng chọn 2 đặc trưng vẽ!")
        elif len(ve)==2 and len(tinhToan)>1:
            m=MR.ve3D(tinhToan,ve)
        elif len(ve)<1:
            messagebox.showerror("Lỗi", "Chưa chọn đặc trưng vẽ!")
app = Application(master=tk.Tk())
app.master.title('Ứng Dụng MALE(Nhóm 1)')
app.master.minsize(800, 600)
app.mainloop()
