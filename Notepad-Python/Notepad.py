#import tkinter, scrolledtext, filedialog and messagebox's functions.
from tkinter import *
from tkinter.scrolledtext import *
from tkinter import filedialog
from tkinter import messagebox

#function to open a file
def openFile():
    f=filedialog.askopenfile(mode="r",filetypes=[("Text File","*.txt"),
                                                 ("Python File","*.py"),
                                                 ("All Files","*.*")])

    if f:
        t.delete(1.0,END)
        c=f.read()
        w.title(f.name)
        t.insert(INSERT,c)
        f.close()

#function to save file    
def saveFile():
    f=filedialog.asksaveasfile(mode="w+",
                               defaultextension="*.*",
                               filetype=[("Text File","*.txt"),
                                          ("Python File","*.py"),
                                          ("All Files","*.*")],
                               title="Save File")
                              
    if f:
        w.title(f.name)
        s=str(t.get(1.0,END))
        f.write(s)
        f.close()

#function to give information about Notepad
def aboutN():
       messagebox.showinfo("About Notepad","Simple text editor like notepad using Python")

#function to open a new file
def newFile():
    w.title("Untitled Notepad")
    file = None
    t.delete(1.0,END)

#function to cut
def cut():
      t.event_generate("<<Cut>>")

#function to copy      
def copy():
      t.event_generate("<<Copy>>")

#function to paste
def paste():
      t.event_generate("<<Paste>>")

#function to find 
def fileInFile():
    #function to find word in file
    def wordFind():
        search=txt.get()
        s=t.get(1.0,END)
        str(s)
        x=s.count(search)
        if search in s:
            label=messagebox.showinfo("Results", search +" "+ "has" +" "+ str(x)+" "+ "occurances")
            fs.destroy()
        
        else:
            label=messagebox.showinfo("Results","Zero results")
    fs=Toplevel() #Used to create and display the toplevel windows which are directly managed by the window manager. 
    fs.title("Find") #Title of Find window  
    fs.geometry("300x100+150+150") #Size of a window
    fs.wm_iconbitmap('icon.ico')   #Icon used in window
    f1=Frame(fs)
    f1.grid(row="0",column="0")
    l=Label(f1,text="Find What:")
    l.grid(row="0",column="0")
    txt=Entry(fs)
    txt.grid(row="0",column="1")
    txt.focus()
    ft=Button(fs,text="Find", command=wordFind)
    ft.grid(row="3",column="1")


#Notepad Window
w=Tk()
w.title("Untitled-Notepad") #Title of Notepad
w.geometry("800x800+0+0")   #Size of a window
w.wm_iconbitmap('icon.ico') #Icon used in window
m=Menu(w)                   #Menu bar
w.config(menu=m)
filemenu=Menu(m,tearoff=0)  #File Menu
m.add_cascade(label="File",menu=filemenu)
filemenu.add_cascade(label="New",command=newFile)
filemenu.add_cascade(label="Open",command=openFile)
filemenu.add_cascade(label="Save",command=saveFile)
filemenu.add_separator()
filemenu.add_cascade(label="Exit",command=w.destroy)
editmenu=Menu(m,tearoff=0)  #Edit Menu
m.add_cascade(label="Edit",menu=editmenu)
editmenu.add_cascade(label="Copy",command=copy)
editmenu.add_cascade(label="Cut", command=cut)
editmenu.add_cascade(label="Paste",command=paste)
editmenu.add_separator()    #To seperate two functions
editmenu.add_cascade(label="Find",command=fileInFile)
helpmenu=Menu(m,tearoff=0)  #Help Menu
m.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_cascade(label="About Notepad",command=aboutN)
t=ScrolledText(w,width=800,height=800,font=("Consolas",11)) #Text area
t.pack()
t.focus()


w.mainloop() #To run window infinity times
