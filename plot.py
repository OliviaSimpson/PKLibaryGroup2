import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class plot():
    def __init__(self, masses=[],times=[]):
        solveData = pd.DataFrame(data = masses, columns=times)
        self.currentData = solveData.transpose()

    def adddata (self,newData=[], newtimeseries=[]):
        newData = np.array(newData)

        if len(newData.shape) == 1:
            newData = pd.DataFrame(data = [newData], columns=newtimeseries)
        else:
            newData = pd.DataFrame(data = newData, columns=newtimeseries)



        newData = newData.transpose()

        self.currentData = pd.concat([self.currentData, newData], axis=1, sort=False)

        self.show()
    def show(self):

        self.setupFig()
        self.fig = plt.plot(self.currentData)
        plt.show()



    def setupFig(self, title="PK Model", xunits="",yunits=""):
        """establishes a matplotlib figure to hold the graph displaying the results of the PK model

        :param title: Title displayed above graph, defaults to "PK Model"
        :type title: string, optional
        :param xunits: units for time on the axis, defaults to ""
        :type xunits: string, optional
        :param yunits: units for mass of the drug administered, defaults to ""
        :type yunits: string, optional
        ...
        :raises [ErrorType]: [ErrorDescription]
        ...
        :return: matplotlib figure
        :rtype: class 'matplotlib.figure.Figure'
        """
        self.fig = plt.figure()
        self.fig.suptitle(title)
      
                
        ax = self.fig.add_subplot(1,1,1)
        ax.set_xlabel("Time"+self.__unitsFormat(xunits))
        ax.set_ylabel("Volume"+self.__unitsFormat(yunits))

        return self.fig

    def __unitsFormat(self, unitsInput):
        if unitsInput != "":
            unitsOutput = " ("+unitsInput+")"
        else:
            unitsOutput = unitsInput
        return unitsOutput
