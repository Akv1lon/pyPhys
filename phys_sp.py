import matplotlib.pyplot as plt
import math as m

v0 = float(input('Введите скорость: '))
angle_deg = float(input('Введите угол: '))
dt = float(input('Введите шаг времени(по-умолчанию - 0.5): ') or 0.5)
g=9.81

angle_rad=m.radians(angle_deg)
vx= v0 * m.cos(angle_rad)
vy=v0 * m.sin(angle_rad)

t_total=(2*vy)/g
x_points=[]
y_points=[]
current_t = 0.0
while current_t <= t_total:
    x = vx * current_t
    y = vy * current_t - 0.5 * g * current_t ** 2
    if y < 0:
        break  

    x_points.append(x)
    y_points.append(y)
    print(f'x= {round(x)}, y={round(y)}, t= {current_t},')
    current_t += dt                              

plt.figure(figsize=(10, 6))
plt.plot(x_points, y_points, 'r-', label='Траектория')

plt.scatter(x_points[0], y_points[0], color='blue', label='Старт')
plt.scatter(x_points[-1], y_points[-1], color='black', label='Падение')
plt.title(f"Траектория снаряда (v0={v0} м/с, угол={angle_deg}°)")
plt.xlabel("Горизонтальная дальность (м)")
plt.ylabel("Высота (м)")
plt.grid(True)
plt.legend()
plt.show()

