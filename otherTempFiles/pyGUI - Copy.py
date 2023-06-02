import tkinter as tk
from tkinter import ttk

# window level
root = tk.Tk()
root.title("Bhagvad Gita Chat")
root.columnconfigure(0, weight=1, minsize=800)
root.rowconfigure([0, 2, 3], weight=1, minsize=50)
root.rowconfigure(1, weight=7, minsize=450)


frm_header = tk.Frame(master=root, borderwidth=5, relief='raised')
frm_header.grid(row=0, column=0, padx=0, pady=0, sticky=tk.NSEW)

frm_main = tk.Frame(master=root)
frm_main.grid(row=1, column=0, padx=0, pady=0, sticky=tk.NSEW)

frm_in = tk.Frame(master=root, borderwidth=5, relief='ridge')
frm_in.grid(row=2, column=0, padx=0, pady=0, sticky=tk.NSEW)

frm_foot = tk.Frame(master=root, borderwidth=5,
                    relief='ridge')
frm_foot.grid(row=3, column=0, padx=0, pady=0, sticky=tk.NSEW)


# configuring frm_header grid structure 0x0 structure
frm_header.columnconfigure(0, weight=1, minsize=200)
frm_header.rowconfigure(0, weight=1, minsize=20)
# placing label in header
lbl_head = ttk.Label(
    master=frm_header,
    text="Talk with the Holy Bhagwad Gita",
    # foreground='#000123',
    # background='#FFF123',
    anchor=tk.CENTER,
    font=("Lucida Calligraphy", 14)
)
lbl_head.grid(row=0, column=0, padx=0, pady=0, sticky=tk.NSEW)
# configuring frm_footer grid structure 0x0 structure
frm_foot.columnconfigure(0, weight=1, minsize=200)
frm_foot.rowconfigure(0, weight=1, minsize=20)
# placing label in footer
lbl_foot = ttk.Label(
    master=frm_foot,
    text="This is the footer",
    foreground='#FFFFFF',
    background='#808080',
    anchor=tk.CENTER,
    font=("Lucida Calligraphy", 11)
)
lbl_foot.grid(row=0, column=0, padx=0, pady=0, sticky=tk.NSEW)
frm_in.columnconfigure(list(range(0, 10)), weight=1, minsize=5)
frm_in.columnconfigure(10, weight=1, minsize=5)
frm1 = tk.Frame(frm_in)
frm1.grid(row=0, column=0, columnspan=10, sticky=tk.NSEW)
frm2 = tk.Frame(frm_in)
frm2.grid(row=0, column=10)
ent_in = tk.Entry(frm1)
ent_in.pack(fill=tk.BOTH, pady=10, padx=10)
btn_in = tk.Button(text='abcdef', master=frm2, width=15,
                   cursor='hand2', font=('Lucida Bright', 14))
btn_in.pack(fill=tk.BOTH, pady=1, padx=0)

canvasMain = tk.Canvas(master=frm_main, background='orange')
canvasMain.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbarMain = ttk.Scrollbar(
    frm_main, orient=tk.VERTICAL, command=canvasMain.yview)
scrollbarMain.pack(side=tk.RIGHT, fill=tk.Y)
canvasMain.configure(yscrollcommand=scrollbarMain.set)
canvasMain.bind("<Configure>", lambda e: canvasMain.configure(
    scrollregion=canvasMain.bbox("all")))
contentMain = tk.Frame(canvasMain)
canvasMain.create_window((24, 25), window=contentMain, anchor=tk.NW)

# Add some widgets to the contentMain frame
for i in range(20):
    label = tk.Label(
        contentMain, text=f"Label {i+1}", width=103)
    label.pack(fill=tk.BOTH, expand=True, pady=10)

# Configure the canvasMain scrolling region
canvasMain.update_idletasks()
canvasMain.configure(scrollregion=canvasMain.bbox("all"))


root.resizable(False, False)
root.mainloop()
