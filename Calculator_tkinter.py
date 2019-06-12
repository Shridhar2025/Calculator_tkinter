# import tkinter as tk
# from tkinter import  messagebox
# mainWindow = tk.Tk()
# mainWindow.title("Calculator")
#
# heading_label = tk.Label(mainWindow,text = "First Number")
# heading_label.pack()
#
# name_field = tk.Entry(mainWindow)
# name_field.pack()
#
# Subtitle_label = tk.Label(mainWindow,text = "Second Number")
# Subtitle_label.pack()
#
# name_field1 = tk.Entry(mainWindow)
# name_field1.pack()
#
# def Input():
#     num1 =name_field.get()
#     num2 =name_field1.get()
#     try:
#         num1=int(num1)
#         num2=int(num2)
#         return num1,num2
#     except ValueError:
#         if((len(name_field.get())==0)|(len(name_field1.get())==0)):
#             messagebox.showerror("Error","Please Enter A Value")
#         else:
#             messagebox.showerror("Error","Enter only Integer Value")
#         quit(0)
#
#
# def add():
#     num1,num2=Input()
#     res1 = num1+num2
#     # print(res1)
#     Result_label.config(text="Result is:"+str(res1))
# def minus():
#     num1, num2 = Input()
#     if(num1>num2):
#      res2 = num1-num2
#      # print(res2)
#      Result_label.config(text="Result is:" + str(res2))
#     else:
#      res2 = num2-num1
#      # print(res2)
#      Result_label.config(text="Result is:" + str(res2))
# def multi():
#     num1, num2 = Input()
#     res3 = num1*num2
#     # print(res3)
#     Result_label.config(text="Result is:" + str(res3))
# def div():
#     num1, num2 = Input()
#     if((num1==0)|(num2==0)):
#         # print("Not Valid")
#         messagebox.showerror("Error","Cannot Divide The Value By Zero")
#     else:
#         res4 = num1/num2
#         # print(res4)
#         res4 = round(res4,2)
#         Result_label.config(text="Result is:"+str(res4))
#
#
# button = tk.Button(mainWindow,text="+",command=lambda :add())
# button.pack()
# button1 = tk.Button(mainWindow,text="-",command=lambda :minus())
# button1.pack()
# button2 = tk.Button(mainWindow,text="*",command=lambda :multi())
# button2.pack()
# button3 = tk.Button(mainWindow,text="/",command=lambda :div())
# button3.pack()
#
# Result_label = tk.Label(mainWindow,text="Result is:")
# Result_label.pack()
#
# mainWindow.mainloop()
