from sql import *
from tkinter import *
from tkinter import messagebox, ttk


def execute():
    sql = query.get()
    result = db.query(sql)
    if isinstance(result, str):
        messagebox.showinfo("Execution Result", result)
    else:
        pass

def main():
    global db, query, data

    db = Database()
    base = Tk()
    base.geometry("300x300")
    base.title("My SQLite Query test")
    
    Label(base, text="My SQLite Query Tester", font=("Times New Roman", 25)).pack()

    query_frame = Frame(base)
    query = Entry(query_frame)
    query.pack(side='left', fill='x', expand=True)

    query_button = Button(query_frame, text="Execute", command=lambda: execute())
    query_button.pack(side='left')
    query_frame.pack()

    data = ttk.Treeview(base)

    base.mainloop()

if __name__ == "__main__":
    main()
