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
import PCA

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
isLogin=[]
tinhToan=[]#bien tam cho tinh toan
isAll=[]#bien tam cho nut all
ve=[]#bien tam cho ve
PCA_n_pc=[1]

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
################ background ##################################
        cv_img = cv2.imread("img/b.png")
        cv_img = cv2.blur(cv_img, (10,10))
        self.canvas = tk.Canvas(self.master, width = 800, height = 600)
        self.canvas.pack()
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
#######################  Login  ##############################################################################
        self.label_loginForm =tk.Label(bg="#A19A99",fg="#f2f2f2",text="Đăng Nhập")
        self.label_username = tk.Label(bg="#A19A99",fg="#f2f2f2", text="Tài khoản")
        self.label_password = tk.Label(bg="#A19A99",fg="#f2f2f2",text="Mật khẩu")
        self.entry_username = Entry(self.master)
        self.entry_password = Entry(self.master, show="*")
        self.logbtn = Button(self.master, text="Đăng Nhập")
        self.label_loginForm.config(font=("Courier bold", 40))
        self.label_username.config(font=("Courier bold", 20))
        self.label_password.config(font=("Courier bold", 20))
        self.entry_username.config(font=("Courier bold", 20))
        self.entry_password.config(font=("Courier bold", 20))
        self.logbtn.config(font=("Courier bold", 20))
        self.label_loginForm.pack()
        self.label_username.pack()
        self.label_password.pack()
        self.entry_username.pack()
        self.entry_password.pack()
        self.logbtn.pack()
        self.label_loginForm.place(x=250,y=10)
        self.label_username.place(x=40,y=250)
        self.label_password.place(x=40,y=300)
        self.entry_username.place(x=180,y=250)
        self.entry_password.place(x=180,y=300)
        self.logbtn.place(x=220,y=350, width=250, height=50)
        #
        self.Back_bt=tk.Button(bg="#ff5c33",fg="#ffebe6")
        self.Back_bt['text']='<--'
        self.Back_bt.pack()
        self.Back_bt.place(x=-2000+0,y=-2000+560,width=60, height=40)
###################### MR  ##############################################################
        self.MR_bt=Button(self.master, text="MultiLinear Regression",width=20, height=2)
        self.MR_bt.config(font=("Courier bold", 20))
        self.MR_bt.pack()
        self.MR_bt.place(x=-2000+220,y=-2000+47)
        self.MR_ketQua_bt = tk.Button(bg="#ffffff")
        self.MR_ketQua_bt.pack()
        self.MR_ketQua_bt.place(x=-2000+250, y=-2000+300, width=300, height=100)
        ###################################
        self.MR_tinhToan_bt = tk.Button(bg="#C9DCEA")
        self.MR_tinhToan_bt['text'] = 'Tính'
        self.MR_tinhToan_bt.pack()
        self.MR_tinhToan_bt.place(x=-2000+252, y=-2000+420, width=90, height=50)
        ###
        self.MR_ve2d_bt = tk.Button(bg="#C9DCEA")
        self.MR_ve2d_bt['text'] = 'Vẽ 2d'
        self.MR_ve2d_bt.pack()
        self.MR_ve2d_bt.place(x=-2000+352, y=-2000+420, width=90, height=50)
        ###
        self.MR_ve3d_bt = tk.Button(bg="#C9DCEA")
        self.MR_ve3d_bt['text'] = 'Vẽ 3d'
        self.MR_ve3d_bt.pack()
        self.MR_ve3d_bt.place(x=-2000+452, y=-2000+420, width=90, height=50)
        self.MR_label = tk.Label(text="MR",bg="#A19A99",fg="#f2f2f2")
        self.MR_label.pack()
        self.MR_label.place(x=-2000+260, y=-2000+5, width=280, height=60)
        self.MR_label.config(font=("Courier bold", 40))
        self.MR_dactrungtinh_label = tk.Label(text="Chọn đặc trưng tính toán",bg="#A19A99",fg="#f2f2f2")
        self.MR_dactrungtinh_label.config(font=("Courier bold", 15))
        self.MR_dactrungtinh_label.pack()
        self.MR_dactrungtinh_label.place(x=-2000+30, y=-2000+10, width=280, height=30)

        ##############################
        self.MR_Age_bt = tk.Button(bg="#C9DCEA")
        self.MR_Age_bt['text'] = 'Age'
        self.MR_Age_bt.pack()
        self.MR_Age_bt.place(x=-2000+30, y=-2000+50, width=70, height=30)
        ###
        self.MR_Weight_bt = tk.Button(bg="#C9DCEA")
        self.MR_Weight_bt['text'] = 'Weight'
        self.MR_Weight_bt.pack()
        self.MR_Weight_bt.place(x=-2000+100, y=-2000+50, width=70, height=30)
        ###
        self.MR_Height_bt = tk.Button(bg="#C9DCEA")
        self.MR_Height_bt['text'] = 'Height'
        self.MR_Height_bt.pack()
        self.MR_Height_bt.place(x=-2000+170, y=-2000+50, width=70, height=30)
        ###
        self.MR_Neck_bt = tk.Button(bg="#C9DCEA")
        self.MR_Neck_bt['text'] = 'Neck'
        self.MR_Neck_bt.pack()
        self.MR_Neck_bt.place(x=-2000+240, y=-2000+50, width=70, height=30)
        ####
        self.MR_Chest_bt = tk.Button(bg="#C9DCEA")
        self.MR_Chest_bt['text'] = 'Chest'
        self.MR_Chest_bt.pack()
        self.MR_Chest_bt.place(x=-2000+30, y=-2000+80, width=70, height=30)
        ####
        self.MR_Abdomen_bt = tk.Button(bg="#C9DCEA")
        self.MR_Abdomen_bt['text'] = 'Abdomen'
        self.MR_Abdomen_bt.pack()
        self.MR_Abdomen_bt.place(x=-2000+100, y=-2000+80, width=70, height=30)
        ####
        self.MR_Hip_bt = tk.Button(bg="#C9DCEA")
        self.MR_Hip_bt['text'] = 'Hip'
        self.MR_Hip_bt.pack()
        self.MR_Hip_bt.place(x=-2000+170, y=-2000+80, width=70, height=30)
        ####
        self.MR_Thigh_bt = tk.Button(bg="#C9DCEA")
        self.MR_Thigh_bt['text'] = 'Thigh'
        self.MR_Thigh_bt.pack()
        self.MR_Thigh_bt.place(x=-2000+240, y=-2000+80, width=70, height=30)
        ####
        self.MR_Knee_bt = tk.Button(bg="#C9DCEA")
        self.MR_Knee_bt['text'] = 'Knee'
        self.MR_Knee_bt.pack()
        self.MR_Knee_bt.place(x=-2000+30, y=-2000+110, width=70, height=30)
        ####
        self.MR_Ankle_bt = tk.Button(bg="#C9DCEA")
        self.MR_Ankle_bt['text'] = 'Ankle'
        self.MR_Ankle_bt.pack()
        self.MR_Ankle_bt.place(x=-2000+100, y=-2000+110, width=70, height=30)
        ####
        self.MR_Biceps_bt = tk.Button(bg="#C9DCEA")
        self.MR_Biceps_bt['text'] = 'Biceps'
        self.MR_Biceps_bt.pack()
        self.MR_Biceps_bt.place(x=-2000+170, y=-2000+110, width=70, height=30)
        ####
        self.MR_Forearm_bt  = tk.Button(bg="#C9DCEA")
        self.MR_Forearm_bt ['text'] = 'Forearm'
        self.MR_Forearm_bt .pack()
        self.MR_Forearm_bt .place(x=-2000+240, y=-2000+110, width=70, height=30)
        ####
        self.MR_Wrist_bt  = tk.Button(bg="#C9DCEA")
        self.MR_Wrist_bt ['text'] = 'Wrist'
        self.MR_Wrist_bt .pack()
        self.MR_Wrist_bt .place(x=-2000+30, y=-2000+140, width=70, height=30)
        ####
        self.MR_All_bt = tk.Button(bg="#C9DCEA")
        self.MR_All_bt['text'] = 'All'
        self.MR_All_bt.pack()
        self.MR_All_bt.place(x=-2000+100, y=-2000+140, width=70, height=30)
        #
        self.MR_dactrungtinh2_label = tk.Label(text="Chọn đặc trưng vẽ",bg="#A19A99",fg="#f2f2f2")
        self.MR_dactrungtinh2_label.pack()
        self.MR_dactrungtinh2_label.config(font=("Courier bold", 15))
        self.MR_dactrungtinh2_label.place(x=-2000+480, y=-2000+10, width=280, height=30)
        self.MR_Age2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Age2_bt['text'] = 'Age'
        self.MR_Age2_bt.pack()
        self.MR_Age2_bt.place(x=-2000+480, y=-2000+50, width=70, height=30)
        ###
        self.MR_Weight2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Weight2_bt['text'] = 'Weight'
        self.MR_Weight2_bt.pack()
        self.MR_Weight2_bt.place(x=-2000+550, y=-2000+50, width=70, height=30)
        ###
        self.MR_Height2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Height2_bt['text'] = 'Height'
        self.MR_Height2_bt.pack()
        self.MR_Height2_bt.place(x=-2000+620, y=-2000+50, width=70, height=30)
        ###
        self.MR_Neck2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Neck2_bt['text'] = 'Neck'
        self.MR_Neck2_bt.pack()
        self.MR_Neck2_bt.place(x=-2000+690, y=-2000+50, width=70, height=30)
        ####
        self.MR_Chest2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Chest2_bt['text'] = 'Chest'
        self.MR_Chest2_bt.pack()
        self.MR_Chest2_bt.place(x=-2000+480, y=-2000+80, width=70, height=30)
        ####
        self.MR_Abdomen2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Abdomen2_bt['text'] = 'Abdomen'
        self.MR_Abdomen2_bt.pack()
        self.MR_Abdomen2_bt.place(x=-2000+550, y=-2000+80, width=70, height=30)
        ####
        self.MR_Hip2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Hip2_bt['text'] = 'Hip'
        self.MR_Hip2_bt.pack()
        self.MR_Hip2_bt.place(x=-2000+620, y=-2000+80, width=70, height=30)
        ####
        self.MR_Thigh2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Thigh2_bt['text'] = 'Thigh'
        self.MR_Thigh2_bt.pack()
        self.MR_Thigh2_bt.place(x=-2000+690, y=-2000+80, width=70, height=30)
        ####
        self.MR_Knee2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Knee2_bt['text'] = 'Knee'
        self.MR_Knee2_bt.pack()
        self.MR_Knee2_bt.place(x=-2000+480, y=-2000+110, width=70, height=30)
        ####
        self.MR_Ankle2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Ankle2_bt['text'] = 'Ankle'
        self.MR_Ankle2_bt.pack()
        self.MR_Ankle2_bt.place(x=-2000+550, y=-2000+110, width=70, height=30)
        ####
        self.MR_Biceps2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Biceps2_bt['text'] = 'Biceps'
        self.MR_Biceps2_bt.pack()
        self.MR_Biceps2_bt.place(x=-2000+620, y=-2000+110, width=70, height=30)
        ####
        self.MR_Forearm2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Forearm2_bt['text'] = 'Forearm'
        self.MR_Forearm2_bt.pack()
        self.MR_Forearm2_bt.place(x=-2000+690, y=-2000+110, width=70, height=30)
        ####
        self.MR_Wrist2_bt = tk.Button(bg="#C9DCEA")
        self.MR_Wrist2_bt['text'] = 'Wrist'
        self.MR_Wrist2_bt.pack()
        self.MR_Wrist2_bt.place(x=-2000+480, y=-2000+140, width=70, height=30)
