import tkinter as tk

win = tk.Tk()                      # 창 생성

win.title("계산기")             # 창 제목

disValue = 0
str_value = tk.StringVar()
str_value.set(str(disValue))
dis = tk.Entry(win, textvariable = str_value, justify = 'right', bg = 'white', fg = 'black')
dis.grid(column=0, row=0, columnspan=4, ipadx=90, ipady=60)


win.mainloop()                  # 창 실행
