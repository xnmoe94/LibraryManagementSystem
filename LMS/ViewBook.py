from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql



def View():

    root = Tk()
    root.title('View Books')
    root.minsize(width=900, height=400)
    root.geometry("600x500")

    mypass = "Muhaz8164"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"  # Book Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e42")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))

    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-40s%-30s%-20s%-90s" % ('Book ID', ' Title', '  Author', '  Status', '                  client'),
          bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from " + bookTable
    try:
        cur.execute(getBooks)
        con.commit()

        for i in cur:
            Label(labelFrame, text="%-10s%-30s%-30s%-40s%-40s" % (i[0], i[1], i[2], i[3], i[4]), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1

            print(i)
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()