################ Kernel_PCA  ###########################################################################################
        self.Kernel_PCA_bt=Button(self.master, text="Kernel PCA",width=20, height=2)
        self.Kernel_PCA_bt.config(font=("Courier bold", 20))
        self.Kernel_PCA_bt.pack()
        self.Kernel_PCA_bt.place(x=-2000+220,y=-2000+127)
################ Logistic_regression  ###########################################################################################
        self.Logistic_regression_bt=Button(self.master, text="Logistic Regression",width=20, height=2)
        self.Logistic_regression_bt.config(font=("Courier bold", 20))
        self.Logistic_regression_bt.pack()
        self.Logistic_regression_bt.place(x=-2000+220,y=-2000+207)
################ PCA  ###########################################################################################
        self.PCA_bt=Button(self.master, text="PCA",width=20, height=2)
        self.PCA_bt.config(font=("Courier bold", 20))
        self.PCA_bt.pack()
        self.PCA_bt.place(x=-2000+220,y=-2000+287)
        #
        self.PCA_Dactrung_label=tk.Label(text="Chọn số đặc trưng mới",bg="#A19A99",fg="#f2f2f2")
        self.PCA_Dactrung_label.config(font=("Courier bold", 12))
        self.PCA_Dactrung_label.pack()
        self.PCA_Dactrung_label.place(x=-2000+565, y=-2000+95, width=280, height=30)
        val=[]
        for i in range(1,39):
            val.append(i)
        self.PCA_label=tk.Label(text="PCA",bg="#A19A99",fg="#f2f2f2")
        self.PCA_label.config(font=("Courier bold", 40))
        self.PCA_label.pack()
        self.PCA_label.place(x=-2000+250, y=-2000+10, width=280, height=70)
        self.PCA_Selecting_Pri_Components= ttk.Combobox(self.master, values=val,width=14, height=5)
        self.PCA_Selecting_Pri_Components.set(1)
        self.PCA_Selecting_Pri_Components.pack()
        self.PCA_Selecting_Pri_Components.place(x=-2000+640,y=-2000+125)
        self.PCA_Selecting_Pri_Components.config(font=("Courier bold", 12))
        self.PCA_ve2d_bt=Button(self.master, text="Vẽ 2d",width=13, height=1)
        self.PCA_ve2d_bt.config(font=("Courier bold", 12))
        self.PCA_ve2d_bt.pack()
        self.PCA_ve2d_bt.place(x=-2000+640,y=-2000+360)
        self.PCA_ve3d_bt=Button(self.master, text="Vẽ 3d",width=13, height=1)
        self.PCA_ve3d_bt.config(font=("Courier bold", 12))
        self.PCA_ve3d_bt.pack()
        self.PCA_ve3d_bt.place(x=-2000+640,y=-2000+395)
        self.PCA_Eigen_Values_bt=Button(self.master, text="Eigen Values",width=13, height=1)
        self.PCA_Eigen_Values_bt.config(font=("Courier bold", 12))
        self.PCA_Eigen_Values_bt.pack()
        self.PCA_Eigen_Values_bt.place(x=-2000+640,y=-2000+220)
        self.PCA_Eigen_Vectors_bt=Button(self.master, text="Eigen Vectors",width=13, height=1)
        self.PCA_Eigen_Vectors_bt.config(font=("Courier bold", 12))
        self.PCA_Eigen_Vectors_bt.pack()
        self.PCA_Eigen_Vectors_bt.place(x=-2000+640,y=-2000+255)
        self.PCA_new_Data_bt=Button(self.master, text="New Data",width=13, height=1)
        self.PCA_new_Data_bt.config(font=("Courier bold", 12))
        self.PCA_new_Data_bt.pack()
        self.PCA_new_Data_bt.place(x=-2000+640,y=-2000+290)
        self.PCA_danhGia_bt=Button(self.master, text="Đánh Giá",width=13, height=1)
        self.PCA_danhGia_bt.config(font=("Courier bold", 12))
        self.PCA_danhGia_bt.pack()
        self.PCA_danhGia_bt.place(x=-2000+640,y=-2000+325)
        self.PCA_Mean_bt=Button(self.master, text="Mean",width=13, height=1)
        self.PCA_Mean_bt.config(font=("Courier bold", 12))
        self.PCA_Mean_bt.pack()
        self.PCA_Mean_bt.place(x=-2000+640,y=-2000+150)
        self.PCA_Selecting_Pri_Components_bt=Button(self.master, text="Se_Pri_Components",width=13, height=1)
        self.PCA_Selecting_Pri_Components_bt.config(font=("Courier bold", 12))
        self.PCA_Selecting_Pri_Components_bt. pack()
        self.PCA_Selecting_Pri_Components_bt.place(x=-2000+640,y=-2000+185)
        self.PCA_ketQua_bt=Button(self.master, text="",width=25, height=8,bg="#ffffff")
        self.PCA_ketQua_bt.config(font=("Courier bold", 20))
        self.PCA_ketQua_bt. pack()
        self.PCA_ketQua_bt.place(x=-2000+100,y=-2000+155)

        ###########






        #########
    ############# LDA  ############################################################################################
        self.LDA_bt=Button(self.master, text="LDA",width=20, height=2)
        self.LDA_bt.config(font=("Courier bold", 20))
        self.LDA_bt.pack()
        self.LDA_bt.place(x=-2000+220,y=-2000+367)
