import tkinter

CalSeq =[]
def gui_main():
    MainWindow = tkinter.Tk()
    MainWindow.title('Calculator')
    MainWindow.geometry('470x708+10+10')
    MainWindow.resizable(False, False)

    '''Lable = tkinter.Label(MainWindow, text = 'test label')
    Lable.pack()
    '''
    def do_job():
        print('Buttion Clicked')
    
    
    CalcMenu = tkinter.Menu(MainWindow)
    CalcTypeMenu = tkinter.Menu(CalcMenu, tearoff=0)
    CalcMenu.add_cascade(label='≡ Change Calculator', menu=CalcTypeMenu)
    CalcTypeMenu.add_cascade(label='Standed', command=do_job)
    CalcTypeMenu.add_cascade(label='Scientific', command=do_job)
    CalcTypeMenu.add_cascade(label='</>Programmer', command=do_job)
    CalcTypeMenu.add_command(label='Exit', command=MainWindow.quit)
    MainWindow.config(menu=CalcMenu)
    #CalcTypeMenu.add_separator()    # 添加一条分隔线
    DisPlayText = tkinter.Text(MainWindow, font=('Calibri', 20, "bold"))
    DisPlayText.place(width=470, height=150)
    #DisPlayText.insert('insert', 'i love china')
    ButtonFrame = tkinter.Frame(MainWindow)
    ButtonFrame.place(x=0, y=150)

    def num_insert(num):
        CalSeq.append(str(num))
        DisPlayText.delete(1.0, tkinter.END)
        DisPlayText.insert('insert', ''.join(CalSeq))

    def notation_insert(notation):
        CalSeq.append(notation)
        DisPlayText.delete(1.0, tkinter.END)
        DisPlayText.insert('insert', ''.join(CalSeq))

    def negate():
        popnum = ''
        i = 0
        if len(CalSeq):
            while i<len(CalSeq):
                popelem = CalSeq.pop()
                if not popelem in ['%', '/', '*', '-', '+']:
                    popnum += popelem
                else:
                    CalSeq.append(popelem)
                    break
        negate_num = -1 * float(popnum[::-1])
        CalSeq.append(str(negate_num))
        DisPlayText.delete(1.0, tkinter.END)
        DisPlayText.insert('insert', ''.join(CalSeq))

    def square_root():
        popnum = ''
        i = 0
        if len(CalSeq):
            while i<len(CalSeq):
                popelem = CalSeq.pop()
                try:
                    int(popelem)
                    popnum += popelem
                    popnum = popnum[::-1]
                except Exception:
                    CalSeq.append(popelem)
                    break
        square_root = popnum ** 0.5
        CalSeq.append(str(square_root))
        DisPlayText.delete(1.0, tkinter.END)
        DisPlayText.insert('insert', ''.join(CalSeq))

    def squareOfValue():
        pass
    
    def ce():
        CalSeq.clear()
        DisPlayText.delete(1.0, tkinter.END)
        DisPlayText.insert('insert', '0')

    def return_value():
        DisPlayText.delete(1.0, tkinter.END)
        DisPlayText.insert('insert', eval(''.join(CalSeq)))

    #标准计算器部分按钮定义开始
    '''
    4x110+5x6=470
    6x86+7x6=558
    '''
    #数学字体使用Calibri
    tkinter.Button(MainWindow, text='%', font=('Calibri', 22), command=lambda: notation_insert('%')).place(width=110, height=86, x=6, y=150)
    tkinter.Button(MainWindow, text='√', font=('Calibri', 22), command=square_root).place(width=110, height=86, x=122, y=150)
    tkinter.Button(MainWindow, text='X^2', font=('Calibri', 22), command=do_job).place(width=110, height=86, x=238, y=150)
    tkinter.Button(MainWindow, text='⅟x', font=('Calibri', 22), command=do_job).place(width=110, height=86, x=354, y=150)
    
    tkinter.Button(MainWindow, text='CE', font=('Calibri', 22), command=ce).place(width=110, height=86, x=6, y=242)
    tkinter.Button(MainWindow, text='C', font=('Calibri', 22), command=ce).place(width=110, height=86, x=122, y=242)
    tkinter.Button(MainWindow, text='<-', font=('Calibri', 22), command=do_job).place(width=110, height=86, x=238, y=242)
    tkinter.Button(MainWindow, text='÷', font=('Calibri', 22), command=lambda: notation_insert('/')).place(width=110, height=86, x=354, y=242)
    
    tkinter.Button(MainWindow, text='7', font=('Calibri', 22), command=lambda: num_insert(7)).place(width=110, height=86, x=6, y=334)
    tkinter.Button(MainWindow, text='8', font=('Calibri', 22), command=lambda: num_insert(8)).place(width=110, height=86, x=122, y=334)
    tkinter.Button(MainWindow, text='9', font=('Calibri', 22), command=lambda: num_insert(9)).place(width=110, height=86, x=238, y=334)
    tkinter.Button(MainWindow, text='×', font=('Calibri', 22), command=lambda: notation_insert('*')).place(width=110, height=86, x=354, y=334)

    tkinter.Button(MainWindow, text='4', font=('Calibri', 22), command=lambda: num_insert(4)).place(width=110, height=86, x=6, y=426)
    tkinter.Button(MainWindow, text='5', font=('Calibri', 22), command=lambda: num_insert(5)).place(width=110, height=86, x=122, y=426)
    tkinter.Button(MainWindow, text='6', font=('Calibri', 22), command=lambda: num_insert(6)).place(width=110, height=86, x=238, y=426)
    tkinter.Button(MainWindow, text='-', font=('Calibri', 22), command=lambda: notation_insert('-')).place(width=110, height=86, x=354, y=426)

    tkinter.Button(MainWindow, text='1', font=('Calibri', 22), command=lambda: num_insert(1)).place(width=110, height=86, x=6, y=518)
    tkinter.Button(MainWindow, text='2', font=('Calibri', 22), command=lambda: num_insert(2)).place(width=110, height=86, x=122, y=518)
    tkinter.Button(MainWindow, text='3', font=('Calibri', 22), command=lambda: num_insert(3)).place(width=110, height=86, x=238, y=518)
    tkinter.Button(MainWindow, text='+', font=('Calibri', 22), command=lambda: notation_insert('+')).place(width=110, height=86, x=354, y=518)

    tkinter.Button(MainWindow, text='±', font=('Calibri', 22), command=negate).place(width=110, height=86, x=6, y=610)
    tkinter.Button(MainWindow, text='0', font=('Calibri', 22), command=lambda: num_insert(0)).place(width=110, height=86, x=122, y=610)
    tkinter.Button(MainWindow, text='.', font=('Calibri', 22), command=lambda: notation_insert('.')).place(width=110, height=86, x=238, y=610)
    tkinter.Button(MainWindow, text='=', font=('Calibri', 22), command=return_value).place(width=110, height=86, x=354, y=610)
    #标准计算器部分按钮定义结束
    
    
    MainWindow.mainloop()


gui_main()
