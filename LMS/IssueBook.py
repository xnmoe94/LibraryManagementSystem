from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from LMS.pySql import *


issueTable = "books_issued"
bookTable = "books"

allBod = []

def issue():

    pass





def issueBook():

    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    root = Tk()
    root.title('Library')
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text='Issue Book', bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.13, rely=0.3, relwidth=0.8, relheight=0.5)

    #Book ID

    lb1 = Label(labelFrame, text='Book ID: ', bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    #Issued To student name

    lb2 = Label(labelFrame, text='issued To: ', bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely= 0.4, relwidth=0.62)

    #IssueButton

    issueBtn = Button(root, text='Issue', bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


