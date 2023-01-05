from tkinter import *
root = Tk()
root.geometry('500x300')

Label(root, text='Registration', font='arial 15 bold').grid(row=0, column=3)

name = Label(root, text='name').grid(row=0, column=3)
phone = Label(root, text='phone').grid(row=0, column=3)
gender = Label(root, text='gender').grid(row=0, column=3)
emergency = Label(root, text='emergency').grid(row=0, column=3)
paymentmood = Label(root, text='paymentmood').grid(row=0, column=3)





root.mainloop()