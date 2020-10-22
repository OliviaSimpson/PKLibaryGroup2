#
# Solution class
#
import numpy as np
import matplotlib
import scipy.integrate


class Solution:
    """Module that solves the Pharmokinetic differential equation model
    taking parameters passed to it from other scripts in the package

    Parameters
    ----------

    model: object, specifying the model to be used and the parameters for the
            central and any peripheral compartments
    protocol: object, specifies the dosing protocol used in the model
    timescale: list, specifies the timescale to solve the model for.

    """
    def __init__(self, model, protocol, timescale):
        self.model = model
        self.protocol = protocol
        self.timescale = timescale
        if type(self.timescale) != list:
             print('Timescale must be a list')
             
        
    if self.protocol.type == 'intravenous'
        if self.protocol.method == 'discrete'
            y0 = np.array([self.protocol.d_g, 0.0])
    #This sets up the initial conditions for the ODE such that the amount of drug 
    #in the central compartment at t=0 is the first dose
    
    
        
        

