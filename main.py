import tkinter as tk
import math

#создание окна с окружностью
root = tk.Tk()
root.title("Анимация движения точки по окружности")

#создание холста для рисования
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

#центр
x1 = 300
y1 = 300
#радиус
r = 200

#создание окружности
circle = canvas.create_oval(x1 - r, y1 - r, x1 + r, y1 + r, outline="blue")

#создание точки
point = canvas.create_oval(x1 - 5, y1 - 5, x1 + 5, y1 + 5, fill="black")

#задаем начальный угол
angle = 0

#задаем скорость движения
speed = 1

#функция обновления позиции точки
def position():
    global angle
    x = x1 + r * math.cos(math.radians(angle))
    y = y1 + r * math.sin(math.radians(angle))
    canvas.coords(point, x-5, y-5, x+5, y+5)
    angle += speed
    root.after(10, position)

#запуск анимации точки
position()

#запуск цикла
root.mainloop()