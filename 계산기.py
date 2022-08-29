from contextlib import redirect_stderr
import tkinter as tk

disValue = 0
operator = {'+':1, '-':2, '÷':3, 'x':4, 'C':5, '=':6, 'Back':7}
stoValue = 0
opPre = 0

### 0~9까지의 숫자를 클릭할 때 정의
def number_Click(value):                         
    global disValue
    disValue = (disValue*10) + value            # 숫자를 클릭할 때마다 10의 자리씩 이동
    str_value.set(disValue)                     # 화면에 숫자를 나타낸다

###  C를 클릭할 때 Clear 정의
def clear():                                      
    global disValue, operator, stoValue, opPre
    disValue = 0                                # 주요 변수 초기화
    stoValue = 0
    opPre = 0
    str_value.set(disValue)                     # 화면을 지운다
 
### +-= 연산자 클릭할 때 정의
def oprator_Click(value):                          
    global disValue, operator, stoValue, opPre

    # value의 값에 따라 숫자로 연산자를 변경한다 (+는 1, -는 2, ...)
    op = operator[value]

    if op == 5:         # C (clear)
        clear()
    
    elif disValue == 0:                         # 현재 화면에 출력된 값이 0일 때
        opPre = 0
    
    elif opPre == 0:                            # 연산자가 한번도 클릭되지 않았을 때
        opPre = op                              # 현재 눌린 연산자가 있으면 저장
        stoValue = disValue                     # 현재까지의 숫자를 저장
        disValue = 0                            # 연산자 이후의 숫자를 받기 위해 초기화
        str_value.set(str(stoValue))            # 0으로 다음 숫자를 받을 준비
   
    elif op == 6:        # = (결과를 계산하고 출력)
       if opPre == 1:      # +
           disValue = stoValue + disValue
       if opPre == 2:      # -
           disValue = stoValue - disValue
       if opPre == 3:      # /
           disValue = stoValue / disValue
       if opPre == 4:      # x
           disValue = stoValue * disValue

       str_value.set(str(disValue))             # 최종 결과 값을 출력
       stoValue = 0
       opPre = 0

    else:
        clear()

### 버튼 클릭 정의
def Button_Click(value):                              
    try:
        value = int(value)                  # 정수로 변환
        number_Click(value)                 # 정수인 경우 number_Click()를 호출
    except:
        oprator_Click(value)                # 정수가 아닌 연산자인 경우 oprator_Click() 호출



win = tk.Tk()                      # 창 생성

win.title("계산기")                # 창 제목

### 결과 창 구조
str_value = tk.StringVar()
str_value.set(str(disValue))
dis = tk.Entry(win, textvariable = str_value, justify = 'right', bg = 'whitesmoke', fg = 'black')
dis.grid(column = 0, row = 0, columnspan = 4, ipadx = 90, ipady = 60)

### 버튼 구조
Button_list = [['%','CE','C','Back'],
               ['1/x','x²','²√x','÷'],
               ['7','8','9','x'],
               ['4','5','6','-'],
               ['1','2','3','+'],
               ['+/-','0','.','=']]

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

win.mainloop()                    # 창 실행