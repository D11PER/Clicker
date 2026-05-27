import tkinter as tk

root = tk.Tk()
root.geometry("250x200")
root.title("Clicker")
root.resizable(False, False)

count = 0


def click():
    global count
    count = count + 1
    Click.configure(text=count)  # Fixed: removed extra parenthesis

def click2():
    global count
    count = count * 10
    Click.configure(text=count)

def click3():
    global count
    count = count / 10
    Click.configure(text=count)



Click = tk.Label(root, text="0", font=("Arial", 20)) # Window
Click.pack()

btn = tk.Button(root, text="Click me * 10", padx=20, command=click2)
btn.pack()

btn = tk.Button(root, text="Click me + 1", padx=20, command=click)
btn.pack()

btn = tk.Button(root, text="Click me / 10", padx=20, command=click3)
btn.pack()


root.mainloop()