################     Poly_regression        ####################################################################################################
        self.Poly_regression_bt=Button(self.master, text="Poly Regression",width=20, height=2)
        self.Poly_regression_bt.config(font=("Courier bold", 20))
        self.Poly_regression_bt.pack()
        self.Poly_regression_bt.place(x=-2000+220,y=-2000+448)

##############      Event        #########################################################################
        ####### Login ###############
        self.logbtn['command']=self.logbtn_Click
        ####### MR #################
        self.MR_tinhToan_bt['command']=self.MR_tinhToan_Click
        self.MR_ve2d_bt['command']=self.MR_ve2d_Click
        self.MR_ve3d_bt['command']=self.MR_ve3d_Click
        self.MR_Age_bt['command']=self.MR_Age_Click
        self.MR_Weight_bt['command']=self.MR_Weight_Click
        self.MR_Height_bt['command']=self.MR_Height_Click
        self.MR_Neck_bt['command']=self.MR_Neck_Click
        self.MR_Chest_bt['command']=self.MR_Chest_Click
        self.MR_Abdomen_bt['command']=self.MR_Abdomen_Click
        self.MR_Hip_bt['command']=self.MR_Hip_Click
        self.MR_Thigh_bt['command']=self.MR_Thigh_Click
        self.MR_Knee_bt['command']=self.MR_Knee_Click
        self.MR_Ankle_bt['command']=self.MR_Ankle_Click
        self.MR_Biceps_bt['command']=self.MR_Biceps_Click
        self.MR_Forearm_bt ['command']=self.MR_Forearm_Click
        self.MR_Wrist_bt ['command']=self.MR_Wrist_Click
        self.Back_bt['command']=self.back_Click
        self.MR_bt['command']=self.MR_Click
        self.MR_All_bt['command']=self.MR_All_Click
        self.MR_Age2_bt['command']=self.MR_Age2_Click
        self.MR_Weight2_bt['command']=self.MR_Weight2_Click
        self.MR_Height2_bt['command']=self.MR_Height2_Click
        self.MR_Neck2_bt['command']=self.MR_Neck2_Click
        self.MR_Chest2_bt['command']=self.MR_Chest2_Click
        self.MR_Abdomen2_bt['command']=self.MR_Abdomen2_Click
        self.MR_Hip2_bt['command']=self.MR_Hip2_Click
        self.MR_Thigh2_bt['command']=self.MR_Thigh2_Click
        self.MR_Knee2_bt['command']=self.MR_Knee2_Click
        self.MR_Ankle2_bt['command']=self.MR_Ankle2_Click
        self.MR_Biceps2_bt['command']=self.MR_Biceps2_Click
        self.MR_Forearm2_bt['command']=self.MR_Forearm2_Click
        self.MR_Wrist2_bt['command']=self.MR_Wrist2_Click
        ##########  PCA  #####################################################
        self.PCA_bt['command']=self.PCA_Click
        self.PCA_Selecting_Pri_Components.bind('<<ComboboxSelected>>', self.on_select)
        self.PCA_Mean_bt['command']=self.PCA_Mean_bt_Click
        self.PCA_Eigen_Values_bt['command']=self.PCA_Eigen_Values_bt_Click
        self.PCA_Selecting_Pri_Components_bt['command']=self.PCA_Selecting_Pri_Components_bt_Click
        self.PCA_Eigen_Vectors_bt['command']=self.PCA_Eigen_Vectors_bt_Click
        self.PCA_new_Data_bt['command']=self.PCA_new_Data_bt_Click
        self.PCA_ve2d_bt['command']=self.PCA_ve2d_bt_Click
        self.PCA_ve3d_bt['command']=self.PCA_ve3d_bt_Click
        self.PCA_danhGia_bt['command']=self.PCA_danhGia_bt_Click

    def logbtn_Click(self,event=None):
        if self.entry_username.get()=='Nhom1' and self.entry_password.get()=='123456':
            isLogin.append(1)
            isAll.clear()
            ve.clear()
            tinhToan.clear()
            ###################################################
            self.label_loginForm.place(x=-2000+250,y=-2000+10)
            self.label_username.place(x=-2000+40,y=-2000+250)
            self.label_password.place(x=-2000+40,y=-2000+300)
            self.entry_username.place(x=-2000+180,y=-2000+250)
            self.entry_password.place(x=-2000+180,y=-2000+300)
            self.logbtn.place(x=-2000+220,y=-2000+350, width=250, height=50)
            self.Back_bt.place(x=0,y=560,width=60, height=40)
            ################################################
            self.MR_bt.place(x=220,y=47)
            self.Kernel_PCA_bt.place(x=220,y=127)
            self.Logistic_regression_bt.place(x=220,y=207)
            self.PCA_bt.place(x=220,y=287)
            self.LDA_bt.place(x=220,y=367)
            self.Poly_regression_bt.place(x=220,y=448)
            ################################################
        else:
            messagebox.showerror('Lỗi','Sai tài khoản hoặc mật khẩu!')
        if 1 not in isLogin:
            self.label_loginForm.place(x=250,y=10)
            self.label_username.place(x=40,y=250)
            self.label_password.place(x=40,y=300)
            self.entry_username.place(x=180,y=250)
            self.entry_password.place(x=180,y=300)
            self.logbtn.place(x=220,y=350, width=250, height=50)
            self.Back_bt.place(x=-2000+0,y=-2000+560,width=60, height=40)
            ###############################################################################
            self.MR_ketQua_bt.place(x=-2000+250, y=-2000+300, width=300, height=100)
            self.MR_tinhToan_bt.place(x=-2000+252, y=-2000+420, width=90, height=50)
            self.MR_ve2d_bt.place(x=-2000+352, y=-2000+420, width=90, height=50)
            self.MR_ve3d_bt.place(x=-2000+452, y=-2000+420, width=90, height=50)
            self.MR_label.place(x=-2000+260, y=-2000+5, width=280, height=60)
            self.MR_dactrungtinh_label.place(x=-2000+30, y=-2000+10, width=280, height=30)
            self.MR_Age_bt.place(x=-2000+30, y=-2000+50, width=70, height=30)
            self.MR_Weight_bt.place(x=-2000+100, y=-2000+50, width=70, height=30)
            self.MR_Height_bt.place(x=-2000+170, y=-2000+50, width=70, height=30)
            self.MR_Neck_bt.place(x=-2000+240, y=-2000+50, width=70, height=30)
            self.MR_Chest_bt.place(x=-2000+30, y=-2000+80, width=70, height=30)
            self.MR_Abdomen_bt.place(x=-2000+100, y=-2000+80, width=70, height=30)
            self.MR_Hip_bt.place(x=-2000+170, y=-2000+80, width=70, height=30)
            self.MR_Thigh_bt.place(x=-2000+240, y=-2000+80, width=70, height=30)
            self.MR_Knee_bt.place(x=-2000+30, y=-2000+110, width=70, height=30)
            self.MR_Ankle_bt.place(x=-2000+100, y=-2000+110, width=70, height=30)
            self.MR_Biceps_bt.place(x=-2000+170, y=-2000+110, width=70, height=30)
            self.MR_Forearm_bt .place(x=-2000+240, y=-2000+110, width=70, height=30)
            self.MR_Wrist_bt .place(x=-2000+30, y=-2000+140, width=70, height=30)
            self.MR_All_bt.place(x=-2000+100, y=-2000+140, width=70, height=30)
            self.MR_dactrungtinh2_label.place(x=-2000+480, y=-2000+10, width=280, height=30)
            self.MR_Age2_bt.place(x=-2000+480, y=-2000+50, width=70, height=30)
            self.MR_Weight2_bt.place(x=-2000+550, y=-2000+50, width=70, height=30)
            self.MR_Height2_bt.place(x=-2000+620, y=-2000+50, width=70, height=30)
            self.MR_Neck2_bt.place(x=-2000+690, y=-2000+50, width=70, height=30)
            self.MR_Chest2_bt.place(x=-2000+480, y=-2000+80, width=70, height=30)
            self.MR_Abdomen2_bt.place(x=-2000+550, y=-2000+80, width=70, height=30)
            self.MR_Hip2_bt.place(x=-2000+620, y=-2000+80, width=70, height=30)
            self.MR_Thigh2_bt.place(x=-2000+690, y=-2000+80, width=70, height=30)
            self.MR_Knee2_bt.place(x=-2000+480, y=-2000+110, width=70, height=30)
            self.MR_Ankle2_bt.place(x=-2000+550, y=-2000+110, width=70, height=30)
            self.MR_Biceps2_bt.place(x=-2000+620, y=-2000+110, width=70, height=30)
            self.MR_Forearm2_bt.place(x=-2000+690, y=-2000+110, width=70, height=30)
            self.MR_Wrist2_bt.place(x=-2000+480, y=-2000+140, width=70, height=30)
            ##########################################################
            self.Back_bt.place(x=-2000+0,y=-2000+560,width=60, height=40)
            self.MR_bt.place(x=-2000+220,y=-2000+47)
            self.Kernel_PCA_bt.place(x=-2000+220,y=-2000+127)
            self.Logistic_regression_bt.place(x=-2000+220,y=-2000+207)
            self.PCA_bt.place(x=-2000+220,y=-2000+287)
            self.LDA_bt.place(x=-2000+220,y=-2000+367)
            self.Poly_regression_bt.place(x=-2000+220,y=-2000+448)
    def back_Click(self,event=None):
        if 2 in isLogin:
            isAll.clear()
            tinhToan.clear()
            ve.clear()
            isLogin.remove(2)
            self.Back_bt.place(x=0,y=560,width=60, height=40)
            self.MR_bt.place(x=220,y=47)
            self.Kernel_PCA_bt.place(x=220,y=127)
            self.Logistic_regression_bt.place(x=220,y=207)
            self.PCA_bt.place(x=220,y=287)
            self.LDA_bt.place(x=220,y=367)
            self.Poly_regression_bt.place(x=220,y=448)
        ########################################################################
            self.MR_ketQua_bt.place(x=-2000+250, y=-2000+300, width=300, height=100)
            self.MR_tinhToan_bt.place(x=-2000+252, y=-2000+420, width=90, height=50)
            self.MR_ve2d_bt.place(x=-2000+352, y=-2000+420, width=90, height=50)
            self.MR_ve3d_bt.place(x=-2000+452, y=-2000+420, width=90, height=50)
            self.MR_label.place(x=-2000+260, y=-2000+5, width=280, height=60)
            self.MR_dactrungtinh_label.place(x=-2000+30, y=-2000+10, width=280, height=30)
            self.MR_Age_bt.place(x=-2000+30, y=-2000+50, width=70, height=30)
            self.MR_Weight_bt.place(x=-2000+100, y=-2000+50, width=70, height=30)
            self.MR_Height_bt.place(x=-2000+170, y=-2000+50, width=70, height=30)
            self.MR_Neck_bt.place(x=-2000+240, y=-2000+50, width=70, height=30)
            self.MR_Chest_bt.place(x=-2000+30, y=-2000+80, width=70, height=30)
            self.MR_Abdomen_bt.place(x=-2000+100, y=-2000+80, width=70, height=30)
            self.MR_Hip_bt.place(x=-2000+170, y=-2000+80, width=70, height=30)
            self.MR_Thigh_bt.place(x=-2000+240, y=-2000+80, width=70, height=30)
            self.MR_Knee_bt.place(x=-2000+30, y=-2000+110, width=70, height=30)
            self.MR_Ankle_bt.place(x=-2000+100, y=-2000+110, width=70, height=30)
            self.MR_Biceps_bt.place(x=-2000+170, y=-2000+110, width=70, height=30)
            self.MR_Forearm_bt .place(x=-2000+240, y=-2000+110, width=70, height=30)
            self.MR_Wrist_bt .place(x=-2000+30, y=-2000+140, width=70, height=30)
            self.MR_All_bt.place(x=-2000+100, y=-2000+140, width=70, height=30)
            self.MR_dactrungtinh2_label.place(x=-2000+480, y=-2000+10, width=280, height=30)
            self.MR_Age2_bt.place(x=-2000+480, y=-2000+50, width=70, height=30)
            self.MR_Weight2_bt.place(x=-2000+550, y=-2000+50, width=70, height=30)
            self.MR_Height2_bt.place(x=-2000+620, y=-2000+50, width=70, height=30)
            self.MR_Neck2_bt.place(x=-2000+690, y=-2000+50, width=70, height=30)
            self.MR_Chest2_bt.place(x=-2000+480, y=-2000+80, width=70, height=30)
            self.MR_Abdomen2_bt.place(x=-2000+550, y=-2000+80, width=70, height=30)
            self.MR_Hip2_bt.place(x=-2000+620, y=-2000+80, width=70, height=30)
            self.MR_Thigh2_bt.place(x=-2000+690, y=-2000+80, width=70, height=30)
            self.MR_Knee2_bt.place(x=-2000+480, y=-2000+110, width=70, height=30)
            self.MR_Ankle2_bt.place(x=-2000+550, y=-2000+110, width=70, height=30)
            self.MR_Biceps2_bt.place(x=-2000+620, y=-2000+110, width=70, height=30)
            self.MR_Forearm2_bt.place(x=-2000+690, y=-2000+110, width=70, height=30)
            self.MR_Wrist2_bt.place(x=-2000+480, y=-2000+140, width=70, height=30)
            ####################### PCA ##################################
            self.PCA_Dactrung_label.place(x=-2000+565, y=-2000+95, width=280, height=30)
            self.PCA_label.place(x=-2000+250, y=-2000+10, width=280, height=70)
            self.PCA_Selecting_Pri_Components.place(x=-2000+640,y=-2000+125)
            self.PCA_ve2d_bt.place(x=-2000+640,y=-2000+360)
            self.PCA_ve3d_bt.place(x=-2000+640,y=-2000+395)
            self.PCA_Eigen_Values_bt.place(x=-2000+640,y=-2000+220)
            self.PCA_Eigen_Vectors_bt.place(x=-2000+640,y=-2000+255)
            self.PCA_new_Data_bt.place(x=-2000+640,y=-2000+290)
            self.PCA_danhGia_bt.place(x=-2000+640,y=-2000+325)
            self.PCA_Mean_bt.place(x=-2000+640,y=-2000+150)
            self.PCA_Selecting_Pri_Components_bt.place(x=-2000+640,y=-2000+185)
            self.PCA_ketQua_bt.place(x=-2000+100,y=-2000+155)
        elif 1 in isLogin:
            isLogin.clear()
            self.label_loginForm.place(x=250,y=10)
            self.label_username.place(x=40,y=250)
            self.label_password.place(x=40,y=300)
            self.entry_username.place(x=180,y=250)
            self.entry_password.place(x=180,y=300)
            self.logbtn.place(x=220,y=350, width=250, height=50)
        ##########################################################
            self.Back_bt.place(x=-2000+0,y=-2000+560,width=60, height=40)
            self.MR_bt.place(x=-2000+220,y=-2000+47)
            self.Kernel_PCA_bt.place(x=-2000+220,y=-2000+127)
            self.Logistic_regression_bt.place(x=-2000+220,y=-2000+207)
            self.PCA_bt.place(x=-2000+220,y=-2000+287)
            self.LDA_bt.place(x=-2000+220,y=-2000+367)
            self.Poly_regression_bt.place(x=-2000+220,y=-2000+448)
        ###############################################################################
            self.MR_ketQua_bt.place(x=-2000+250, y=-2000+300, width=300, height=100)
            self.MR_tinhToan_bt.place(x=-2000+252, y=-2000+420, width=90, height=50)
            self.MR_ve2d_bt.place(x=-2000+352, y=-2000+420, width=90, height=50)
            self.MR_ve3d_bt.place(x=-2000+452, y=-2000+420, width=90, height=50)
            self.MR_label.place(x=-2000+260, y=-2000+5, width=280, height=60)
            self.MR_dactrungtinh_label.place(x=-2000+30, y=-2000+10, width=280, height=30)
            self.MR_Age_bt.place(x=-2000+30, y=-2000+50, width=70, height=30)
            self.MR_Weight_bt.place(x=-2000+100, y=-2000+50, width=70, height=30)
            self.MR_Height_bt.place(x=-2000+170, y=-2000+50, width=70, height=30)
            self.MR_Neck_bt.place(x=-2000+240, y=-2000+50, width=70, height=30)
            self.MR_Chest_bt.place(x=-2000+30, y=-2000+80, width=70, height=30)
            self.MR_Abdomen_bt.place(x=-2000+100, y=-2000+80, width=70, height=30)
            self.MR_Hip_bt.place(x=-2000+170, y=-2000+80, width=70, height=30)
            self.MR_Thigh_bt.place(x=-2000+240, y=-2000+80, width=70, height=30)
            self.MR_Knee_bt.place(x=-2000+30, y=-2000+110, width=70, height=30)
            self.MR_Ankle_bt.place(x=-2000+100, y=-2000+110, width=70, height=30)
            self.MR_Biceps_bt.place(x=-2000+170, y=-2000+110, width=70, height=30)
            self.MR_Forearm_bt .place(x=-2000+240, y=-2000+110, width=70, height=30)
            self.MR_Wrist_bt .place(x=-2000+30, y=-2000+140, width=70, height=30)
            self.MR_All_bt.place(x=-2000+100, y=-2000+140, width=70, height=30)
            self.MR_dactrungtinh2_label.place(x=-2000+480, y=-2000+10, width=280, height=30)
            self.MR_Age2_bt.place(x=-2000+480, y=-2000+50, width=70, height=30)
            self.MR_Weight2_bt.place(x=-2000+550, y=-2000+50, width=70, height=30)
            self.MR_Height2_bt.place(x=-2000+620, y=-2000+50, width=70, height=30)
            self.MR_Neck2_bt.place(x=-2000+690, y=-2000+50, width=70, height=30)
            self.MR_Chest2_bt.place(x=-2000+480, y=-2000+80, width=70, height=30)
            self.MR_Abdomen2_bt.place(x=-2000+550, y=-2000+80, width=70, height=30)
            self.MR_Hip2_bt.place(x=-2000+620, y=-2000+80, width=70, height=30)
            self.MR_Thigh2_bt.place(x=-2000+690, y=-2000+80, width=70, height=30)
            self.MR_Knee2_bt.place(x=-2000+480, y=-2000+110, width=70, height=30)
            self.MR_Ankle2_bt.place(x=-2000+550, y=-2000+110, width=70, height=30)
            self.MR_Biceps2_bt.place(x=-2000+620, y=-2000+110, width=70, height=30)
            self.MR_Forearm2_bt.place(x=-2000+690, y=-2000+110, width=70, height=30)
            self.MR_Wrist2_bt.place(x=-2000+480, y=-2000+140, width=70, height=30)

    def on_select(self,event=None):
        if event: # <-- this works only with bind because `command=` doesn't send event
            PCA_n_pc.clear()
            PCA_n_pc.append(int( event.widget.get()))
    def PCA_danhGia_bt_Click(self,event=None):
        knn=PCA.KNN(n_pc=PCA_n_pc[0],k=1)
        s="Kết quả:\n F(knn_bd)=%.3f"%knn[0]
        s1="\n F(knn_PCA)=%.3f"%knn[1]
        s+=s1
        self.PCA_ketQua_bt.config(text=s)
        self.PCA_ketQua_bt.place(x=100,y=155)

    def PCA_ve2d_bt_Click(self,event=None):
        PCA.Draw_2d(1,"Vẽ 2d cho tập gốc")
        PCA.Draw_2d(2,"Vẽ 2d cho tập iris")
        self.PCA_ketQua_bt.place(x=-2000+100,y=-2000+155)

    def PCA_ve3d_bt_Click(self,event=None):
        PCA.Draw_3d(1,"Vẽ 3d cho tập gốc")
        PCA.Draw_3d(2,"Vẽ 3d cho tập iris")
        self.PCA_ketQua_bt.place(x=-2000+100,y=-2000+155)

    def PCA_new_Data_bt_Click(self,event=None):
        print("\n\n\n\t\t\tNew Data")
        new_Data=PCA.new_Data(n_pc=PCA_n_pc[0],k=1)
        print(new_Data)
        print("\n\n\n")
        self.PCA_ketQua_bt.place(x=-2000+100,y=-2000+155)

    def PCA_Eigen_Vectors_bt_Click(self,event=None):
        print("\n\n\n\t\t\t\tEigen_Vectors")
        print(PCA.Eigen_Vectors(1))
        print("\n\n\n")
        self.PCA_ketQua_bt.place(x=-2000+100,y=-2000+155)

    def PCA_Eigen_Values_bt_Click(self,event=None):
        self.PCA_ketQua_bt.place(x=-2000+100,y=-2000+155)
        Eigen_Values=PCA.Eigen_Values(1)
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        a=[]
        b=[]
        c=[]
        dem=0
        for i in range(len(Eigen_Values)):
            if i<4:
                a.append(Eigen_Values[i])
            elif i>=4 :
                dem+=1
                b.append(Eigen_Values[i])
                if dem==4:
                    c.append((np.array(b)).T)
                    dem=0
                    b.clear()
                if dem==3 and i==len(Eigen_Values)-1:
                    b.append(" ")
                    c.append((np.array(b)).T)
        df = pd.DataFrame(c, columns=a)
        ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        fig.tight_layout()
        plt.show()

    def PCA_Selecting_Pri_Components_bt_Click(self,event=None):
        dt=PCA.Selecting_Pri_Components(1)
        self.PCA_ketQua_bt.place(x=-2000+100,y=-2000+155)


    def PCA_Mean_bt_Click(self,event=None):
        self.PCA_ketQua_bt.place(x=-2000+100,y=-2000+155)
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        dt=PCA.Standardizing(1)
        mean_vec=PCA.Mean(dt)
        a=[]
        b=[]
        c=[]
        dem=0
        for i in range(len(mean_vec)):
            if i<4:
                a.append(mean_vec[i])
            elif i>=4 :
                dem+=1
                b.append(mean_vec[i])
                if dem==4:
                    c.append((np.array(b)).T)
                    dem=0
                    b.clear()
                if dem==3 and i==len(mean_vec)-1:
                    b.append(" ")
                    c.append((np.array(b)).T)
        df = pd.DataFrame(c, columns=a)
        ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        fig.tight_layout()
        plt.show()

    def PCA_Click(self,event=None):
        isLogin.append(2)
        k=2000
        self.MR_bt.place(x=-k+220,y=47)
        self.Kernel_PCA_bt.place(x=-k+220,y=127)
        self.Logistic_regression_bt.place(x=-k+220,y=207)
        self.PCA_bt.place(x=-k+220,y=287)
        self.LDA_bt.place(x=-k+220,y=367)
        self.Poly_regression_bt.place(x=-k+220,y=448)
        #
        self.PCA_Dactrung_label.place(x=565, y=95, width=280, height=30)
        self.PCA_label.place(x=250, y=10, width=280, height=70)
        self.PCA_Selecting_Pri_Components.place(x=640,y=125)
        self.PCA_ve2d_bt.place(x=640,y=360)
        self.PCA_ve3d_bt.place(x=640,y=395)
        self.PCA_Eigen_Values_bt.place(x=640,y=220)
        self.PCA_Eigen_Vectors_bt.place(x=640,y=255)
        self.PCA_new_Data_bt.place(x=640,y=290)
        self.PCA_danhGia_bt.place(x=640,y=325)
        self.PCA_Mean_bt.place(x=640,y=150)
        self.PCA_Selecting_Pri_Components_bt.place(x=640,y=185)
        self.PCA_ketQua_bt.place(x=-2000+100,y=-2000+155)







    def MR_Click(self,event=None):
        isLogin.append(2)
        k=2000
        self.MR_bt.place(x=-k+220,y=47)
        self.Kernel_PCA_bt.place(x=-k+220,y=127)
        self.Logistic_regression_bt.place(x=-k+220,y=207)
        self.PCA_bt.place(x=-k+220,y=287)
        self.LDA_bt.place(x=-k+220,y=367)
        self.Poly_regression_bt.place(x=-k+220,y=448)
        #############################################################
        self.MR_Age_bt.config(bg="#C9DCEA")
        self.MR_Weight_bt.config(bg="#C9DCEA")
        self.MR_Height_bt.config(bg="#C9DCEA")
        self.MR_Neck_bt.config(bg="#C9DCEA")
        self.MR_Chest_bt.config(bg="#C9DCEA")
        self.MR_Abdomen_bt.config(bg="#C9DCEA")
        self.MR_Hip_bt.config(bg="#C9DCEA")
        self.MR_Thigh_bt.config(bg="#C9DCEA")
        self.MR_Knee_bt.config(bg="#C9DCEA")
        self.MR_Ankle_bt.config(bg="#C9DCEA")
        self.MR_Biceps_bt.config(bg="#C9DCEA")
        self.MR_Forearm_bt .config(bg="#C9DCEA")
        self.MR_Wrist_bt .config(bg="#C9DCEA")
        self.MR_Age2_bt.config(bg="#C9DCEA")
        self.MR_Weight2_bt.config(bg="#C9DCEA")
        self.MR_Height2_bt.config(bg="#C9DCEA")
        self.MR_Neck2_bt.config(bg="#C9DCEA")
        self.MR_Chest2_bt.config(bg="#C9DCEA")
        self.MR_Abdomen2_bt.config(bg="#C9DCEA")
        self.MR_Hip2_bt.config(bg="#C9DCEA")
        self.MR_Thigh2_bt.config(bg="#C9DCEA")
        self.MR_Knee2_bt.config(bg="#C9DCEA")
        self.MR_Ankle2_bt.config(bg="#C9DCEA")
        self.MR_Biceps2_bt.config(bg="#C9DCEA")
        self.MR_Forearm2_bt.config(bg="#C9DCEA")
        self.MR_Wrist2_bt.config(bg="#C9DCEA")
        self.MR_All_bt.config(bg="#C9DCEA")
        self.MR_ketQua_bt.config(text="")
        ###################################################################
        ######################################################################################
        self.MR_ketQua_bt.place(x=250, y=300, width=300, height=100)
        self.MR_tinhToan_bt.place(x=252, y=420, width=90, height=50)
        self.MR_ve2d_bt.place(x=352, y=420, width=90, height=50)
        self.MR_ve3d_bt.place(x=452, y=420, width=90, height=50)
        self.MR_label.place(x=260, y=5, width=280, height=60)
        self.MR_dactrungtinh_label.place(x=30, y=10, width=280, height=30)
        self.MR_Age_bt.place(x=30, y=50, width=70, height=30)
        self.MR_Weight_bt.place(x=100, y=50, width=70, height=30)
        self.MR_Height_bt.place(x=170, y=50, width=70, height=30)
        self.MR_Neck_bt.place(x=240, y=50, width=70, height=30)
        self.MR_Chest_bt.place(x=30, y=80, width=70, height=30)
        self.MR_Abdomen_bt.place(x=100, y=80, width=70, height=30)
        self.MR_Hip_bt.place(x=170, y=80, width=70, height=30)
        self.MR_Thigh_bt.place(x=240, y=80, width=70, height=30)
        self.MR_Knee_bt.place(x=30, y=110, width=70, height=30)
        self.MR_Ankle_bt.place(x=100, y=110, width=70, height=30)
        self.MR_Biceps_bt.place(x=170, y=110, width=70, height=30)
        self.MR_Forearm_bt .place(x=240, y=110, width=70, height=30)
        self.MR_Wrist_bt .place(x=30, y=140, width=70, height=30)
        self.MR_All_bt.place(x=100, y=140, width=70, height=30)
        self.MR_dactrungtinh2_label.place(x=480, y=10, width=280, height=30)
        self.MR_Age2_bt.place(x=480, y=50, width=70, height=30)
        self.MR_Weight2_bt.place(x=550, y=50, width=70, height=30)
        self.MR_Height2_bt.place(x=620, y=50, width=70, height=30)
        self.MR_Neck2_bt.place(x=690, y=50, width=70, height=30)
        self.MR_Chest2_bt.place(x=480, y=80, width=70, height=30)
        self.MR_Abdomen2_bt.place(x=550, y=80, width=70, height=30)
        self.MR_Hip2_bt.place(x=620, y=80, width=70, height=30)
        self.MR_Thigh2_bt.place(x=690, y=80, width=70, height=30)
        self.MR_Knee2_bt.place(x=480, y=110, width=70, height=30)
        self.MR_Ankle2_bt.place(x=550, y=110, width=70, height=30)
        self.MR_Biceps2_bt.place(x=620, y=110, width=70, height=30)
        self.MR_Forearm2_bt.place(x=690, y=110, width=70, height=30)
        self.MR_Wrist2_bt.place(x=480, y=140, width=70, height=30)

    def MR_Age_Click(self,event=None):
        if 'Age' not in tinhToan:
            tinhToan.append('Age')
            self.MR_Age_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Age')
            self.MR_Age_bt.config(bg="#C9DCEA")
    def MR_Weight_Click(self,event=None):
        if 'Weight' not in tinhToan:
            tinhToan.append('Weight')
            self.MR_Weight_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Weight')
            self.MR_Weight_bt.config(bg="#C9DCEA")
    def MR_Height_Click(self,event=None):
        if 'Height' not in tinhToan:
            tinhToan.append('Height')
            self.MR_Height_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Height')
            self.MR_Height_bt.config(bg="#C9DCEA")
    def MR_Neck_Click(self,event=None):
        if 'Neck' not in tinhToan:
            tinhToan.append('Neck')
            self.MR_Neck_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Neck')
            self.MR_Neck_bt.config(bg="#C9DCEA")
    def MR_Chest_Click(self,event=None):
        if 'Chest' not in tinhToan:
            tinhToan.append('Chest')
            self.MR_Chest_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Chest')
            self.MR_Chest_bt.config(bg="#C9DCEA")
    def MR_Abdomen_Click(self,event=None):
        if 'Abdomen' not in tinhToan:
            tinhToan.append('Abdomen')
            self.MR_Abdomen_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Abdomen')
            self.MR_Abdomen_bt.config(bg="#C9DCEA")
    def MR_Hip_Click(self,event=None):
        if 'Hip' not in tinhToan:
            tinhToan.append('Hip')
            self.MR_Hip_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Hip')
            self.MR_Hip_bt.config(bg="#C9DCEA")
    def MR_Thigh_Click(self,event=None):
        if 'Thigh' not in tinhToan:
            tinhToan.append('Thigh')
            self.MR_Thigh_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Thigh')
            self.MR_Thigh_bt.config(bg="#C9DCEA")
    def MR_Knee_Click(self,event=None):
        if 'Knee' not in tinhToan:
            tinhToan.append('Knee')
            self.MR_Knee_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Knee')
            self.MR_Knee_bt.config(bg="#C9DCEA")
    def MR_Ankle_Click(self,event=None):
        if 'Ankle' not in tinhToan:
            tinhToan.append('Ankle')
            self.MR_Ankle_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Ankle')
            self.MR_Ankle_bt.config(bg="#C9DCEA")
    def MR_Biceps_Click(self,event=None):
        if 'Biceps' not in tinhToan:
            tinhToan.append('Biceps')
            self.MR_Biceps_bt.config(bg="#FEB857")
        else:
            tinhToan.remove('Biceps')
            self.MR_Biceps_bt.config(bg="#C9DCEA")
    def MR_Forearm_Click(self,event=None):
        if 'Forearm' not in tinhToan:
            tinhToan.append('Forearm')
            self.MR_Forearm_bt .config(bg="#FEB857")
        else:
            tinhToan.remove('Forearm')
            self.MR_Forearm_bt .config(bg="#C9DCEA")
    def MR_Wrist_Click(self,event=None):
        if 'Wrist' not in tinhToan:
            tinhToan.append('Wrist')
            self.MR_Wrist_bt .config(bg="#FEB857")
        else:
            tinhToan.remove('Wrist')
            self.MR_Wrist_bt .config(bg="#C9DCEA")
    def MR_All_Click(self,event=None):
        if 1 not in isAll:
            t=['Age','Weight','Height','Neck','Chest','Abdomen','Hip','Thigh','Knee','Ankle','Biceps','Forearm','Wrist']
            for i in t:
                if i not in tinhToan:
                    tinhToan.append(i)
            self.MR_Age_bt.config(bg="#FEB857")
            self.MR_Weight_bt.config(bg="#FEB857")
            self.MR_Height_bt.config(bg="#FEB857")
            self.MR_Neck_bt.config(bg="#FEB857")
            self.MR_Chest_bt.config(bg="#FEB857")
            self.MR_Abdomen_bt.config(bg="#FEB857")
            self.MR_Hip_bt.config(bg="#FEB857")
            self.MR_Thigh_bt.config(bg="#FEB857")
            self.MR_Knee_bt.config(bg="#FEB857")
            self.MR_Ankle_bt.config(bg="#FEB857")
            self.MR_Biceps_bt.config(bg="#FEB857")
            self.MR_Forearm_bt .config(bg="#FEB857")
            self.MR_Wrist_bt .config(bg="#FEB857")
            self.MR_All_bt.config(bg="#FEB857")
            isAll.append(1)
        else:
            tinhToan.clear()
            isAll.remove(1)
            self.MR_Age_bt.config(bg="#C9DCEA")
            self.MR_Weight_bt.config(bg="#C9DCEA")
            self.MR_Height_bt.config(bg="#C9DCEA")
            self.MR_Neck_bt.config(bg="#C9DCEA")
            self.MR_Chest_bt.config(bg="#C9DCEA")
            self.MR_Abdomen_bt.config(bg="#C9DCEA")
            self.MR_Hip_bt.config(bg="#C9DCEA")
            self.MR_Thigh_bt.config(bg="#C9DCEA")
            self.MR_Knee_bt.config(bg="#C9DCEA")
            self.MR_Ankle_bt.config(bg="#C9DCEA")
            self.MR_Biceps_bt.config(bg="#C9DCEA")
            self.MR_Forearm_bt .config(bg="#C9DCEA")
            self.MR_Wrist_bt .config(bg="#C9DCEA")
            self.MR_All_bt.config(bg="#C9DCEA")
