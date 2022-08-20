import tkinter as tk

win = tk.Tk()                      # 창 생성

win.title("계산기")             # 창 제목

disValue = 0
str_value = tk.StringVar()
str_value.set(str(disValue))
dis = tk.Entry(win, textvariable = str_value, justify = 'right', bg = 'whitesmoke', fg = 'black')
dis.grid(column=0, row=0, columnspan=4, ipadx=90, ipady=60)

Button_list = [['%','CE','C','Back'],
               ['1/x','x^2','2√x','÷'],
               ['7','8','9','×'],
               ['4','5','6','－'],
               ['1','2','3','＋'],
               ['+/-','0','.','＝']]

for i,items in enumerate(Button_list):
    for k,item in enumerate(items):

        try:
            color = int(item)
            color = 'white'
        except:
            color = 'whitesmoke'

        btn = tk.Button(win,
            text = item,
            width = 10,
            height = 3,
            bg = color,
            fg = 'black'
            )
        btn.grid(column=k, row=(i+1))

win.mainloop()                  # 창 실행
