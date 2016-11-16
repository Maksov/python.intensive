# coding: utf-8

# Первая часть интенсива.
# Игра "Виселица" с простым графическим интерфейсом
                 
import turtle
import random
import sys

# Для Python 2.x нужно раскомментировать следующую строку:
# import tkSimpleDialog   


# Загадываем число
x = random.randrange(1, 100)

def gotoxy(x,y):
    ''' Перемещение курсора без оставления следа черепашки
    '''
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    
def draw_line(from_x, from_y, to_x, to_y):
    ''' Рисование линии из точки (from_x, from_y) в точку (to_x, to_y)
    '''
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)     

  
def erase():
    ''' Стирание указанной области
    '''
    turtle.home()
    turtle.begin_poly()
    turtle.fd(100)
    turtle.left(20)
    turtle.fd(30)
    turtle.left(60)
    turtle.fd(50)
    turtle.end_poly()
  

def draw_gibbet(step):   
    ''' Пошаговое рисование виселицы
    '''
    turtle.color("blue")
    if step == 1:
        # вертикальная линия
        draw_line(-160, -100, -160, 80)        
    elif step == 2:
        # горизонтальная линия
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


# Основной код программы

answer = turtle.textinput("Играть?", "y/n")
if answer == 'n':
    sys.exit()


gotoxy(-200,250)
turtle.write("Я загадал число от 1 до 1000.\nПопробуй угадать?", font=("Arial", 18, "normal"))
turtle.write(x)
try_count = 0


answer = turtle.textinput("Давать подсказки?", "Y/N")
#tkSimpleDialog.askstring("Нарисовать окружность", "Y/N")       # для 2.x Python

hints = False
if answer == 'Y':
    hints = True


while True:

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


    