###########################################################################################################
    def MR_Age2_Click(self,event=None):
        if 'Age' not in ve:
            ve.append('Age')
            self.MR_Age2_bt.config(bg="#FEB857")
        else:
            ve.remove('Age')
            self.MR_Age2_bt.config(bg="#C9DCEA")
    def MR_Weight2_Click(self,event=None):
        if 'Weight' not in ve:
            ve.append('Weight')
            self.MR_Weight2_bt.config(bg="#FEB857")
        else:
            ve.remove('Weight')
            self.MR_Weight2_bt.config(bg="#C9DCEA")
    def MR_Height2_Click(self,event=None):
        if 'Height' not in ve:
            ve.append('Height')
            self.MR_Height2_bt.config(bg="#FEB857")
        else:
            ve.remove('Height')
            self.MR_Height2_bt.config(bg="#C9DCEA")
    def MR_Neck2_Click(self,event=None):
        if 'Neck' not in ve:
            ve.append('Neck')
            self.MR_Neck2_bt.config(bg="#FEB857")
        else:
            ve.remove('Neck')
            self.MR_Neck2_bt.config(bg="#C9DCEA")
    def MR_Chest2_Click(self,event=None):
        if 'Chest' not in ve:
            ve.append('Chest')
            self.MR_Chest2_bt.config(bg="#FEB857")
        else:
            ve.remove('Chest')
            self.MR_Chest2_bt.config(bg="#C9DCEA")
    def MR_Abdomen2_Click(self,event=None):
        if 'Abdomen' not in ve:
            ve.append('Abdomen')
            self.MR_Abdomen2_bt.config(bg="#FEB857")
        else:
            ve.remove('Abdomen')
            self.MR_Abdomen2_bt.config(bg="#C9DCEA")
    def MR_Hip2_Click(self,event=None):
        if 'Hip' not in ve:
            ve.append('Hip')
            self.MR_Hip2_bt.config(bg="#FEB857")
        else:
            ve.remove('Hip')
            self.MR_Hip2_bt.config(bg="#C9DCEA")
    def MR_Thigh2_Click(self,event=None):
        if 'Thigh' not in ve:
            ve.append('Thigh')
            self.MR_Thigh2_bt.config(bg="#FEB857")
        else:
            ve.remove('Thigh')
            self.MR_Thigh2_bt.config(bg="#C9DCEA")
    def MR_Knee2_Click(self,event=None):
        if 'Knee' not in ve:
            ve.append('Knee')
            self.MR_Knee2_bt.config(bg="#FEB857")
        else:
            ve.remove('Knee')
            self.MR_Knee2_bt.config(bg="#C9DCEA")
    def MR_Ankle2_Click(self,event=None):
        if 'Ankle' not in ve:
            ve.append('Ankle')
            self.MR_Ankle2_bt.config(bg="#FEB857")
        else:
            ve.remove('Ankle')
            self.MR_Ankle2_bt.config(bg="#C9DCEA")
    def MR_Biceps2_Click(self,event=None):
        if 'Biceps' not in ve:
            ve.append('Biceps')
            self.MR_Biceps2_bt.config(bg="#FEB857")
        else:
            ve.remove('Biceps')
            self.MR_Biceps2_bt.config(bg="#C9DCEA")
    def MR_Forearm2_Click(self,event=None):
        if 'Forearm' not in ve:
            ve.append('Forearm')
            self.MR_Forearm2_bt.config(bg="#FEB857")
        else:
            ve.remove('Forearm')
            self.MR_Forearm2_bt.config(bg="#C9DCEA")
    def MR_Wrist2_Click(self,event=None):
        if 'Wrist' not in ve:
            ve.append('Wrist')
            self.MR_Wrist2_bt.config(bg="#FEB857")
        else:
            ve.remove('Wrist')
            self.MR_Wrist2_bt.config(bg="#C9DCEA")
    def MR_tinhToan_Click(self,event=None):
        if len(tinhToan)<1:
            messagebox.showerror("Lỗi", "Vui lòng chọn  đặc trưng để tính!")
        if tinhToan is not None:
            self.MR_ketQua_bt.config(text="Lỗi bạn chưa chọn đặc trưng")
            m=MR.tinhToan(tinhToan)
            self.MR_ketQua_bt.config(text="%s"%m)
    def MR_ve2d_Click(self,event=None):
        if len(ve)>=2 :
            messagebox.showerror("Lỗi", "Vẽ 2d bạn vui lòng chọn duy nhất 1 đặc trưng vẽ!")
        elif len(ve)==1 and len(tinhToan)>0:
            m=MR.ve2D(tinhToan,ve)
        elif len(ve)<1:
            messagebox.showerror("Lỗi", "Chưa chọn đặc trưng vẽ!")
    def MR_ve3d_Click(self,event=None):
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
app.master.maxsize(800, 600)
app.mainloop()
