from tkinter import *

def button_click1():
    print("Button has been clicked.")

def button_click2():
    root.destroy()
    print("Quit")
root = Tk()

root.title("SiSo")
root.geometry("460x330")
root.resizable(False,False)

# main frame
main_Frame1 = Frame(root, width=200, height=200, bg='blue').grid(row=0, column=0, padx=10, pady=5)
main_Frame2 = Frame(root, width=200, height=200, bg='red').grid(row=0, column=1, padx=10, pady=5)

# button
button1 = Button(main_Frame1, text="Button", command=button_click1).grid(row=0, column=0)
button2 = Button(main_Frame2, text="Quit", command=button_click2).grid(row=0, column=1)

# input
input_text = Text(main_Frame1, width=30, height=1)
input_text.insert(INSERT, "Hello")
# input_text.delete("1.0","1.3")
input_text.grid(row=1, column=0)

# Label
Label(main_Frame1, text="Label").grid(row=2, column=0)

# CheckButton
CheckButton1 = Checkbutton(main_Frame2, text="aa").grid(row=1, column=1)
CheckButton2 = Checkbutton(main_Frame2, text="aa").grid(row=2, column=1)
CheckButton3 = Checkbutton(main_Frame2, text="aa").grid(row=3, column=1)
CheckButton4 = Checkbutton(main_Frame2, text="aa").grid(row=4, column=1)

root.mainloop()