# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def on_click(event):
    print('sos')

def _yes(event):
    print("yolo")

def print_hi(name):
    column1 = pandas.read_excel('test.xlsx', sheet_name='Лист1')
    # Use a breakpoint in the code line below to debug your script.
    header = column1.columns.tolist()
    verificationData = column1[header[0]].tolist()
    print(verificationData)

    fig = plt.figure()
    x = range(len(verificationData))
    print(x)
    plt.plot(x,verificationData)

    plt.connect('button_press_event', on_click)
    # button
    axcut = plt.axes([0.9, 0.0, 0.1, 0.075])
    bcut = Button(axcut, 'YES', color='red', hovercolor='green')
    bcut.on_clicked(_yes)

    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
