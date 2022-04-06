import tkinter as tk

window = tk.Tk()

label = tk.Label(text="")
label.grid(row=0, columnspan=6)

def OnClick0():
    label["text"] = label["text"] + "0"
def OnClick1():
    label["text"] = label["text"] + "1"
def OnClick2():
    label["text"] = label["text"] + "2"
def OnClick3():
    label["text"] = label["text"] + "3"
def OnClick4():
    label["text"] = label["text"] + "4"
def OnClick5():
    label["text"] = label["text"] + "5"
def OnClick6():
    label["text"] = label["text"] + "6"
def OnClick7():
    label["text"] = label["text"] + "7"
def OnClick8():
    label["text"] = label["text"] + "8"
def OnClick9():
    label["text"] = label["text"] + "9"
button0 = tk.Button(text="0", command=OnClick0, height=3, width=7)
button0.grid(row=3, column=3)
button1 = tk.Button(text="1", command=OnClick1, height=3, width=7)
button1.grid(row=1, column=0)
button2 = tk.Button(text="2", command=OnClick2, height=3, width=7)
button2.grid(row=1, column=1)
button3 = tk.Button(text="3", command=OnClick3, height=3, width=7)
button3.grid(row=1, column=2)
button4 = tk.Button(text="4", command=OnClick4, height=3, width=7)
button4.grid(row=2, column=0)
button5 = tk.Button(text="5", command=OnClick5, height=3, width=7)
button5.grid(row=2, column=1)
button6 = tk.Button(text="6", command=OnClick6, height=3, width=7)
button6.grid(row=2, column=2)
button7 = tk.Button(text="7", command=OnClick7, height=3, width=7)
button7.grid(row=3, column=0)
button8 = tk.Button(text="8", command=OnClick8, height=3, width=7)
button8.grid(row=3, column=1)
button9 = tk.Button(text="9", command=OnClick9, height=3, width=7)
button9.grid(row=3, column=2)

def OnClickplus():
    label["text"] = label["text"] + " + "
buttonplus = tk.Button(text="+", command=OnClickplus, height=3, width=7)
buttonplus.grid(row=1, column=4)
def OnClickminus():
    label["text"] = label["text"] + " - "
buttonminus = tk.Button(text="-", command=OnClickminus, height=3, width=7)
buttonminus.grid(row=2, column=4)
def OnClickmultiply():
    label["text"] = label["text"] + " x "
buttonmultiply = tk.Button(text="x", command=OnClickmultiply, height=3, width=7)
buttonmultiply.grid(row=3, column=4)
def OnClickdivide():
    label["text"] = label["text"] + " ÷ "
buttondivide = tk.Button(text="÷", command=OnClickdivide, height=3, width=7)
buttondivide.grid(row=1, column=3)

def OnClickclear():
    label["text"] = ""
buttonclear = tk.Button(text="clr", command=OnClickclear, height=3, width=7)
buttonclear.grid(row=2, column=5)

def OnClickdot():
    label["text"] = label["text"] + "."
buttondot = tk.Button(text=".", command=OnClickdot, height=3, width=7)
buttondot.grid(row=2, column=3)

def OnClickdel():
    def Convert(string):
        li1 = list(string.split(" "))
        return li1
    x = label["text"]
    y = (Convert(x))
    print (y)
    die = label["text"]
    label["text"] = (die[:-1])  
    if y[2] == '':
        die = label["text"]
        label["text"] = (die[:-2]) 
buttondel = tk.Button(text="del", command=OnClickdel, height=3, width=7)
buttondel.grid(row=1, column=5)

def OnClickequal():
    def Convert(string):
        li1 = list(string.split(" "))
        return li1
    def convert(string):
        li2 = list(string.split("."))
        return li2
  
    # Driver code    
    x = label["text"]
    y = (Convert(x))
    print (y)
    if (y[1]) == "+":
        z = float(y[0]) + float(y[2])
        a = (convert(str(z)))
        if (a[1]) == "0":
            z = round(z)
        label["text"] = str(z)
    if (y[1]) == "-":
        z = float(y[0]) - float(y[2])
        a = (convert(str(z)))
        if (a[1]) == "0":
            z = round(z)
        label["text"] = str(z)
    if (y[1]) == "x":
        z = float(y[0]) * float(y[2])
        a = (convert(str(z)))
        if (a[1]) == "0":
            z = round(z)
        label["text"] = str(z)
    if (y[1]) == "÷":
        z = float(y[0]) / float(y[2])
        a = (convert(str(z)))
        if (a[1]) == "0":
            z = round(z)
        label["text"] = str(z)
buttonequal = tk.Button(text="=", command=OnClickequal, height=3, width=7)
buttonequal.grid(row=3, column=5)

window.title("calculator")
window.iconbitmap("cal.ico")
window.mainloop()