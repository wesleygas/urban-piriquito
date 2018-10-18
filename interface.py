try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter
# needs Python25 or higher

from functools import partial
from signalTeste import *
import matplotlib.pyplot as plt
#matplotlib.use('TkAgg')

num ='12'
sig = signalMeu()
def numero():
    global num, sig
    def on_key_press(event):
        global num, sig
        num = repr(event.char)
        num = num[1:-1]
        print(int(num))
        tempo, sinal = sig.geraNum(int(num))
        sig.playSig(sinal)
        plt.close("all")
        plt.plot(tempo[0:500],sinal[0:500])
        plt.show(block=False)
        
        
    def click(btn):
        global num, sig
        # test the button command click
        if(btn == "exit"):
            boot.quit()
        else:
            print(int(btn))
            tempo, sinal = sig.geraNum(int(btn), duration=2)
            sig.playSig(sinal)
            plt.close("all")
            plt.plot(tempo[0:500],sinal[0:500])
            #tempo, sinal = sig.calcFFT(sinal, 48000)
            #plt.plot(tempo,sinal)
            plt.show(block=False)
            
            
            
        num = btn
        #return num

    boot = tkinter.Tk()

    boot['bg'] = 'green'
    # create a labeled frame for the keypad buttons
    # relief='groove' and labelanchor='nw' are default
    lf = tkinter.LabelFrame(boot, bd=8)
    lf.pack(padx=15, pady=15)
    # typical calculator button layout
    btn_list = [
        '1',  '2',  '3',
        '4',  '5',  '6',
        '7',  '8',  '9',
        '','0', 'exit']
    # create and position all buttons with a for-loop
    # r, c used for row, column grid values
    r = 1
    c = 0
    n = 0
    # list(range()) needed for Python3
    btn = list(range(len(btn_list)))
    for label in btn_list:
        # partial takes care of function and argument
        cmd = partial(click, label)
        # create the button
        btn[n] = tkinter.Button(lf, text=label, width=10, height=5, command=cmd)
        # position the button
        btn[n].grid(row=r, column=c)
        # increment button index
        n += 1
        # update row/column position
        c += 1
        if c == 3:
            c = 0
            r += 1

    frame = tkinter.Frame(boot, width=100, height=100)
    frame.bind("<KeyRelease-1>", on_key_press)
    frame.bind("<KeyRelease-2>", on_key_press)
    frame.bind("<KeyRelease-3>", on_key_press)
    frame.bind("<KeyRelease-4>", on_key_press)
    frame.bind("<KeyRelease-5>", on_key_press)
    frame.bind("<KeyRelease-6>", on_key_press)
    frame.bind("<KeyRelease-7>", on_key_press)
    frame.bind("<KeyRelease-8>", on_key_press)
    frame.bind("<KeyRelease-9>", on_key_press)
    frame.bind("<KeyRelease-0>", on_key_press)
    frame.pack()
    frame.focus_set()



    tk = boot
    tk.resizable(width=False, height=False)
    tk.mainloop()




if __name__ == '__main__':
    numero()