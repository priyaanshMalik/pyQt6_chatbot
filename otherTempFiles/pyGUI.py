import tkinter as tk

window = tk.Tk()

window.columnconfigure(0, weight=1, minsize=800)
window.rowconfigure([0, 2], weight=1, minsize=40)
window.rowconfigure(1, weight=7, minsize=450)


frm_head = tk.Frame(master=window, relief='sunken', borderwidth=3)
frm_head.columnconfigure(0, weight=1, minsize=200)
frm_head.rowconfigure(0, weight=1, minsize=20)
lbl_head = tk.Label(
                    master=frm_head,
    text="Hello, Tkinter",
        foreground='#000123',
            background='#FFF123',
)
lbl_head.grid(row=0, column=0, padx=0, pady=0, sticky=tk.NSEW)
frm_head.grid(row=0, column=0, padx=0, pady=0, sticky=tk.NSEW)

# MAIN FRAME BEGINS
frm_main = tk.Frame(master=window, relief='sunken', borderwidth=5)

# main_label of main
# common column for frame main_label
frm_main.columnconfigure(0, weight=1, minsize=240)
frm_main.rowconfigure(0, weight=1, minsize=20)
lbl_main = tk.Label(
    master=frm_main,
    text="This is the chatbot write your related queries",
    foreground='#FFFFFF',
    background='#123123',
)
lbl_main.grid(row=0, column=0, padx=0, pady=0, sticky=tk.NSEW)

# mainChat of main
frm_main.rowconfigure(1, weight=1, minsize=400)
frm_mainChat = tk.Frame(master=frm_main, borderwidth=0)
frm_mainChat.columnconfigure(list(range(1, 4)), weight=4, minsize=100)
frm_mainChat.columnconfigure(0, weight=1, minsize=1)
frm_mainChat.columnconfigure(4, weight=1, minsize=1)
frm_mainChat.rowconfigure(list(range(10)), weight=1, minsize=4)
# chatBubble = tk.Frame(master=frm_mainChat, relief='raised',
#          borderwidth=3, background='pink')
# chatBubble.grid(row=0, column=1, padx=0, pady=0,
#                                          sticky=tk.NSEW, columnspan=3)
chatBubble = []
change = False
for i in range(2):
    chatBubble += [tk.Label(master=frm_mainChat,
                            borderwidth=0,
                            background='pink',
                            height=2)]
    chatBubble[i].grid(row=i, column=1, columnspan=3,
                       sticky=tk.NSEW, padx=0, pady=3)
    change = not change
    shp = tk.Canvas(master=frm_mainChat, background='blue', height=0, width=0)
    shp.grid(row=i, column=(0 if change else 4), sticky=tk.NSEW)
    shp.create_polygon([1, 1, 33, 33, 55, 55], fill='red')


# inside mainChat, chatBubble
frm_mainChat.grid(row=1, column=0, padx=0, pady=0, sticky=tk.NSEW)

# input of main
frm_main.rowconfigure(2, weight=1, minsize=40)
frm_input = tk.Frame(master=frm_main, relief='raised', borderwidth=3)
frm_input.columnconfigure(list(range(5)), weight=1, minsize=40)
frm_input.rowconfigure(0, weight=5, minsize=20)
# textbox of input of main
txt_input = tk.Text(master=frm_input, relief='raised',
                    borderwidth=2, height=3)
txt_input.grid(row=0, column=0, padx=0, pady=0, sticky=tk.NSEW, columnspan=4)
# button of input of main
btn_input = tk.Button(master=frm_input, text='Okay')
btn_input.grid(row=0, column=4, padx=0, pady=0, sticky=tk.NSEW, columnspan=1)

# placing subgrid of main_frame
frm_input.grid(row=2, column=0, padx=0, pady=0, sticky=tk.NSEW)

# placing main_grid
frm_main.grid(row=1, column=0, padx=2, pady=5, sticky=tk.NSEW)


frm_foot = tk.Frame(master=window, relief='raised', borderwidth=3)
frm_foot.columnconfigure(0, weight=1, minsize=200)
frm_foot.rowconfigure(0, weight=1, minsize=20)
lbl_foot = tk.Label(
    master=frm_foot,
    text="This is the footer",
    foreground='#FFFFFF',
    background='#123123',
    # width=70,
    # height=1
)
lbl_foot.grid(row=0, column=0, padx=0, pady=0, sticky=tk.NSEW)
frm_foot.grid(row=2, column=0, padx=0, pady=0, sticky=tk.NSEW)

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)

#     for j in range(0, 3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)

window.mainloop()
