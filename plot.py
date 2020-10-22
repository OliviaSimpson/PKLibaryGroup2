import matplotlib.pyplot as plt
import numpy as np


def plot(Compartments = [], xdata = [], ydata = [], xlim = 0, ylim = 0, title = "PK Model"):
    for series in range(len(ydata)):
        plt.plot(xdata ,ydata[series])
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    #plt.axis([min(xdata), max(xdata), min(ydata), max(ydata)])
    plt.legend(Compartments,loc='upper right', frameon = True, framealpha=0.9, title="Compatments")
    #plt.show()
    return plt
def add(plt):
    plt.show

graph = plot(["Main","1","2","3"],[1,2,3,4,5,6,7,8],[[2,4,8,16,32,64,128,256],[256,128,64,32,16,8,4,2],[1,1,2,3,5,8,13,21]])
add(graph)