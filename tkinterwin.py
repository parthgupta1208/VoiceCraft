import tkinter as tk

def display_grid():
    global rootgrid
    rootgrid = tk.Tk()
    rootgrid.overrideredirect(True)
    rootgrid.attributes('-topmost',1)
    rootgrid.geometry("{0}x{1}+0+0".format(rootgrid.winfo_screenwidth(), rootgrid.winfo_screenheight()))
    rootgrid.resizable(False, False)
    rootgrid.attributes("-alpha", 0.3)

    width = rootgrid.winfo_screenwidth() // 10
    height = rootgrid.winfo_screenheight() // 7

    for i in range(10):
        for j in range(7):
            num = j * 10 + i + 1  # calculate the block number
            block = tk.Frame(rootgrid, width=width, height=height, bg="white")
            label = tk.Label(block, text=num, font=("Helvetica", 16), fg="black", bg="white")
            label.place(relx=0.5, rely=0.5, anchor="center")
            block.grid(row=j, column=i, padx=0, pady=0)

    rootgrid.mainloop()

def destroy_win():
    global rootgrid
    rootgrid.destroy()