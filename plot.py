import matplotlib.pyplot as plt
import numpy as np

class plot:
    """A class used for the graphical display of PK model results

    :param Compartments: a list of compatments in the model (starting with Main followed by periferal comparments in order defined by model), defaults to ["Main", "1", "2", ... , "n"]
    :type Compartments: list, optional
    :param xdata: TimeSeries corrosponding to the data to graph, defaults to having each Y element corrospond to a time step of 1
    :type xdata: list, optional
    :param ydata: a list of drug masses over time. for multidimential imputs each each row is treated as a seprate series, defaults to []
    :type ydata: list, optional
    :param xmin: start point of the time series if time is not explicitly provided in xdata, defaults to 0.0
    :type xmin: int, optional
    :param title: Title displayed above graph, defaults to "PK Model"
    :type title: string, optional
    :param xunits: units for time on the axis, defaults to ""
    :type xunits: string, optional
    :param yunits: units for mass of the drug administered, defaults to ""
    :type yunits: string, optional
    """
    def __init__(self,Compartments = [], xdata = [], ydata = [], xmin = 0, title = "PK Model", xunits="", yunits=""):
        self.Compartments = Compartments
        self.xdata = xdata
        self.ydata = ydata
        self.xmin = xmin


        self.fig = self.setupFig()
        print("init fig "+str(type(self.fig)))
        if ydata != []:
            self.addData(Compartments, xdata, ydata, xmin)

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
    def addData(self, Compartments = [], xdata = [], ydata = [], xmin = 0):
        """A class used for the graphical display of PK model results

        :param Compartments: a list of compatments in the model (starting with Main followed by periferal comparments in order defined by model), defaults to ["Main", "1", "2", ... , "n"]
        :type Compartments: list, optional
        :param xdata: TimeSeries corrosponding to the data to graph, defaults to having each Y element corrospond to a time step of 1
        :type xdata: list, optional
        :param ydata: a list of drug masses over time. for multidimential imputs each each row is treated as a seprate series, defaults to []
        :type ydata: list, optional
        :param xmin: start point of the time series if time is not explicitly provided in xdata, defaults to 0.0
        :type xmin: int, optional
        ...
        :raises [ErrorType]: [ErrorDescription]
        ...
        :return: none
        :rtype: none
        """
        
        print("add data self.fig "+str(type(self.fig)))
        ax = self.fig.add_subplot(1,1,1)


                
        #for series in range(len(ydata)):
        #    plt.plot(timeSeries, ydata[series])
         
        timeSeries = self.__makeTimeSeries(xdata, len(ydata), xmin)
        ax.plot(timeSeries, ydata)




    def __unitsFormat(self, unitsInput):
        if unitsInput != "":
            unitsOutput = " ("+unitsInput+")"
        else:
            unitsOutput = unitsInput
        return unitsOutput

    def __makeTimeSeries(self, xdata, leny, xmin):
        """A class used for the graphical display of PK model results

        :param Compartments: a list of compatments in the model (starting with Main followed by periferal comparments in order defined by model), defaults to ["Main", "1", "2", ... , "n"]
        :type Compartments: list, optional
        :param xdata: TimeSeries corrosponding to the data to graph, defaults to having each Y element corrospond to a time step of 1
        :type xdata: list
        :param leny: interger value of the length of thedata series to be plotted
        :type leny: int
        :param xmin: start point of the time series if time is not explicitly provided in xdata, defaults to 0.0
        :type xmin: int
        ...
        :raises [ErrorType]: [ErrorDescription]
        ...
        :return: none
        :rtype: none
        """
        if xdata != []:
            timeSeries = xdata
        else:
            timeSeries = list(range(xmin,leny))
        return timeSeries

plot(ydata=[1,2,4,6,10,18,30,58])