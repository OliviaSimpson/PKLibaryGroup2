#format
#graph = plot()  #initialise plot class
#graph.adddata([100,50,25,12,6,3,1,0.5],[0,2,3,4,5,6,7,9])  #add a single series as a list folowed by the time series
#graph.adddata([data],[timesereies]) 
#graph.adddata([[1,2,3,5,8,13,21],[15,4,3,2,1,2,3]],[1,2,3,4,5,6,7]) #add two sets of data with a common time series
#graph.adddata([[data1],[data2]],[timesereies]) 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class plot():
    def __init__(self, masses=[],times=[], t0=0, compatmentNames=[], title="PK Model"):
        """A class used for the graphical display of PK model results
        
        :param masses: a list of values descriping the mass of drug present in each compartment. to provide values for multiple 
        compatments masses should be 2-dimentional of the form [[list of results for compatment 1], [list of results for compatment 2]]
        defaults to []
        :type list: list, optional
        :param times: TimeSeries corrosponding to the data the data in masses, defaults to having each Y element corrospond to a time step of 1
        :type times: list, optional
        :param t0: start point of the time series if time is not explicitly provided in times, defaults to 0.0
        :type t0: int, optional
        :param title: Title displayed above graph, defaults to "PK Model"
        :type title: string, optional
        :param xunits: units for time on the axis, defaults to ""
        :type xunits: string, optional
        :param yunits: units for mass of the drug administered, defaults to ""
        :type yunits: string, optional
        :param compatmentNames: list of names for the compatments, defaults to []
        :type compatmentNames: list(, optional)
        """
        self.compatmentNames=compatmentNames
        self.title=title

        times = self.__makeTimeSeries(times, len(masses), t0=0)

        solveData = pd.DataFrame(data = masses, columns=times)
        self.currentData = solveData.transpose()


    def adddata (self,masses=[], Timeseries=[], compatmentNames=[], title="PK Model", show=True):
        """funciton to add data to the output plot 

        :param masses: a list of values descriping the mass of drug present in each compartment. to provide values for multiple 
        compatments masses should be 2-dimentional of the form [[list of results for compatment 1], [list of results for compatment 2]]
        defaults to []
        :param times: TimeSeries corrosponding to the data the data in masses, defaults to having each Y element corrospond to a time step of 1
        :type times: list, optional
        :type list: list, optional
        :param compatmentNames: list of names for the compatments, defaults to []
        :type compatmentNames: list(, optional)
        :param show: boolean to decide if the new data on the graph will automaticaly be displayed, defaults to True
        :type show: boolean(, optional)
        ...
        :raises [ErrorType]: [ErrorDescription]
        ...
        :return: [ReturnDescription]
        :rtype: [ReturnType]
        """
        self.compatmentNames=compatmentNames

        masses = np.array(masses)  
        newtimeseries = self.__makeTimeSeries(Timeseries, len(masses), t0=0)

        if len(masses.shape) == 1:
            masses = pd.DataFrame(data = [masses], columns=newtimeseries)
        else:
            masses = pd.DataFrame(data = masses, columns=newtimeseries)
        masses = masses.transpose()
        self.currentData = pd.concat([self.currentData, masses], axis=1, sort=False)
        
        if show == True:
            self.show()
    def show(self):
        """display the graph containing currentdata

        ...
        :raises [ErrorType]: [ErrorDescription]
        ...
        :return: [ReturnDescription]
        :rtype: [ReturnType]
        """

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


    def __makeTimeSeries(self, times, leny, t0=0):
        """A class used for the graphical display of PK model results
        :param Compartments: a list of compatments in the model (starting with Main followed by periferal comparments in order defined by model), defaults to ["Main", "1", "2", ... , "n"]
        :type Compartments: list, optional
        :param times: TimeSeries corrosponding to the data to graph, defaults to having each Y element corrospond to a time step of 1
        :type times: list
        :param leny: interger value of the length of thedata series to be plotted
        :type leny: int
        :param t0: start point of the time series if time is not explicitly provided in times, defaults to 0.0
        :type t0: int
        ...
        :raises [ErrorType]: [ErrorDescription]
        ...
        :return: none
        :rtype: none
        """
        if times != []:
            timeSeries = times
        else:
            timeSeries = list(range(t0,leny))
        return timeSeries

graph = plot()  #initialise plot class
graph.adddata([100,50,25,12,6,3,1,0.5],[0,2,4,6,8,10,12,14])  #add a single series as a list folowed by the time series