import numpy as np
import matplotlib.pyplot as plt

def brown_move(t=1.0, n=1000):
    t=float(input('Ведите время(по-умолчанию 1.0): ') or 1.0)
    n=int(input('Введите шаг времени(по-умолчанию 1000): ') or 1000)
    dt = t/n
    #dw = np.random.normal(0, np.sqrt(dt), n)
    
    #W = np.zeros(n+1)
    #W[1:] = np.cumsum(dw)
    dWx = np.random.normal(0, np.sqrt(dt), n)
    dWy = np.random.normal(0, np.sqrt(dt), n)
    
    Wx = np.zeros(n+1)
    Wy = np.zeros(n+1)
    
    Wx[1:] = np.cumsum(dWx)
    Wy[1:] = np.cumsum(dWy)
    
    #T = np.linspace(0, t, n+1)
    
    #plt.plot(T, W)
    #plt.figure(figsize=(8,6))
    plt.plot(Wx, Wy, linewidth=0.5)
    plt.title("Броуновское движение в 2D")
    plt.xlabel("Движение по X")
    plt.scatter(Wx[0], Wy[0], marker='o', color='blue', label='Начало')
    plt.scatter(Wx[-1], Wy[-1], marker='o', color='red', label='Конец')
    plt.ylabel("Двжиение по Y")
    plt.legend()
    plt.grid()
    plt.show()
    
brown_move()

