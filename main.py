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

        df1 = df1[['Time', 'Distance']].groupby('Time').sum()
        df1.plot(kind='line', legend=True, ax=ax1, color='r', fontsize=10)

        # velocity plot

        df2 = df2[['Time', 'Velocity']].groupby('Time').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r', fontsize=10)

        # acceleration plot

        df3 = df3[['Time', 'Acceleration']].groupby('Time').sum()
        df3.plot(kind='line', legend=True, ax=ax3, color='r', fontsize=10)


if __name__ == "__main__":
    matplotlib.use('TkAgg')
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)

    # text fields
    L1 = tk.Label(root, text="Set object mass: ")
    T1 = tk.Entry(root, width=30)
    L1.grid(column=0, row=0, sticky=tk.N)
    T1.grid(column=1, row=0, sticky=tk.N)
    T1.insert(tk.END, "10")

    L2 = tk.Label(root, text="Set B value: ")
    T2 = tk.Entry(root, width=30)
    L2.grid(column=0, row=1, sticky=tk.N)
    T2.grid(column=1, row=1, sticky=tk.N)
    T2.insert(tk.END, "0.1")

    L3 = tk.Label(root, text="Set starting height: ")
    T3 = tk.Entry(root, width=30)
    L3.grid(column=0, row=2, sticky=tk.N)
    T3.grid(column=1, row=2, sticky=tk.N)
    T3.insert(tk.END, "1000")

    figure1 = plt.Figure(figsize=(10, 4), dpi=100)

    line1 = FigureCanvasTkAgg(figure1, root)
    line1.get_tk_widget().grid(column=2, row=0, rowspan=5, padx=20, pady=20)

    ax1 = figure1.add_subplot(131)
    ax2 = figure1.add_subplot(132)
    ax3 = figure1.add_subplot(133)

    ax1.set_title('Distance vs Time')
    ax2.set_title('Velocity vs Time')
    ax3.set_title('Acceleration vs Time')

    def onSimulate():
        paratrooper = Paratrooper(float(T1.get()), float(T2.get()), float(T3.get()))
        paratrooper.display()
        line1.draw_idle()

    def onReset():
        figure1.clf()
        line1.draw_idle()

    # call of function
    simulate = tk.Button(root, text="Simulate", command=onSimulate)
    reset = tk.Button(root, text="Reset", command=onReset)
    simulate.grid(column=0, row=3, sticky=tk.N)
    reset.grid(column=1, row=3, sticky=tk.N)

    root.mainloop()
