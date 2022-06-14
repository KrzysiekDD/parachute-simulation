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
    def __init__(self, mass: float, B: float, y0: float, ax1, ax2, ax3, H):
        self.mass = mass
        self.B = B
        self.y0 = y0
        self.H = H
        self.ax1 = ax1
        self.ax2 = ax2
        self.ax3 = ax3
        self.data = DataFrame
        self.lastVelocity = 0.0
        self.lastAcceleration = 0.0
        self.elapsedTime = 0.0

    def display(self):
        method = TaylorMethod(self.mass, self.B, self.y0, self.H)
        method.numerical_method()
        length = list(range(len(method.y_position)))

        # data set from TaylorMethod

        self.data = {'Time': length,
                     'Distance': method.y_position,
                     'Velocity': method.y_first_derivative,
                     'Acceleration': method.y_second_derivative
                     }

        self.elapsedTime = len(method.y_position)*self.H
        self.lastVelocity = method.y_first_derivative[-1]
        self.lastAcceleration = method.y_second_derivative[-1]

        # dataframes

        df1 = DataFrame(self.data, columns=['Time', 'Distance'])
        df2 = DataFrame(self.data, columns=['Time', 'Velocity'])
        df3 = DataFrame(self.data, columns=['Time', 'Acceleration'])

        df1['Time'] = self.H*df1['Time']
        df2['Time'] = self.H * df2['Time']
        df3['Time'] = self.H * df3['Time']

        # position plot

        df1 = df1[['Time', 'Distance']].groupby('Time').sum()
        df1.plot(kind='line', legend=True, ax=self.ax1, color='r', fontsize=10, xlabel="Time [s]", ylabel="Distance [m]")

        # velocity plot

        df2 = df2[['Time', 'Velocity']].groupby('Time').sum()
        df2.plot(kind='line', legend=True, ax=self.ax2, color='g', fontsize=10, xlabel="Time [s]", ylabel="Velocity [m/s]")

        # acceleration plot

        df3 = df3[['Time', 'Acceleration']].groupby('Time').sum()
        df3.plot(kind='line', legend=True, ax=self.ax3, color='b', fontsize=10, xlabel="Time [s]", ylabel="Acceleration [m/s^2]")

    def saveToCsv(self):
        df_save = DataFrame(self.data, columns=['Time', 'Velocity', 'Acceleration'])
        df_save.to_csv('output.csv')


if __name__ == "__main__":
    matplotlib.use('TkAgg')
    root = tk.Tk()
    root.geometry("1300x400")

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

    L2 = tk.Label(root, text="Set B value (air resistance): ")
    T2 = tk.Entry(root, width=30)
    L2.grid(column=0, row=1, sticky=tk.N)
    T2.grid(column=1, row=1, sticky=tk.N)
    T2.insert(tk.END, "0.1")

    L3 = tk.Label(root, text="Set starting height: ")
    T3 = tk.Entry(root, width=30)
    L3.grid(column=0, row=2, sticky=tk.N)
    T3.grid(column=1, row=2, sticky=tk.N)
    T3.insert(tk.END, "1000")

    L8 = tk.Label(root, text="Set simulation step: ")
    T4 = tk.Entry(root, width=30)
    L8.grid(column=0, row=3, sticky=tk.N)
    T4.grid(column=1, row=3, sticky=tk.N)
    T4.insert(tk.END, "0.01")

    figure1 = plt.Figure(figsize=(10, 5))
    figure1.tight_layout()

    line1 = FigureCanvasTkAgg(figure1, root)

    # toolbar

    toolbar = NavigationToolbar2Tk(line1, root, pack_toolbar=False)
    toolbar.update()
    toolbar.grid(column=2, row=6)

    # last velocity and acceleration

    lastVel = tk.StringVar()
    elapsedTime = tk.StringVar()

    L4 = tk.Label(root, textvariable=lastVel)
    L5 = tk.Label(root, textvariable=elapsedTime)
    L6 = tk.Label(root, text="Final velocity [m/s]")
    L7 = tk.Label(root, text="Elapsed time [s]")
    L4.grid(column=0, row=6)
    L5.grid(column=1, row=6)
    L6.grid(column=0, row=5)
    L7.grid(column=1, row=5)

    # plots

    line1.get_tk_widget().grid(column=2, row=0, rowspan=5, padx=20, pady=20)

    ax1 = figure1.add_subplot(131)
    ax2 = figure1.add_subplot(132)
    ax3 = figure1.add_subplot(133)

    ax1.set_title('Distance vs Time')
    ax2.set_title('Velocity vs Time')
    ax3.set_title('Acceleration vs Time')

    figure1.tight_layout()

    paratrooper = Paratrooper(float(T1.get()), float(T2.get()), float(T3.get()), ax1, ax2, ax3, float(T4.get()))


    def onSimulate():
        figure1.clf()

        ax1 = figure1.add_subplot(131)
        ax2 = figure1.add_subplot(132)
        ax3 = figure1.add_subplot(133)

        ax1.set_title('Distance vs Time')
        ax2.set_title('Velocity vs Time')
        ax3.set_title('Acceleration vs Time')

        paratrooper.mass = float(T1.get())
        paratrooper.B = float(T2.get())
        paratrooper.y0 = float(T3.get())
        paratrooper.ax1 = ax1
        paratrooper.ax2 = ax2
        paratrooper.ax3 = ax3
        paratrooper.H = float(T4.get())

        paratrooper.display()

        lastVel.set(repr(paratrooper.lastVelocity))
        elapsedTime.set(repr(paratrooper.elapsedTime))

        figure1.tight_layout()
        line1.draw_idle()


    def onReset():
        figure1.clf()
        line1.draw_idle()


    def onSave():
        paratrooper.saveToCsv()


    # buttons

    simulate = tk.Button(root, text="Simulate", command=onSimulate)
    reset = tk.Button(root, text="Reset", command=onReset)
    save = tk.Button(root, text="Save to CSV", command=onSave)

    simulate.grid(column=0, row=4, sticky=tk.N)
    reset.grid(column=1, row=4, sticky=tk.N)
    save.grid(column=2, row=7)

    root.mainloop()
