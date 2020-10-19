from tkinter import Tk,Button,Label,DoubleVar,Entry
# Tk for main window creation
#Button for button creation
#Label for label creation
#DoubleVar is data_point includes floating point number
#Entry for input place

#MAIN WINDOW DESIGN
window = Tk() #window or Container created
window.title("Feet to Meter Conversion App")
window.configure(background = "Blue")
window.geometry("420x320")
window.resizable(width = False, height = False)

#function for convert_button
def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set("%.4f" %meter)

#function for clear button
def clear():
    ft_value.set("")
    mt_value.set("")

#for label creation and properties

ft_lbl = Label(window, text = "Feet", bg = "white", fg = "black", width = 20)
ft_lbl.grid(column = 0,row = 0,padx = 20,pady = 20 )

#entry or input for feet Label
ft_value = DoubleVar()
ft_entry = Entry(window,textvariable = ft_value, width = 20)
ft_entry.grid(column = 1, row = 0)
ft_entry.delete(0,'end')

#for label creation and properties of meter

mt_lbl = Label(window, text = "Meter", bg = "white", fg = "black", width = 20)
mt_lbl.grid(column = 0,row = 1)

#entry or input for meter Label
mt_value = DoubleVar()
mt_entry = Entry(window,textvariable = mt_value, width = 20)
mt_entry.grid(column = 1, row = 1, pady = 30)
mt_entry.delete(0,'end')

#creating CONVERT Button

convert_btn = Button(window, text = "Convert", bg = "white", fg = "black", width = 20, command = convert)
convert_btn.grid(column = 0,row = 3, padx = 20, pady = 60)

#creating CLEAR Button

clr_btn = Button(window, text = "Clear", bg = "white", fg = "black", width = 20, command = clear)
clr_btn.grid(column = 1,row = 3, pady = 60)

window.mainloop()
