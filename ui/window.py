
from tkinter import *
from tabulate import tabulate
import tkinter.ttk as ttk
from tkinter import messagebox, scrolledtext
from ttkthemes import ThemedTk
from modules.bin import BinConvetor
from modules.oct import OctCoversion
from modules.hex import HexConvertor
theme =["black", "aquativo", "equilux", "arc", "blue", "breeze",
         "clearlooks", "elegance", "itfti","karamic","kroc","plastik",
         "radience","scid themes","smog","winxpblue", "radiance"]
global themes
themes = [theme[0],theme[3], theme[6], theme[7], theme[10], theme[11], theme[15]]
class Window:
    def __init__(self):
        self.title_ = "Bin, Hex, Dec and Oct Guru"
        return
    def convert(self, number, number_input, output_screen, type_conversion, working, notebook):
        tageted_tab = notebook.index("current")
        if tageted_tab == 0:
            parts = str(number).split('.')
            if len(parts) == 1:
                number_ =int(number)
            else:
                number_ = float(number)
            if type_conversion.get() == "Binary (base 2)":
                output = BinConvetor.from_dec_to_binary("", number_)

                working.delete('0.0', END)
                working.insert(END, '{:7s}|{:14s}|{:10s}\n'.format("Base", "Number", "Remainder"))
                # working.insert(END, '{:5s}|{:10s}|{:2s}\n'.format("2", str(i[1]), str(i[0])))
                for i in output:
                    working.insert(END, '-------------------------------------------\n')
                    if str(i[1])=="pass":
                        working.insert(END, '{:>10} | {:<20}|{:>20}\n'.format("2",str(i[0]), ""))
                    else:
                        working.insert(END, '{:>10} | {:<20}|{:>20}\n'.format("2", str(i[0]), str(i[1])))

                working.insert(END, "\n\n To Read the converted number 'Read the remainders from bottom to top'")
                converted_number=[]
                for i in output:
                    converted_number.append(i[1])
                converted_number.reverse()
                converted_number.pop()
                converted_number_string =''
                for i in converted_number:
                    converted_number_string += str(i)
                output_screen.delete('0.0', END)
                output_screen.insert('0.0', f'{number} to binary (base 2) is {converted_number_string}')
                # print(type_conversion.get())
            else:
                output = BinConvetor.from_binary_to_dec("", number_)
                output_screen.delete('0.0', END)
                # print(output) 0b1100 =12
                output_screen.insert('0.0', f'{number} to decimal (base 10) is {str(output).split("b")[-1]}')
        elif tageted_tab== 1:
            parts = str(number).split('.')
            if len(parts) == 1:
                number_ = int(number)
            else:
                number_ = float(number)
            if type_conversion.get() == "Octal (base 8)":
                output = OctCoversion.dec_to_oct("", number_)

                working.delete('0.0', END)
                working.insert(END, '{:7s}|{:14s}|{:10s}\n'.format("Base", "Number", "Remainder"))
                for i in output:
                    working.insert(END, '-------------------------------------------\n')
                    if str(i[1]) == "pass":
                        working.insert(END, '{:>10} | {:<20}|{:>20}\n'.format("2", str(i[0]), ""))
                    else:
                        working.insert(END, '{:>10} | {:<20}|{:>20}\n'.format("2", str(i[0]), str(i[1])))
                working.insert(END, "\n\n To Read the converted number 'Read the remainders from bottom to top'")

                converted_number = []
                for i in output:
                    converted_number.append(i[1])
                converted_number.reverse()
                converted_number.pop()
                converted_number_string = ''
                for i in converted_number:
                    converted_number_string += str(i)
                output_screen.delete('0.0', END)
                output_screen.insert('0.0', f'{number} to octal (base 8) is {converted_number_string}')
        else:
            parts = str(number).split('.')
            if len(parts) == 1:
                number_ = int(number)
            else:
                number_ = float(number)
            if type_conversion.get() == "Hexadecimal (base 16)":
                output = HexConvertor.dec_to_hex("", number_)

                working.delete('0.0', END)
                working.insert(END, '{:7s}|{:14s}|{:10s}\n'.format("Base", "Number", "Remainder"))
                for i in output:
                    working.insert(END, '-------------------------------------------\n')
                    if str(i[1]) == "pass":
                        working.insert(END, '{:>10} | {:<20}|{:>20}\n'.format("2", str(i[0]), ""))
                    else:
                        working.insert(END, '{:>10} | {:<20}|{:>20}\n'.format("2", str(i[0]), str(i[1])))
                working.insert(END, "\n\n To Read the converted number 'Read the remainders from bottom to top'")

                converted_number = []
                for i in output:
                    converted_number.append(i[1])
                converted_number.reverse()
                converted_number.pop()
                converted_number_string = ''
                for i in converted_number:
                    converted_number_string += str(i)
                output_screen.delete('0.0', END)
                output_screen.insert('0.0', f'{number} to hexadecimal (base 16) is {converted_number_string}')
        number_input.delete(0, END)
        return
    def reset(self, target1, target2, target3):
        choice = messagebox.showwarning(self.title_, "RESETING THE WORKPLACE MAY RESULT IN LOSING SOME IMPORTANT "
                                                     "UNSAVED "
                                                     "INFORMATION")
        if choice:
            target1.delete(0, END)
            target2.delete('0.0', END)
            target3.delete('0.0', END)
        return
    def close(self, root):
        choice = messagebox.askyesnocancel(self.title_, "ARE YOU SURE YOU WANT TO CLOSE {}?".format(self.title_))
        if(choice):
            root.destroy() or root.quit()
        else:
            root.focus()
        return
    def clear(self, target, target_name):
        choice = messagebox.askyesnocancel(self.title_, "ARE YOU SURE YOU WANT TO CLEAR {}?".format(target_name))
        if choice:
            target.delete('0.0', END)
        else:
            target.focus()
        return

    def tabContents(self, tab, number_options, label_title, root, forcused_tab, notebook):
        option = StringVar()
        frame_left = Frame(tab)
        # contents of frame left
        Label(tab, text=label_title, font=("Arial", 13, "bold")).grid(row=0, column=0, pady=10, columnspan=10)
        Label(frame_left, text="SELECT BASE", font=('Arial', 11, "bold")).grid(row=1, column=0, sticky=W, pady=5)
        number_option = ttk.OptionMenu(frame_left, option, number_options[0], *number_options)
        number_option.grid(row=1, column=1, sticky=W)
        Label(frame_left, text="NUMBER", font=('Arial', 11, "bold")).grid(row=2, column=0, sticky=W, pady=5)
        number = ttk.Entry(frame_left, width=26)
        number.grid(row=2, column=1, sticky=W)
        Button(frame_left, text="Convert", bg="green", fg="white", font=("Arial", 12, "bold"), width=15, relief=SOLID,
               bd=0, command=lambda:self.convert(number.get(),  number_input=number,
                                                 output_screen=output_left, type_conversion=option, working=working,
                                                 notebook=notebook
                                                 )).grid(
            row=3, column=0,
                                                                                               padx=5, pady=5)
        Button(frame_left, text="Reset", bg="orange", fg="white", font=("Arial", 12, "bold"), width=15, relief=SOLID,
               bd=0, command=lambda :self.reset(number, output_left, working)).grid(row=3, column=1, padx=5, pady=5)
        Label(frame_left, text="Output", font=('Arial', 11, "bold")).grid(row=4, column=0, sticky=W, pady=5)
        output_left = Text(frame_left, width=35, height=5, font=("Arial", 12))
        output_left.grid(row=5, column=0, columnspan=2, pady=2, sticky=W, padx=5)
        frame_left.grid(row=1, column=0, columnspan=7, pady=10, sticky=W)
        frame_right = Frame(tab)
        Label(frame_right, text="Working", font=('Arial', 11, "bold")).grid(row=0, column=0, sticky=W, pady=5,
                                                                            columnspan=3, padx=5)
        working = scrolledtext.ScrolledText(frame_right, font=('Arial', 11), width=40, height=15)
        working.grid(row=1, column=0, columnspan=3, sticky=W, pady=5, padx=5, rowspan=6)
        Button(frame_right, text="Clear", bg="green", fg="white", font=("Arial", 12, "bold"), width=10, relief=SOLID,
               bd=0, command=lambda:self.clear(working, "Working Space")).grid(row=7, column=0, padx=5, pady=5)
        Button(frame_right, text="Reset", bg="orange", fg="white", font=("Arial", 12, "bold"),command=lambda
        :self.reset(number, output_left, working), width=10, relief=SOLID,
               bd=0).grid(row=7, column=1, padx=5, pady=5)
        Button(frame_right, text="Close", bg="red", fg="white", font=("Arial", 12, "bold"), width=10, relief=SOLID,
               bd=0, command= lambda : self.close(root=root)).grid(row=7, column=2, padx=5, pady=5)
        frame_right.grid(row=1, column=7, columnspan=3, pady=10, sticky=W)
        return
    def main(self):
        root = Tk()
        width = 760
        height = 480
        title_ = "Bin, Hex, Dec and Oct Guru"
        window_width = root.winfo_screenwidth()
        window_height = root.winfo_screenheight()
        pos_top = int(window_height/2 - height/2)
        pos_right = int(window_width/2 - width/2)
        root.title(title_)
        root.iconbitmap()
        root.geometry(f'{width}x{height}+{pos_right}+{pos_top}')
        root.resizable(False, False)
        # Adding a notebook
        notebook = ttk.Notebook(root, height=height, width=width, padding=20)
        # Binary Tab
        bin_tab = Frame(notebook)
        number_options1 = ['Binary (base 2)', "Decimal base(10)"]
        label_title1 = "CONVERTING NUMBERS FROM BINARY TO DECIMAL OR FROM DECIMAL TO BINARY"
        self.tabContents(bin_tab, number_options=number_options1, label_title=label_title1, root=root,
                         forcused_tab="bin", notebook=notebook)
        # Octal Tab
        oct_tab = Frame(notebook)
        number_options2 = ['Octal (base 8)', "Decimal base(10)"]
        label_title2= "CONVERTING NUMBERS FROM OCTAL TO DECIMAL OR FROM DECIMAL TO OCTAL"
        self.tabContents(oct_tab, number_options=number_options2, label_title=label_title2, root=root,
                         forcused_tab="oct", notebook=notebook)
        # Hexadecimal Tab
        hex_tab = Frame(notebook)
        number_options3 = ['Hexadecimal (base 16)', "Decimal base(10)"]
        label_title3 = "CONVERTING NUMBERS FROM HEX TO DECIMAL OR FROM DECIMAL TO HEX"
        self.tabContents(hex_tab, number_options=number_options3, label_title=label_title3, root=root,
                         forcused_tab="hex", notebook=notebook)
        notebook.add(bin_tab, text="Binary Conversion")
        notebook.add(oct_tab, text="Octal Conversion")
        notebook.add(hex_tab, text="Hexadecimal Conversion")
        notebook.pack()
        root.mainloop()
        return

""""
loan = 10000
6.5% intrest rate + 1000
"""