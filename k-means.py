"""
Created on Tue Nov 24 22:02:29 2020

@author: Mu-Ping
"""

import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import animation

def gen_data():
    global data
    data=[]
    plt.clf()
    plt.title("Data")
    for _ in range(cluster.get()): #群數
        center_x = np.random.randint(-60, 60)
        center_y = np.random.randint(-60, 60)
        for _ in range(np.random.randint(20, 30)): #一群的點數
            new_x = center_x + np.random.uniform(-5, 5)
            new_y = center_y + np.random.uniform(-5, 5)
            data.append([new_x, new_y])
            plt.plot(new_x, new_y, 'o', ms=4 , color = 'gray', alpha=.8) #畫圖 ms：折點大小
    data = np.array(data)
    canvas1.draw()
    
    
def start():    
    ani = animation.FuncAnimation(fig=fig, func=update, frames=frames, init_func = init, interval=1200, blit=False, repeat=False) #動畫
    canvas1.draw()
    

def init(): 
    pass
        
def update(i): #2維資料更新參數
    pass
        
        
def frames(): # 禎數生成器
    for i in range(1,60):
        yield i%2

window = tk.Tk()
window.geometry("480x390")
window.resizable(False, False)
window.title("k-means 演算法")

#全域變數
cluster = tk.IntVar()#群
cluster.set(3)
color = ["#FF0000", "#0000E3", "#FFD306", "#FF5809", "#02DF82", "#6F00D2", "#73BF00"]
center = [] #群心
center_data = [[] for _ in range(cluster.get())] #群心資料
plot = [] #群心圖


setting1 = tk.Frame(window)
setting1.grid(row=0, column=0, padx=10, pady=10)
tk.Label(setting1, font=("微軟正黑體", 12, "bold"), text="群數(k值)").grid(row=0, sticky=tk.W, pady=5)
tk.Entry(setting1, width=10, textvariable=cluster).grid(row=1, sticky=tk.W)

btn = tk.Button(setting1, text='隨機產生資料', command = gen_data)
btn.grid(row=8, sticky=tk.W, pady=20)
btn = tk.Button(setting1, text='開始分類', command = start)
btn.grid(row=9, sticky=tk.W)

setting2 = tk.Frame(window)
setting2.grid(row=0, column=1, pady=10)
fig = plt.figure(figsize=(5,5))
plt.title("Data")
canvas1 = FigureCanvasTkAgg(fig, setting2)  # A tk.DrawingArea.
canvas1.get_tk_widget().grid()

window.mainloop()