import tkinter as tk

disValue = 0
operator = {'＋':1, '－':2, '÷':3, '×':4, 'C':5, '＝':6}
stoValue = 0
opPre = 0

def number_Click(value):                         # 숫자 클릭 정의
    global disValue
    disValue = (disValue*10) + value
    str_value.set(disValue)

def clear():                                      #  Clear 정의
    global disValue, operator, stoValue, opPre
    disValue = 0
    stoValue = 0
    opPre = 0
    str_value.set(disValue)
 

def oprator_Click(value):                          # 연산자 클릭 정의
    global disValue, operator, stoValue, opPre
    op = operator[value]
    if op == 5:          # C
        clear()
    elif disValue == 0:
        opPre = 0
    elif opPre == 0:
        opPre = op
        stoValue = disValue
        disValue = 0
        str_value.set(str(stoValue))
    elif op == 6:         # =
       if opPre == 1:
           disValue = stoValue + disValue
       if opPre == 2:
           disValue = stoValue - disValue
       if opPre == 3:
           disValue = stoValue / disValue
       if opPre == 4:
           disValue = stoValue * disValue

       str_value.set(str(disValue))
       stoValue = 0
       opPre = 0
    else:
        clear()


def Button_Click(value):                              # 버튼 클릭 정의
    try:
        value = int(value)
        number_Click(value)
    except:
        oprator_Click(value)



win = tk.Tk()                      # 창 생성

win.title("계산기")             # 창 제목

# 결과 창 구조
str_value = tk.StringVar()
str_value.set(str(disValue))
dis = tk.Entry(win, textvariable = str_value, justify = 'right', bg = 'whitesmoke', fg = 'black')
dis.grid(column = 0, row = 0, columnspan = 4, ipadx = 90, ipady = 60)

# 버튼 구조
Button_list = [['%','CE','C','Back'],
               ['1/x','x²','²√x','÷'],
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
            fg = 'black',
            command = lambda cmd = item: Button_Click(cmd)
            )
        btn.grid(column = k, row = (i + 1))

win.mainloop()                  # 창 실행

