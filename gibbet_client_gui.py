# coding: utf-8

# Использование своих модулей
                 
import turtle
import random

x = random.randrange(1, 100)

def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)       
  
def erase():
    >>> turtle.home()
>>> turtle.begin_poly()
>>> turtle.fd(100)
>>> turtle.left(20)
>>> turtle.fd(30)
>>> turtle.left(60)
>>> turtle.fd(50)
>>> turtle.end_poly()
  

def draw_gibbet(step):   
    ''' Виселица
    '''
    turtle.color("blue")
    if step == 1:
        # вертикальная
        draw_line(-160, -100, -160, 80)        
    elif step == 2:
        # горизонтальная
        draw_line(-160, 80, -80, 80)
    elif step == 3:
        # косая - ребро жесткости
        draw_line(-160, 40, -120, 80)    
    elif step == 4:    
        # веревка
        draw_line(-100,80,-100,40)
    elif step == 5:    
        # голова
        gotoxy(-100, 0)
        turtle.circle(20)    
    elif step == 6:
        # туловище
        draw_line(-100,0,-100,-50)
    elif step == 7:    
        # рука левая
        draw_line(-100,-10,-120,-20)
    elif step == 8:    
        # рука правая
        draw_line(-100,-10,-80,-20)
    elif step == 9:    
        # нога левая
        draw_line(-100,-50,-120,-60)
    elif step == 10:        
        # нога правая
        draw_line(-100,-50,-80,-60)



gotoxy(-200,250)
turtle.write("Я загадал число от 1 до 1000.\nПопробуй угадать?", font=("Arial", 18, "normal"))
turtle.write(x)
try_count = 0

answer = turtle.textinput("Давать подсказки?", "Y/N")      # из ДЗ
hints = False
if answer == 'Y':
    hints = True


while True:
    answer = turtle.textinput("Играть?", "Y/N")
    if answer == 'Y':

        number = turtle.numinput("Попробуй угадать", "Число", 0, 0, 100)
        gotoxy(200, 200 - try_count*11)
        turtle.write(number)
        
        gotoxy(-150, 100)
        turtle.write("Неверно!", font=("Arial", 28, "normal"))
            
        if hints:                   # из ДЗ
            gotoxy(250, 200 - try_count*11)
            if number < x:
                turtle.write("Загаданное число больше")
            elif number > x:
                turtle.write("Загаданное число меньше")
        
        if number == x:
            gotoxy(-150, -200)
            turtle.write("Ура!", font=("Arial", 28, "normal"))
            break
        else:
            turtle.color("red")
            gotoxy(-150, 100)
            turtle.write("Неверно!", font=("Arial", 28, "normal"))
            try_count += 1
            draw_gibbet(try_count)
            if try_count == 10:
                turtle.color("red")
                gotoxy(-150, 100)
                
    elif answer == 'N':
        break


    


