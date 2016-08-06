import sqlite3
import tkinter as tk
from tkinter import N, S, E, W
from tkinter import TOP, BOTTOM, LEFT, RIGHT, END, ALL


#Python 3.5
#Create Database
def main():
    db = 'bballstats.db'
    tbl = 'Players'
    columns = 'PlayerName text', 'Points integer', 'Rebounds integer', 'Assists integer', 'Other text'
    createTable(db, tbl, *columns)

    root = tk.Tk()
    demo_window = EntryWindow(root, *[db, tbl])
    root.mainloop()
    

def createTable(database, table, *col_defs):
    
    NBA = (('create table {}('+('{},'*len(col_defs))[:-1]+');')
             .format(table, *col_defs))
    with sqlite3.connect(database) as conn:
        c = conn.cursor()
        c.execute('drop table if exists {};'.format(table))
        c.execute(NBA)
        conn.commit()


class EntryWindow(tk.Frame):

    def __init__(self, master=None, *args):
        tk.Frame.__init__(self, master)
        self.master = master
        self.database = args[0]
        self.table = args[1]
        self.initWindow()
        #self.Listbox()
        
                
    def initWindow(self):
        self.master.title('NBA Data Entry'.format(self.table.upper()))
        self.grid(column=0, row=0, sticky=(N, W, E, S), padx=50, pady=75)
        self.grid_columnconfigure(15, weight=15)
        self.grid_rowconfigure(15, weight=15)      

        def getColNames(self):
            with sqlite3.connect(self.database) as conn:
                c = conn.cursor()
                c.execute("PRAGMA table_info('{}')".format(self.table))
                self.ColNames = [x[1] for x in c.fetchall()]
            return self.ColNames

        self.column_names = getColNames(self)

        self.item_entry = []
        for item in self.column_names:
            num = len(self.item_entry)
            tk.Label(self, text=item).grid(row=num, column=0, pady=1, sticky=E)
            self.item_entry.append(tk.Entry(self))
            self.item_entry[num].grid(row=num, column=1, pady=1, padx=5)

        def addItem(self):
            entries = [e.get() for e in self.item_entry]
            NBA = ('insert into {0}({1}) values ({2})'.format(self.table, ','.join(self.column_names),':'+',:'.join(self.column_names)))
            with sqlite3.connect(self.database) as conn:
                c = conn.cursor()
                c.execute(NBA, entries)
                conn.commit()
            clear_fields(self)
            print(entries)

        def clear_fields(self):
            for e in self.item_entry:
                e.delete(0, END)
            self.item_entry[0].focus()

        
     
        # Create Buttons
        submit_button = tk.Button(self, text='Add Item', width=8, command=lambda: addItem(self))
        submit_button.grid(row=10, column=0, sticky=E, pady=0, padx=1)
     
       # poll_button = tk.Button(self, text='Grid', width=8, command=lambda: poll(self))
       # poll_button.grid(row=10, column=1, sticky=W, pady=0, padx=1)

        

if __name__ == '__main__':
    main()
