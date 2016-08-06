from tkinter import *
import webbrowser
import sqlite3

#Create database
db = sqlite3.connect('sale.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS content(id INTEGER PRIMARY KEY, name TEXT)''')
db.commit()

htmlGui = Tk()
_list = Listbox(htmlGui)
source = StringVar()
source.set("Stay tuned for our amazing summer sale!")

#_list.pack()    
                            
def saveRecord():
    name = source.get()
    con = sqlite3.connect('sale.db')

    with con:
        cur = con.cursor()
        cur.execute('''INSERT INTO content(name) VALUES(?)''', (name,))
        con.commit()
    #print("Data saved")
    
def fetchRecord():
    _list.delete(0, END)
    con = sqlite3.connect('sale.db')
    with con:
        cur = con.cursor()
        list_loadr = cur.execute('''SELECT name FROM content''')
        list_load = list_loadr.fetchall()
        for item in list_load:
            _list.insert(END, item)
    
       
        
#Load is supposed to select content choice and insert into text field
def loadRecord(self):
    index = _list.curselection()[0]
    seltext = _list.get(index) #+ '\n'
    source.set(seltext)
     
 
    
   
        
        
#Open web browser window and display selection
def browser():
    f = open('summersale.html','w')
    text = source.get()
    message = "<html><head></head><body><p>%s</p></body></html>" % text
    f.write(message)
    f.close()
    webbrowser.open_new_tab('summersale.html')

htmlGui.geometry('450x450+500+500')
htmlGui.title('HTML Body Builder')
htmllabel = Label(htmlGui,text='Enter Text Below').pack()
htmlEntry = Entry(htmlGui,textvariable=source).pack()
htmlbutton = Button(htmlGui,text="Open Browser",command = browser).pack()    
        

frame2 = Frame(htmlGui)
frame2.pack()

wbbutton3 = Button(frame2,text="Save",command = saveRecord)
wbbutton4 = Button(frame2,text="Fetch",command = fetchRecord)

wbbutton3.pack(side=LEFT)
wbbutton4.pack(side=LEFT)

_list.bind("<ButtonRelease-1>", loadRecord)



_list.pack()

htmlGui.mainloop()
