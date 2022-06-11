import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib
from pandas import DataFrame
from TaylorMethod import TaylorMethod
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class Paratrooper:
    def __init__(self, mass: float, B: float, y0: float):
        self.mass = mass
        self.B = B
        self.y0 = y0

    def display(self):

        method = TaylorMethod(self.mass, self.B, self.y0)
        method.numerical_method()
        length = list(range(len(method.y_position)))

        # data set from TaylorMethod

        data = {'Time': length,
                'Distance': method.y_position,
                'Velocity': method.y_first_derivative,
                'Acceleration': method.y_second_derivative
                }

        # dataframes
        df1 = DataFrame(data, columns=['Time', 'Distance'])
        df2 = DataFrame(data, columns=['Time', 'Velocity'])
        df3 = DataFrame(data, columns=['Time', 'Acceleration'])

        # position plot

        figure1 = plt.Figure(figsize=(5, 4), dpi=100)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, root)
        line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = df1[['Time', 'Distance']].groupby('Time').sum()
        df1.plot(kind='line', legend=True, ax=ax1, color='r', fontsize=10)
        ax1.set_title('Distance vs Time')

        # velocity plot

        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, root)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2 = df2[['Time', 'Velocity']].groupby('Time').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r', fontsize=10)
        ax2.set_title('Velocity vs Time')

        # acceleration plot

        figure3 = plt.Figure(figsize=(5, 4), dpi=100)
        ax3 = figure3.add_subplot(111)
        line3 = FigureCanvasTkAgg(figure3, root)
        line3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df3 = df3[['Time', 'Acceleration']].groupby('Time').sum()
        df3.plot(kind='line', legend=True, ax=ax3, color='r', fontsize=10)
        ax3.set_title('Acceleration vs Time')

if __name__ == "__main__":
    matplotlib.use('TkAgg')
    root = tk.Tk()
    # text fields
    T1 = tk.Entry(root, width=30)
    T1.pack()
    T1.insert(tk.END, "10")

    T2 = tk.Entry(root, width=30)
    T2.pack()
    T2.insert(tk.END, "0.1")

    T3 = tk.Entry(root, width=30)
    T3.pack()
    T3.insert(tk.END, "1000")

    def onSimulate():
        paratrooper = Paratrooper(float(T1.get()), float(T2.get()), float(T3.get()))
        paratrooper.display()

    # call of function
    simulate = tk.Button(root, text = "Simulate", command = onSimulate)
    simulate.pack()

    root.mainloop()